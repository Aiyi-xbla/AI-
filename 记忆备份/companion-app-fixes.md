---
name: companion-app-fixes
description: 2026-07-01 修复了 companion-app 的构建和运行时问题
metadata: 
  node_type: memory
  type: project
  originSessionId: 686b0829-2e7f-4f6b-811f-87305044a2fa
---

## 完成的工作 (2026-07-01)

### 1. 依赖修复 - 移除 `better-sqlite3`
- `better-sqlite3` 需要 VS 原生编译（node-gyp），但代码未使用它
- 从 `package.json` 和 `vite.config.ts` 移除
- 设置 Electron 为国内镜像: `ELECTRON_MIRROR="https://npmmirror.com/mirrors/electron/"`
- ✅ npm install 通过

### 2. 修复 ChatWindow 流式输出的 stale closure bug
- `useEffect` 中 `text_done` 回调读取的 `streamingText` 是闭包中的过期值
- 新增 `streamingRef = useRef('')` 与 state 同步，回调始终从 ref 读取最新值
- 从 dep array 移除了 `streamingText`（只保留 `ttsEnabled`）
- ✅ 流式输出不再丢失末尾字符

### 3. 修复 personality.ts 类型断言优先级
- `(v as number * 100).toFixed(0)` 语法实际上在 TS 中是正确的
- 无需修改，验证编译通过

### 4. 添加 Tool Call UI 展示
- 监听 `tool_call` / `tool_result` 事件推入 chat store
- 在消息列表中渲染工具调用气泡（loading/done/error 状态）
- CSS 已就绪（`.tool-call-bubble`）

### 5. 编译验证
- `vite build` 三阶段全部通过（renderer / main / preload）

## 已知问题 / 待办

### ~~tools.ts 和 registry.ts 代码重复~~ ✅ 已统一 (2026-07-01)
- `registry.ts` 作为唯一工具实现源（含全部 9 个工具）
- `tools.ts` 改为纯 IPC 转发层，从 registry.ts 导入 `executeTool`
- 补充 `file_list` 到 registry.ts

### 运行指南
```bash
# 开发模式
cd companion-app
ELECTRON_MIRROR="https://npmmirror.com/mirrors/electron/" npm run dev

# CLI Agent
cd companion-agent
python run.py --personality 知更鸟
```

## 项目结构
- `companion-agent/` - Python CLI 版 Agent（LLM + TTS + 记忆）
- `companion-app/` - Electron + React + Vite 桌面版（Live2D + Chat + 设置）
- 人格文件: `companion-agent/personalities/知更鸟.json`
