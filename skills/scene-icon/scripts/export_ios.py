#!/usr/bin/env python3
"""将已确认的方形图稿导出为 iOS 图标，并验证本机渲染与编译。"""

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


RENDITIONS = ("Default", "Dark", "ClearLight", "ClearDark", "TintedLight", "TintedDark")


def run(*arguments):
    return subprocess.run([str(value) for value in arguments], check=True, capture_output=True, text=True).stdout.strip()


def background(value):
    colors = value.split(",")
    if len(colors) not in (1, 2) or any(not re.fullmatch(r"#[0-9a-fA-F]{6}", color) for color in colors):
        raise argparse.ArgumentTypeError("背景需要 #RRGGBB 或 #RRGGBB,#RRGGBB")
    return colors if len(colors) == 2 else colors * 2


def inspect(source):
    width, height, opaque = run("magick", "identify", "-format", "%w %h %[opaque]", source).split()
    if int(width) != int(height):
        raise ValueError(f"请先确认方形构图，脚本不自动裁切或拉伸 {source}")
    return opaque.lower() == "true"


def gradient(colors):
    encoded = ["extended-srgb:" + ",".join(str(int(color[index:index + 2], 16) / 255) for index in (1, 3, 5)) + ",1" for color in colors]
    return {
        "linear-gradient": encoded,
        "orientation": {"start": {"x": 0, "y": 0}, "stop": {"x": 1, "y": 1}},
    }


def write_json(destination, value):
    destination.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def normalize(source, destination, profile):
    run("magick", source, "-auto-orient", "-resize", "1024x1024", "-colorspace", "sRGB", "-depth", "8", "-profile", profile, destination)


def flatten(source, colors, destination, profile):
    run("magick", "-size", "1024x1024", "-define", "gradient:vector=0,0,1023,1023",
        "gradient:" + "-".join(colors), source, "-compose", "over", "-composite",
        "-alpha", "off", "-colorspace", "sRGB", "-depth", "8", "-profile", profile,
        "-define", "png:color-type=2", destination)


def compile_icon(source, destination, minimum_ios):
    destination.mkdir()
    output = run("xcrun", "actool", source, "--platform", "iphoneos",
                 "--target-device", "iphone", "--target-device", "ipad",
                 "--minimum-deployment-target", minimum_ios, "--app-icon", "AppIcon",
                 "--output-format", "human-readable-text", "--errors", "--warnings", "--notices",
                 "--output-partial-info-plist", destination / "Info.plist", "--compile", destination)
    if "com.apple.actool.errors" in output or "com.apple.actool.warnings" in output:
        raise ValueError(output)
    if not (destination / "Assets.car").is_file():
        raise ValueError("actool 未产生 Assets.car")
    for platform in ("CFBundleIcons", "CFBundleIcons~ipad"):
        name = run("plutil", "-extract", platform + ".CFBundlePrimaryIcon.CFBundleIconName", "raw", "-o", "-", destination / "Info.plist")
        if name != "AppIcon":
            raise ValueError(f"{platform} 图标名未正确编译")


