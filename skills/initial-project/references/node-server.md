# Node Server Playbook（强制默认栈）

## 目标

初始化可运行的 Node 后端项目，默认技术栈：

- `@yeliex/fastify`
- `fastify`
- `@fastify/type-provider-typebox`
- `@sinclair/typebox`
- Prisma 作为可选 ORM

## 目录建议

- `src/app.ts`
- `src/server.ts`
- `src/routes/`

## 最小脚本建议

- `start`: 使用 `tsx watch` 或等效命令启动开发进程
- `build`: 产出 `dist`
- `test:type`: `tsc --build --verbose` 或 `tsc --noEmit`
