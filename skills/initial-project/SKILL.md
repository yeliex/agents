---
name: initial-project
description: 初始化 Node 服务、Vite/Next.js 前端和 npm 包；用于创建项目、搭脚手架或选择新项目类型。
---

# 项目初始化路由 Skill

## 目标

根据用户要求和现有上下文选择项目类型，完成初始化和与项目类型匹配的最小验证。

## 执行原则

1. 用户明确要求优先；在既有项目或 monorepo 中沿用现有规范。本技能及引用文档中的默认偏好只用于尚未确定的配置，保留框架必需的结构和配置。
2. 使用中文说明流程、决策和结论，保持代码与配置键名英文。
3. 根据用户要求、当前目录和已有配置确定项目名、项目类型、目标目录及仓库形态；信息充分时直接执行，不重复确认。
4. 仅在缺失信息会实质改变目录结构、脚手架或 npm 包发布配置，且无法从上下文合理确定时提问。其他细节采用默认值并简要说明；等待回答时继续不依赖该信息的已授权工作。
5. 使用包管理器命令添加依赖，不直接修改依赖列表字段。

## 项目路由

只读取所选类型对应的文档：

| 项目类型 | 文档 |
| --- | --- |
| Node 服务（`node-server`） | [references/node-server.md](references/node-server.md) |
| Vite / Next.js 前端（`frontend-vite` / `frontend-nextjs`） | [references/frontend.md](references/frontend.md) |
| npm 通用包 / React 组件库（`npm-package-general` / `npm-package-react`） | [references/npm-packages.md](references/npm-packages.md) |

独立项目直接在目标目录初始化；加入已有 monorepo 时沿用其 workspace 配置。新建 monorepo 默认按 `apps/* + packages/*` 组织，并创建 `pnpm-workspace.yaml`。

## 默认偏好

1. 包管理器：`pnpm`。
2. 使用 `TypeScript only + ESM`。
3. Node 版本：最新 LTS major；在项目根 `.node-version` 写入 `lts/*`。
4. `tsconfig` 继承顺序：`@tsconfig/strictest` -> `@tsconfig/nodeXX` -> `@yeliex/tsconfig`，`nodeXX` 按目标 Node major 选择。
5. `.editorconfig` 基于 [templates/editorconfig](templates/editorconfig) 生成。
6. 不默认安装 husky、lint-staged、Storybook 或 Vitest。

### Registry 配置

沿用用户指定或项目已有的 registry 与作用域配置。目标项目尚无配置时，创建 `.npmrc`：

- git 远端域名包含 `gitlab.qima-inc.com`：`registry=http://registry.npm.qima-inc.com`。
- 其他情况：`registry=https://registry.npmjs.org/`。

## 完成与验证

- 应用完成与生成脚本匹配的最小构建或启动检查；npm 包完成构建，并确认 `exports`、`types` 指向存在的产物。
- 修复本次初始化造成的问题后，只重跑相关检查，不为验证额外引入测试框架。依赖安装或必要检查未通过时，明确说明未完成项。
- 简要输出项目类型、采用的默认值、关键文件、验证结果，以及后续启动或构建命令。