def export(args, tool, profile):
    icon = args.output / "AppIcon.icon"
    assets = icon / "Assets"
    assets.mkdir(parents=True)
    normalize(args.source, assets / "Artwork.png", profile)
    light = args.background or ["#FFFFFF", "#FFFFFF"]
    dark = args.dark_background or light
    layers = [{"name": "原画", "image-name": "Artwork.png", "glass": False}]
    fills = [{"value": gradient(light)}]
    if args.dark_background:
        fills.append({"appearance": "dark", "value": gradient(dark)})
    if args.dark_source:
        normalize(args.dark_source, assets / "Dark.png", profile)
        layers[0]["opacity-specializations"] = [{"value": 1}, {"appearance": "dark", "value": 0}]
        layers.append({"name": "深色原画", "image-name": "Dark.png", "glass": False,
                       "opacity-specializations": [{"value": 0}, {"appearance": "dark", "value": 1}]})
    write_json(icon / "icon.json", {
        "fill-specializations": fills,
        "groups": [{"name": "图稿", "layers": layers, "specular": False,
                    "translucency": {"enabled": False, "value": 0},
                    "shadow": {"kind": "none", "opacity": 0}}],
        "supported-platforms": {"squares": ["iOS"]},
    })
    flatten(assets / "Artwork.png", light, args.output / "default.png", profile)
    custom_dark = bool(args.dark_source or args.dark_background)
    if custom_dark:
        dark_art = assets / ("Dark.png" if args.dark_source else "Artwork.png")
        flatten(dark_art, dark, args.output / "dark.png", profile)

    previews = args.output / "previews"
    previews.mkdir()
    for rendition in RENDITIONS:
        for points, scale in ((256, 1), (60, 2), (29, 2)):
            destination = previews / f"{rendition}-{points}pt@{scale}x.png"
            run(tool, icon, "--export-image", "--platform", "iOS", "--rendition", rendition,
                "--width", points, "--height", points, "--scale", scale, "--output-file", destination)
            dimensions = run("magick", "identify", "-format", "%w %h", destination)
            if dimensions != f"{points * scale} {points * scale}":
                raise ValueError(f"预览尺寸错误 {destination}")

    catalog = args.output / "AppIcon.appiconset"
    if args.asset_catalog:
        catalog.mkdir()
        images = []
        for appearance in (["default", "dark"] if custom_dark else ["default"]):
            filename = appearance + ".png"
            shutil.copyfile(args.output / filename, catalog / filename)
            image = {"filename": filename, "idiom": "universal", "platform": "ios", "size": "1024x1024"}
            if appearance == "dark":
                image["appearances"] = [{"appearance": "luminosity", "value": "dark"}]
            images.append(image)
        write_json(catalog / "Contents.json", {"images": images, "info": {"author": "xcode", "version": 1}})

    with tempfile.TemporaryDirectory(prefix="scene-icon-compile-") as temporary:
        scratch = Path(temporary)
        compile_icon(icon, scratch / "native", args.minimum_ios)
        if args.asset_catalog:
            wrapper = scratch / "Images.xcassets"
            wrapper.mkdir()
            write_json(wrapper / "Contents.json", {"info": {"author": "xcode", "version": 1}})
            shutil.copytree(catalog, wrapper / catalog.name)
            compile_icon(wrapper, scratch / "catalog", args.minimum_ios)

    print(json.dumps({
        "output": str(args.output), "custom_appearances": ["Default", "Dark"] if custom_dark else ["Default"],
        "system_derived": list(RENDITIONS[2:] if custom_dark else RENDITIONS[1:]),
        "minimum_ios": args.minimum_ios,
        "native_previews": 18, "compiled": ["Icon Composer", "Asset catalog"] if args.asset_catalog else ["Icon Composer"],
        "visual_review": "请查看 previews 中各外观和小尺寸图像",
    }, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--background", type=background)
    parser.add_argument("--dark-source", type=Path)
    parser.add_argument("--dark-background", type=background)
    parser.add_argument("--asset-catalog", action="store_true")
    parser.add_argument("--minimum-ios", default="18.0", help="与目标项目一致的最低 iOS 版本，默认 18.0")
    args = parser.parse_args()
    if not re.fullmatch(r"\d+(\.\d+){0,2}", args.minimum_ios):
        parser.error("最低 iOS 版本需要形如 18.0 的版本号")
    args.source = args.source.resolve()
    args.output = args.output.absolute()
    if args.dark_source:
        args.dark_source = args.dark_source.resolve()
    if os.path.lexists(args.output):
        parser.error("输出目录已存在，请选择新的目录")
    for command in ("magick", "xcrun", "xcode-select", "plutil"):
        if not shutil.which(command):
            parser.error(f"缺少 {command}，请配置 macOS、完整 Xcode 和 ImageMagick 7")
    developer = Path(os.environ.get("DEVELOPER_DIR") or run("xcode-select", "-p")).resolve()
    tool = developer.parent / "Applications/Icon Composer.app/Contents/Executables/ictool"
    profile = Path("/System/Library/ColorSync/Profiles/sRGB Profile.icc")
    if not tool.is_file() or not profile.is_file():
        parser.error("当前 Xcode 缺少 Icon Composer，或系统缺少 sRGB 色彩配置")
    opaque = inspect(args.source)
    if not opaque and not args.background:
        parser.error("透明前景需要 --background 指定已确认的背景")
    if opaque and args.background:
        parser.error("完整原稿已有背景，--background 仅用于透明前景")
    if opaque and args.dark_background and not args.dark_source:
        parser.error("完整原稿请提供 --dark-source，单改背景无法改变画稿")
    if args.dark_source:
        dark_opaque = inspect(args.dark_source)
        if not dark_opaque and not args.dark_background:
            parser.error("透明深色前景需要 --dark-background")
        if dark_opaque and args.dark_background:
            parser.error("深色原稿已有背景，--dark-background 仅用于透明前景")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.mkdir()
    try:
        export(args, tool, profile)
    except BaseException:
        # 输出目录由本次独占创建，失败时避免留下看似完整的交付物。
        shutil.rmtree(args.output)
        raise


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        if isinstance(error, subprocess.CalledProcessError):
            detail = "\n".join(part for part in (error.stdout, error.stderr) if part).strip() or str(error)
        else:
            detail = str(error)
        print(detail, file=sys.stderr)
        sys.exit(1)
