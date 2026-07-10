---
name: github-backup-rule
description: GitHub 记忆备份规则 — 先读仓库再行动，不做重复无用工
metadata: 
  node_type: memory
  type: reference
  originSessionId: af1f1c3c-41b6-4553-9ffa-aaebda45d1d1
---

# GitHub 记忆备份规则

所有关键记忆同步备份在 GitHub 仓库中：

- **仓库**: https://github.com/Aiyi-xbla/robin-tts
- **备份路径**: `memory-backup/` 目录下

## 使用规则

1. **每次工作前**：先检查 GitHub 仓库的 `memory-backup/`，确认已有记录
2. **不要重复做**：已经记录过的修复、方案、配置，直接引用而非重新排查
3. **新增时同步**：更新记忆文件时，同时更新 GitHub 仓库
4. **覆盖范围**：TTS 修复、MikuChat 配置、MMD 项目、用户偏好、对话历史等

**Why:** 避免反复排查已解决的问题，节省时间精力。
**How to apply:** 涉及项目配置、修复方案、用户偏好时，先查 GitHub 上的记忆备份再行动。
