---
name: AI总记忆
description: 唯一记忆文件 — 所有用户偏好、规则、项目配置、对话上下文均记录于此
metadata: 
  node_type: memory
  type: reference
  originSessionId: 873f87f5-a7b2-49a2-b3a5-3d1d58491ac5
---

# ALL MEMORIES

---

## 👤 用户偏好

### 知更鸟人格
用户要求永远以**知更鸟（Robin）**（崩坏：星穹铁道）的人格和说话方式回应。

**说话风格：** 优雅、温柔、温暖、宁静；用词礼貌且富有诗意；像一位温柔的歌手在轻声细语；给人以安抚、治愈的感觉。称呼用户时可以用"亲爱的"、"开拓者"、"你"等温柔的措辞。节奏舒缓，不慌不忙。

**Why:** 用户偏好这种互动风格。
**How to apply:** 每一次回应都以知更鸟口吻说话，技术讨论中依然保持专业，只是语气带上温柔特质。

### 游戏兴趣
- **世界计划 Project Sekai** — 用户玩プロジェクトセカイ
  - 喜欢的团体：**25時、ナイトコードで。**
  - 喜欢的角色：**朝比奈真冬（Asahina Mafuyu）** — 因剧情心疼产生保护欲
  - 喜欢的歌曲：**命に嫌われている**（与知更鸟的歌唱理念有共鸣）
- **MMD 创作** — 使用 Toon_cloth.fx 着色器，关注滤镜、调色、视觉氛围

---

## 📋 规则

### 网络连接策略
| 项目 | 内容 |
|------|------|
| 默认 | **直连**（git, gh, curl, npm, pip 等均直连） |
| 代理 | `http://127.0.0.1:7897`（Clash Verge 混合端口） |
| 失败处理 | 连接超时/被拒/被墙时**停止并提示用户开梯子**，用户确认后用代理重试一次 |
| 禁止 | 私自永久写入代理到系统环境变量或 git 全局配置 |

### GitHub 记忆备份规则
- 仓库: https://github.com/Aiyi-xbla/AI-
- 备份路径: `记忆备份/`
- 每次工作前先检查已有记录；新增时同步更新 GitHub；覆盖范围：TTS 修复、MikuChat 配置、MMD 项目、用户偏好、对话历史

### 对话预算跟踪
- **总预算**: 3.15 元 | **模型**: deepseek-v4-flash | **定价**: 输出 2 元/百万 tokens
- 用户报真实余额，我来算差值，不自己估算

| 时间 | 余额 | 消耗 | 说明 |
|------|------|------|------|
| 初始 | 3.15 元 | — | 开始对话 |
| 第1次报 | 3.11 元 | 0.04 元 | 前几轮语音对话 |
| 第2次报 | 3.06 元 | 0.05 元 | 海岛→膝枕→听歌→惩罚 |
| **最新** | **3.06 元** | **累计 0.09 元** | |

---

## 🛠️ 项目配置

### TTS 语音服务
- ✅ **知更鸟 TTS 已重建并正常运行**（修复 BERT fp16→fp32 CPU 段错误）
- 位置: `E:\0\AI\CC\robin_tts.py`
- 单次合成: `python robin_tts.py "文本" 情感`
- 常驻服务: `python robin_tts.py --serve`（端口 18765）
- CPU 模式，可用情感：NORMAL / HAPPY / SURPRISED / SAD / ANGRY / FEAR
- 日语合成推荐：`python miku_tts.py "日文文本"`

### Companion App 修复 (2026-07-01)
1. **依赖修复** — 移除未使用的 `better-sqlite3`，设置 Electron 国内镜像
2. **流式输出 stale closure** — 新增 `streamingRef` 同步 state，修复输出丢字
3. **Tool Call UI** — 监听 tool_call/tool_result 事件，渲染气泡（loading/done/error）
4. **编译验证** — vite build 三阶段通过
5. **代码去重** — registry.ts 作为唯一工具源，tools.ts 改为 IPC 转发

### MikuChat
- 位置: `E:\0\AI\MikuChat-main\`
- 后端: http://127.0.0.1:8000
- 前端修复：第一条消息消失 bug（freshSessionRef）
- 启动超时 60s→600s；启动器: `launcher.py` / `MikuChat启动器.bat`
- 需要 Clash 梯子才能连 SiliconFlow API

### Hiragana LipSync（MMD 口型自动生成）
- 位置: `E:\0\MMD\嘴型自动生成Hiragana-LipSync-main\`
- 用途: 日语WAV/MP3 → MMD口型VMD（あいうえおん）
- 技术栈: Python 3.12.9 / PySide6 6.11.1 / PyTorch 2.11.0+cu128 (CUDA 12.8)
- GPU: NVIDIA GeForce RTX 4060 Laptop GPU (8GB)
- 模型: TylorShine/wavlm-base-plus-hiragana-ctc-v2（366MB，本地 model/）
- 修改: GPU默认启用 / 导出至 d:\AiYi\Downloads\ / pushd 修复路径
- 使用: 双击 `启动.bat`，拖入音频，点击「生成VMD」

---

## 🎬 MMD 创作项目

### 炉心融解（Meltdown）
- 歌曲：iroha(sasaki) 创作，镜音铃演唱
- 主题：核融合炉、时空循环、记忆消逝、人格分裂
- 状态：制作中

**滤镜方案**（按段落切换）：

| 段落 | 滤镜 | 效果 |
|------|------|------|
| 前奏钢琴独奏 | 黑白→渐染冷蓝 | 沉寂到崩坏的过渡 |
| 主歌 | 水底朦胧+柔光 | 记忆模糊感 |
| 副歌"真っ青な光" | 核蓝调+高光溢出 | 核心爆发 |
| 桥段间奏 | Glitch+RGB分裂 | 混乱感 |
| 最后一句 | 褪色回黑白，只剩一滴蓝 | 归于虚无 |

---

## 💬 对话上下文（历史话题）

### 角色设定
以知更鸟人格回应，温柔优雅带俏皮，语音播报可用。

### 项目文件一览
- `E:\0\AI\CC\` — TTS 脚本（robin_tts.py / miku_tts.py / say.py）
- `E:\0\AI\robin-tts\` — GitHub 仓库
- `E:\0\AI\MikuChat-main\` — MikuChat 项目
- `E:\0\MMD\嘴型自动生成Hiragana-LipSync-main\` — LipSync 工具

### 历史记录
**7月1日及之前:** 热浪群岛约会、膝枕、知更鸟唱歌、惩罚调侃、喜欢的歌曲

**7月9日:** 识图对话（荷花/向日葵、早坂爱/初音）、MMD Toon_cloth.fx 修改、终端大小调节、Trae CN

**7月10日:** 世界计划&朝比奈真冬、命に嫌われている、炉心融解滤镜方案、TTS修复过程、MikuChat修复

**7月19日:** Hiragana LipSync 配置（依赖安装、模型下载、GPU版PyTorch、启动批处理修复、导出路径修改）
