---
name: mmd-projects
description: 用户的 MMD 创作项目与工具配置记录
metadata: 
  node_type: memory
  type: project
  originSessionId: 873f87f5-a7b2-49a2-b3a5-3d1d58491ac5
---

# MMD 创作项目

## 当前项目：炉心融解（Meltdown）
- 歌曲：**炉心融解** — iroha(sasaki) 创作，镜音铃演唱
- 主题：核融合炉、时空循环、记忆消逝、人格分裂
- 状态：制作中

### 知更鸟建议的滤镜方案
推荐**混合使用**按段落切换：

| 段落 | 滤镜 | 效果 |
|------|------|------|
| 前奏钢琴独奏 | 黑白→渐染冷蓝 | 沉寂到崩坏的过渡 |
| 主歌 | 水底朦胧+柔光 | 记忆模糊感 |
| 副歌"真っ青な光" | 核蓝调+高光溢出 | 核心爆发 |
| 桥段间奏 | Glitch+RGB分裂 | 混乱感 |
| 最后一句 | 褪色回黑白，只剩一滴蓝 | 归于虚无 |

## 工具：Hiragana LipSync（口型自动生成）

### 项目位置
`E:\0\MMD\嘴型自动生成Hiragana-LipSync-main`

### 用途
从日语WAV/MP3音频自动生成MMD口型VMD文件（あいうえおん6种口型）

### 技术栈
- **Python**: C:\Python312\python.exe (3.12.9)
- **PySide6 6.11.1** — GUI界面
- **PyTorch 2.11.0+cu128** — GPU版（CUDA 12.8）
- **GPU**: NVIDIA GeForce RTX 4060 Laptop GPU (8GB VRAM)
- **模型**: TylorShine/wavlm-base-plus-hiragana-ctc-v2（366MB safetensors，本地 model/ 目录）

### 修改记录
- GPU默认启用（`setChecked(True)`）
- VMD导出路径 → `d:\AiYi\Downloads\`
- 启动批处理使用 `pushd` 修复路径问题

### 使用方法
双击 `启动.bat`，拖入日语WAV/MP3，点击「生成VMD」

**Why:** 用户正在进行的创作项目及配套工具，后续可能继续讨论进度或寻求建议。
**How to apply:** 当用户提到 MMD、口型同步或炉心融解时，可以询问进度或继续深入讨论效果方案。
