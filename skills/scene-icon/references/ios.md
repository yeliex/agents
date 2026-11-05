# iOS export and validation

The agent performs this workflow with available design tools, Icon Composer, and Xcode. This skill does not bundle an exporter or require a separate Python/ImageMagick runtime. Keep any task-specific commands and generated files in the task's output directory.

Confirm the target system, minimum deployment version, icon name, and the project's existing icon format. Check the current Apple guidance linked below. Complete the [composition and artwork scale check](../SKILL.md#composition-and-artwork-scale) before export; resizing an image or compiling a resource does not establish that its composition works.

## Prepare the artwork

1. Inspect the approved sources, dimensions, color profiles, and alpha channels. Preserve the original files and choose a new output location unless replacement is authorized.
2. Prepare a 1024 × 1024 square iOS master using an available export tool. Preserve proportions and the approved subject/prop relationships. Do not stretch, silently crop, or enlarge the scene to fill the canvas. Use sRGB unless the project explicitly requires another profile.
3. Keep square outer edges on source images; the system applies its mask. The default full-color background should cover the canvas. Retain true alpha for separate foreground layers and appearances that need it.
4. Keep a complete illustration as a complete layer when that is the approved source. Only describe a background or foreground as editable separately when those layers actually exist. A custom dark background cannot recolor an opaque full-scene image.

## Prepare the native resource

Choose the format required by the project or delivery request; do not automatically produce both formats.

- **Icon Composer:** Create or open the document, import the approved image or existing layers, preserve placement and appearance, and save `AppIcon.icon` (or the project's chosen name). Configure an editable background only for separated foregrounds. Inspect material effects before applying them; packaging must not silently change the selected illustration. Use the current Icon Composer UI or an existing supported project workflow, rather than treating a hand-written `icon.json` schema as a stable public API.
- **Asset catalog:** Add the approved master to the project's `AppIcon.appiconset` within an `.xcassets` catalog. Follow the project's single-size or individual-size configuration. Add custom dark/tinted assets only when available and requested; current Apple guidance uses a transparent background for a custom Dark asset and grayscale for Tinted. Do not generate extra variants by assumption.

Use the host's computer-use capability for app UI interaction. If there is an existing native resource, work from a copy and retain its settings unless a change is required. When adding an `.icon` file to an app, check the project's existing catalog configuration: Icon Composer can replace its existing app icon, so do not assume both resources will be used together.

Native compilation requires macOS and a selected full Xcode installation. Check the selected tools with `xcode-select -p` and `xcrun --find actool`. Icon Composer may also be installed separately for design work. Do not make image-only delivery depend on installing Xcode.

## Render and inspect previews

Use Icon Composer to review the appearances supported by the selected toolchain and target system: default, dark, and the supported clear/tinted variants. Export a larger view and actual small display sizes relevant to the app, such as 60 pt and 29 pt. Derive pixel dimensions from the chosen display scale; these examples are not a universal required preview count.

For an existing `.icon` document, the installed `ictool` can render previews directly. Inspect its help first; the following example uses the tool bundled with the selected Xcode. Replace the paths and create the preview directory before running it:

```sh
task_developer_dir="${DEVELOPER_DIR:-$(xcode-select -p)}"
task_ictool="$task_developer_dir/../Applications/Icon Composer.app/Contents/Executables/ictool"
"$task_ictool" --help
"$task_ictool" /project/AppIcon.icon --export-image \
  --platform iOS --rendition Default --width 60 --height 60 --scale 2 \
  --output-file /project/icon-work/previews/Default-60pt@2x.png
```

Use only rendition names and options supported by that installation. If the executable is unavailable, use Icon Composer's export UI; do not invent CLI flags. Rendered preview images are presentation artifacts, not replacements for unmasked source artwork.

Open the previews and inspect clipping, top/side spacing, small-size recognition, and separation from backgrounds. Compare variants at equal sizes. Without custom dark artwork, the system Dark appearance may resemble Default. Clearly distinguish supplied custom artwork from system-derived appearances. Merely creating preview files does not establish visual adaptation.

## Compile and deliver

When a target project is available, use its configured Xcode build to validate integration. For standalone resource delivery, the agent can invoke `actool` directly without a skill-specific wrapper.

Set `task_icon_input` to the `.icon` document or the containing `.xcassets` catalog, `task_icon_name` to the resource name, `task_minimum_ios` to the target deployment version, and `task_compile_dir` to a new task-owned scratch directory. Match the target-device flags to the app; this example includes iPhone and iPad:

```sh
xcrun actool "$task_icon_input" --platform iphoneos \
  --target-device iphone --target-device ipad \
  --minimum-deployment-target "$task_minimum_ios" --app-icon "$task_icon_name" \
  --output-format human-readable-text --errors --warnings --notices \
  --output-partial-info-plist "$task_compile_dir/Info.plist" \
  --compile "$task_compile_dir"
```

Inspect the exit status and diagnostics, confirm that `Assets.car` exists, and check the generated icon name in `Info.plist` for the selected devices. Resolve relevant warnings instead of assuming a zero exit status proves every appearance is suitable. Standalone compilation does not prove integration into an app that was not built.

Deliver the approved master, required editable/native resources, and inspected previews. Record the toolchain and checks actually completed. Remove only scratch files created for this task when no longer needed; preserve sources and unrelated outputs. Do not add a reusable exporter or test suite to the skill as part of delivery.

If native tools are unavailable, deliver the artwork and available small-size previews, and identify the native rendering or compilation checks that remain unverified. Do not describe a simulated rounded-corner preview as system-validated.

## Sources

- [Apple App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons/)
- [Icon Composer](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer)
- [Asset catalog icon configuration](https://developer.apple.com/documentation/xcode/configuring-your-app-icon)
