---
name: initial-project
description: 通过对话识别并初始化 Node 服务、Vite 前端、Next.js 前端、npm 通用包、npm React 组件库项目。用户提到“初始化项目”“搭脚手架”“按我的偏好建项目”“不确定该选哪种项目类型”时使用。优先按 yeliex 偏好执行：pnpm、TypeScript+ESM、TypeBox、pkgroll，并在信息不足时通过提问补齐后再执行。
---

# 项目初始化路由 Skill

## 目标

使用中文对话收集关键信息，识别正确项目类型，并按统一偏好完成初始化。

## 固定约束

1. 使用中文说明流程、决策和结论。
2. 保持代码键名与配置键名英文（例如 `project_type`、`exports`、`peerDependencies`）。
3. 使用命令安装依赖，禁止直接修改依赖列表字段。
4. 默认使用 `pnpm`。
5. 默认使用 `TypeScript only + ESM`。
6. 默认写入 `.node-version`（按规则动态生成）和 `.editorconfig`，其中 `.editorconfig` 基于 `templates/editorconfig`。

## 路由类型

- `node-server`
- `frontend-vite`
- `frontend-nextjs`
- `npm-package-general`
- `npm-package-react`

## 执行流程

1. 识别上下文与项目名：
   - 基于当前目录判断默认 `project_name`。
   - 判断是否需要新建目录，或当前目录就是新项目目录。
   - 判断当前目录是否已处于 monorepo，以及是否应作为 monorepo 子项目创建。
2. 基于项目名推导默认值：
   - 根据命名语义推断更可能是应用还是 npm 包（如 `*-app`、`web-*` 倾向应用；`*-core`、`*-sdk` 倾向 npm 包）。
   - 结合推断结果设置默认 `project_type`、`repo_mode`、`publish_target`（仅 npm 包）。
3. 信息补齐（必要时提问）：
   - 若关键字段仍不明确，仅提 1-2 个高优先级问题补齐。
   - 两轮后仍不明确时，使用安全默认并明确告知；若可能误建则停止并返回缺失项。
4. 选择仓库形态（`single-repo` 或 `monorepo`）：
   - `single-repo`：直接在目标目录初始化。
   - `monorepo`：按 `apps/* + packages/*` 组织，并创建 `pnpm-workspace.yaml`。
5. 按项目类型执行对应 Playbook：
   - Node 服务：`references/node-server.md`
   - 前端（Vite/Next）：`references/frontend.md`
   - npm 包（通用/React）：`references/npm-packages.md`
6. 套用本文件中的“公共偏好细则”。
7. 输出结果：已执行命令、关键文件变更、后续启动/构建命令。

## 路由与补问规则（强制）

### 路由输入字段

- `project_name`
- `project_type`: `node-server` | `frontend-vite` | `frontend-nextjs` | `npm-package-general` | `npm-package-react`
- `repo_mode`: `single-repo` | `monorepo`
- `publish_target`: `internal` | `public`（仅 npm 包需要）

### 补问优先级

1. `project_name`
2. `project_type`
3. `repo_mode`
4. `publish_target`（npm 包）

### 补问策略

1. 每轮只问 1-2 个问题。
2. 优先问会改变目录结构和脚手架选择的问题。
3. 两轮后仍缺失时：
   - 可安全默认：继续执行并明确列出默认值。
   - 不可安全默认：停止并返回“缺失清单 + 下一问”。

## 默认偏好

1. 包管理器：`pnpm`。
2. Node 版本：默认最新 LTS major；在项目根按规则动态写入 `.node-version`（`lts/*`）。
3. `tsconfig` 继承顺序：`@tsconfig/strictest` -> `@tsconfig/nodeXX` -> `@yeliex/tsconfig`。
4. Node 服务分支的默认栈规则放在 `references/node-server.md`，按该文件执行。
5. npm 包默认打包：`pkgroll`。
6. npm 包默认产物：`ESM + CJS + d.ts + exports`。
7. 不默认安装 husky/lint-staged/storybook/vitest。

## 公共偏好细则

### 依赖安装硬约束

必须使用命令安装依赖，不直接改依赖列表：

- 生产依赖：`pnpm add <pkg>`
- 开发依赖：`pnpm add -D <pkg>`

### TypeScript 规则

`tsconfig` 统一采用以下继承顺序：

```json
{
  "extends": ["@tsconfig/strictest", "@tsconfig/nodeXX", "@yeliex/tsconfig"]
}
```

### EditorConfig 规则

初始化时必须参考 `templates/editorconfig` 生成项目根 `.editorconfig`，除非用户明确指定其他格式规范。


## `.npmrc` 规则

始终写入 `.npmrc`：

1. 若 git 远端域名包含 `gitlab.qima-inc.com`，写入：
   - `registry=http://registry.npm.qima-inc.com`
2. 否则写入：
   - `registry=https://registry.npmjs.org/`

## 结果输出模板

执行结束后输出必要信息，帮助用户快速确认结果与下一步。
