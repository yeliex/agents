# iOS export and validation

Confirm the target system and the project's icon format. Check Apple's current requirements and the appearances supported by the installed Xcode. The included script packages approved square artwork while preserving its proportions and composition. Complete the [composition and artwork scale check](../SKILL.md#composition-and-artwork-scale) first: the script does not automatically shrink an overcrowded subject, and successful compilation does not replace this check.

## Environment and commands

Generate images with the host's image tool. The iOS export script requires macOS, a selected full Xcode installation, Icon Composer, Python 3.9+, and ImageMagick 7's `magick` command.

Resolve the script path relative to this skill directory and use absolute input and output paths. The output directory must not already exist. Set `--minimum-ios` to the project's minimum deployment target; the default is 18.0.

```sh
python3 <skill-directory>/scripts/export_ios.py \
  --source /project/icon-source.png \
  --output /project/outputs/AppIcon
```

Complete artwork can be passed directly. Transparent foregrounds require an explicit background, either a solid color or a two-color gradient from top left to bottom right.

```sh
python3 <skill-directory>/scripts/export_ios.py \
  --source /project/foreground.png \
  --background '#E1E8DF,#B1C3AE' \
  --dark-background '#606C5E,#2F382E' \
  --asset-catalog \
  --output /project/outputs/AppIcon
```

These colors demonstrate the argument format only. For other gradient directions, prepare the background in the approved complete artwork and pass that as a complete layer.

Pass separately approved dark artwork with `--dark-source /project/dark-source.png`. A transparent dark foreground also requires `--dark-background`. Background arguments only change the background behind a transparent foreground. Complete artwork needs a separate dark image or the system-rendered appearance.

## Outputs and checks

- `AppIcon.icon` contains normalized image layers and the specified background. Transparent foregrounds retain alpha and the background remains editable. Complete artwork stays a complete layer.
- `default.png`, and `dark.png` when a custom dark appearance is supplied, are 1024 × 1024 sRGB square exports.
- `previews/` contains six appearances rendered by the installed Icon Composer, including 60 pt and 29 pt previews at 2×. These sizes serve the current check; add previews for other actual placements as needed.
- `--asset-catalog` also creates `AppIcon.appiconset` for projects that need an asset catalog.
- The script uses `actool` to validate iPhone and iPad compilation, then removes temporary build files. Its terminal report distinguishes custom and system-derived appearances and records the checks performed.

Open previews to inspect system clipping, edges, small-size recognition, separation against dark backgrounds, and identifying features in clear and tinted appearances. Compilation proves that the current toolchain can process the resources; appearance quality still requires visual inspection. Without a custom dark design, system Dark may look identical to Default. Supply approved dark artwork or a transparent foreground with a dark background when a different dark design is needed. Generating a preview file does not establish visual adaptation.

The default full-color background should cover the square canvas. Apply transparency rules according to the asset's role and appearance; separate foregrounds may be transparent. The script's default and custom dark PNGs are complete artwork composited over confirmed backgrounds. For a transparent Dark resource that uses the system background, follow the target project's convention with the original transparent layer.

If only image generation is available, deliver artwork and small-size previews first. If Xcode is unavailable, list the native previews and compilation checks that remain unverified. Do not describe a simulated rounded-corner image as a system-validated preview.

## Sources

- [Apple App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons/)
- [Icon Composer](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer)
- [Asset catalog icon configuration](https://developer.apple.com/documentation/xcode/configuring-your-app-icon)
