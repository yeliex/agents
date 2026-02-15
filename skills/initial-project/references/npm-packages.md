# npm 包 Playbook（通用包 / React 组件库）

## 通用 npm 包

### 默认要求

1. 优先使用 `pkgroll` 打包。
2. 产物包含 `ESM + CJS + d.ts`。
3. 配置 `exports` 与 `types`。
4. 提供 `prepublishOnly`，发布前强制构建。

## React 组件库

### 默认要求

1. 最小模板，不默认 Storybook/测试。
2. `react`、`react-dom` 使用 `peerDependencies`。
3. 保持与通用包一致的 `pkgroll` 打包策略。
