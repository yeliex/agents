# Frontend Playbook（Vite / Next.js）

默认情况下，前端项目或 monorepo 中的前端子项目统一基于 Vite 或 Next.js 初始化。

- Next.js：需要 SSR/SSG 能力，面向营销站点、企业官网、C 端应用。
- Vite：其他场景，包括 SPA 和后台类应用。

## 公共偏好细则
1. 页面文件优先使用 `.page.tsx` 后缀，保持语义清晰。
2. 布局与路由可对应使用 `.layout.tsx`、`.route.tsx`。
3. 样式方案优先 `tailwindcss`，除非用户明确提出其他方案。
4. 组件与数据层默认偏好：`shadcn/ui`、`react-hook-form`、`swr`。

## Vite 分支

1. 使用官方命令创建 TypeScript 项目。
2. 确保 `type: module` 与 ESM 导入风格。
3. 套用公共偏好（tsconfig、.node-version、.editorconfig、.npmrc）。

## Next.js 分支

1. 使用官方命令创建 TypeScript 项目。
2. 保持默认推荐结构，不额外引入重型工具。
3. 套用公共偏好（tsconfig、.node-version、.editorconfig、.npmrc）。

## 前端默认边界

1. 除非用户明确要求，不默认安装 Storybook、Vitest 等工具。
