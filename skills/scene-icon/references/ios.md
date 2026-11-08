# iOS export and validation

Use available design tools, Icon Composer, and Xcode to prepare the requested iOS resources.

Confirm the target system, minimum deployment version, icon name, and the project's existing icon format. Check the current Apple guidance linked below. Complete the [composition and artwork scale check](../SKILL.md#composition-and-artwork-scale) before export.

## Prepare the artwork

1. Inspect the approved sources, dimensions, color profiles, and alpha channels. Preserve the original files while preparing exports.
2. Prepare a 1024 × 1024 square iOS master using an available export tool. Preserve the approved composition, aspect ratio, and subject/prop relationships. Use sRGB unless the project explicitly requires another profile.
3. Keep square outer edges on source images; the system applies its mask. The default full-color background should cover the canvas. Retain true alpha for separate foreground layers and appearances that need it.
4. Treat an approved flattened illustration as one layer. For separate background or foreground adjustments, use assets with independent layers and appropriate transparency.

## Prepare the native resource

Choose the format required by the project or delivery request.

- **Icon Composer:** Create or open the document, import the approved image or existing layers, preserve placement and appearance, and save `AppIcon.icon` (or the project's chosen name). Configure an editable background only for separated foregrounds. Check material effects against the approved appearance before applying them. Create and edit the document through the current Icon Composer UI or an existing supported project workflow.
- **Asset catalog:** Add the approved master to the project's `AppIcon.appiconset` within an `.xcassets` catalog. Follow the project's single-size or individual-size configuration. Add custom dark/tinted assets only when available and requested; current Apple guidance uses a transparent background for a custom Dark asset and grayscale for Tinted.

Use the host's computer-use capability for app UI interaction. If there is an existing native resource, work from a copy and retain its settings unless a change is required. When adding an `.icon` file to an app, check the existing catalog configuration and select the intended app icon source.

Native compilation requires macOS and a selected full Xcode installation. Check the selected tools with `xcode-select -p` and `xcrun --find actool`. Icon Composer may also be installed separately for design work.

## Inspect appearance and readability

Use Icon Composer to review the appearances supported by the selected toolchain and target system: default, dark, and the supported clear/tinted variants. Check composition, clipping, and recognition at the sizes relevant to the app, such as 60 pt and 29 pt. Inspect within the tool where possible; render temporary images when needed for the check. Derive pixel dimensions from the chosen display scale.

When an exported image is needed for inspection or requested review, the installed `ictool` can render an existing `.icon` document directly. Inspect its help first; the following example uses the tool bundled with the selected Xcode. Replace the paths and create the preview directory before running it:

```sh
task_developer_dir="${DEVELOPER_DIR:-$(xcode-select -p)}"
task_ictool="$task_developer_dir/../Applications/Icon Composer.app/Contents/Executables/ictool"
"$task_ictool" --help
"$task_ictool" /project/AppIcon.icon --export-image \
  --platform iOS --rendition Default --width 60 --height 60 --scale 2 \
  --output-file /project/icon-work/previews/Default-60pt@2x.png
```

Use only rendition names and options supported by that installation. If the executable is unavailable, use Icon Composer's export UI. Inspection renders are temporary checks; include them in delivery only when requested.

Inspect the icon in the tool or temporary renders for clipping, top/side spacing, small-size recognition, and separation from backgrounds. Compare variants at equal sizes. Without custom dark artwork, the system Dark appearance may resemble Default. Clearly distinguish supplied custom artwork from system-derived appearances.

## Compile and deliver

When a target project is available, use its configured Xcode build to validate integration. For standalone resource delivery, invoke `actool` directly.

Set `task_icon_input` to the `.icon` document or the containing `.xcassets` catalog, `task_icon_name` to the resource name, `task_minimum_ios` to the target deployment version, and `task_compile_dir` to a new task-owned scratch directory. Match the target-device flags to the app; this example includes iPhone and iPad:

```sh
xcrun actool "$task_icon_input" --platform iphoneos \
  --target-device iphone --target-device ipad \
  --minimum-deployment-target "$task_minimum_ios" --app-icon "$task_icon_name" \
  --output-format human-readable-text --errors --warnings --notices \
  --output-partial-info-plist "$task_compile_dir/Info.plist" \
  --compile "$task_compile_dir"
```

Inspect the exit status and diagnostics, confirm that `Assets.car` exists, and check the generated icon name in `Info.plist` for the selected devices. Resolve relevant warnings. Record resource compilation and target-app integration as separate validation results.

Deliver the requested icon file or native resource, plus editable sources when needed. Include comparison or preview files only when requested. Record the toolchain and checks actually completed. Clean up temporary inspection files created for this task after review, preserving source files and final resources.

If native tools are unavailable, deliver the final icon image and identify the native rendering or compilation checks that remain unverified.

## Sources

- [Apple App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons/)
- [Icon Composer](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer)
- [Asset catalog icon configuration](https://developer.apple.com/documentation/xcode/configuring-your-app-icon)
