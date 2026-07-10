---
name: network-proxy-rule
description: 网络连接策略 — 默认直连，失败时提示开梯子后用代理重试
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 28b96d97-1a82-42a3-bcf3-aa05feb1b4ea
---

# 网络连接策略（严格执行）

## 默认行为
所有网络请求默认走**直连**（不使用代理）。包括但不限于：`git`、`gh` CLI、`curl`、`npm`、`pip`、`wget`、`go get`、`cargo`、以及任何需要访问 GitHub 或外部网络的操作。

## 代理信息
- 代理地址：`http://127.0.0.1:7897`
- 代理类型：HTTP（Clash Verge 混合端口）

## 连接失败处理流程
1. 当任何网络操作因为**连接超时/被拒绝/被墙**而失败时，**不要反复重试**
2. **立即停止当前操作**，向用户明确提示连接失败，要求用户打开梯子（Clash Verge）
3. 等待用户确认梯子已打开后，设置临时代理并重试：
   ```bash
   export HTTPS_PROXY=http://127.0.0.1:7897
   export HTTP_PROXY=http://127.0.0.1:7897
   ```
4. 对于 `git` 操作，额外设置：
   ```bash
   git config --global http.proxy http://127.0.0.1:7897
   git config --global https.proxy http://127.0.0.1:7897
   ```
5. 操作完成后，**不主动清除**当前会话的代理环境变量（保持可用）
6. **禁止**私自永久写入代理配置到系统环境变量或 git 全局配置

**Why:** 用户平时走内网直连，仅在需要时手动开启梯子。你必须在连接失败时主动提示，而非静默失败或反复重试。禁止在没有提示的情况下直接假设梯子是开着的。

**How to apply:** 每次执行网络操作前不预设代理；操作失败且错误信息指向连接问题（timeout/refused/reset/blocked）时，停止并提示用户开梯子。用户确认后再带代理重试，只重试一次。
