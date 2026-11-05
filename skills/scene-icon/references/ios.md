# iOS 导出与验收

先确认目标系统和项目采用的图标格式。使用时核对 Apple 当前规范以及本机 Xcode 支持的外观。本技能附带脚本处理已确认的方形原稿，保持其比例和构图。导出前先完成 [构图与元素占比检查](../SKILL.md#构图与元素占比)；脚本不会自动为偏满的构图缩小主体，编译通过也不能替代这项检查。

## 环境与执行

生成图片本身使用宿主图像工具。以下 iOS 导出脚本需要 macOS、已选择的完整 Xcode、Icon Composer、Python 3.9+ 和 ImageMagick 7 的 `magick` 命令。

脚本路径相对于本技能目录，输入和输出使用绝对路径。输出目录必须尚不存在。用 `--minimum-ios` 指定目标项目的最低 iOS 版本，省略时按 18.0 校验。

```sh
python3 <skill目录>/scripts/export_ios.py \
  --source /项目/icon-source.png \
  --output /项目/outputs/AppIcon
```

完整画稿可以直接传入。透明前景需要明确指定背景，支持单色或由左上到右下的双色渐变。

```sh
python3 <skill目录>/scripts/export_ios.py \
  --source /项目/foreground.png \
  --background '#E1E8DF,#B1C3AE' \
  --dark-background '#606C5E,#2F382E' \
  --asset-catalog \
  --output /项目/outputs/AppIcon
```

示例颜色仅演示参数格式。其他方向的渐变可以先在已选定的完整画稿中完成，再作为完整图层输入。

使用单独确认的深色画稿时传入 `--dark-source /项目/dark-source.png`。透明的深色画稿同样需要 `--dark-background`。只有透明前景可以通过背景参数直接改变底色；完整画稿的深色外观由独立深色画稿或系统生成。

## 产物与检查

- `AppIcon.icon` 包含标准化的图像图层和已指定的背景。透明前景保留 alpha，背景在工程中可编辑。完整画稿作为完整图层保留。
- `default.png` 及有自定义深色方案时的 `dark.png` 为 1024 × 1024 sRGB 方形导出。
- `previews/` 包含本机 Icon Composer 的六种外观，以及 60 pt、29 pt 的 2× 预览。尺寸用于本次检查，可按实际使用位置追加预览。
- `--asset-catalog` 额外创建 `AppIcon.appiconset`，用于需要资源目录的项目。
- 脚本调用 `actool` 验证 iPhone、iPad 编译，临时编译文件在退出后清理。终端记录自定义外观、系统衍生外观及检查结果。

打开预览检查系统裁切、边缘、缩小后的识别、深色背景中的分离度，以及透明和着色外观下的主要特征。成功编译证明资源可被当前工具链处理，系统外观的视觉检查仍需实际查看。未提供自定义深色方案时，系统 Dark 可能与默认画面相同；需要不同深色视觉时，应提供已确认的深色原稿或透明前景与深色背景，不把生成预览文件等同于完成外观适配。

默认全彩图的背景应完整覆盖方形画布。透明度规则按素材角色和外观分别处理，独立前景允许透明。当前脚本的默认和自定义深色 PNG 都是确认背景后的完整画稿；需要系统背景的透明 Dark 资源时，按目标项目约定使用原始透明图层。

生成工具只有图片能力时可先交付原稿与缩小预览。缺少 Xcode 时明确列出尚未完成的原生预览和编译校验，避免将普通圆角模拟图描述成系统验证结果。

## 规范来源

- [Apple App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons/)
- [Icon Composer](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer)
- [Asset catalog 图标配置](https://developer.apple.com/documentation/xcode/configuring-your-app-icon)
