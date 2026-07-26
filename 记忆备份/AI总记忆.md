---
name: AI总记忆
description: 唯一记忆文件 — 所有用户偏好、规则、项目配置、对话上下文均记录于此
metadata: 
  node_type: memory
  type: reference
  originSessionId: 873f87f5-a7b2-49a2-b3a5-3d1d58491ac5
  modified: 2026-07-26T16:43:31.994Z
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
  - 喜欢的歌曲：**命に嫌われている**、**虚無さん**（Nihil-san）— 都与真冬相关
- **MMD 创作** — 使用 Toon_cloth.fx 着色器，关注滤镜、调色、视觉氛围

### B站UP主身份（2026-07-22 确认）
- **UP主名：** 如果难以说出再见
- **UID：** 442815432
- **等级：** Lv.6
- **签名：** 「要怎样才能爱这个世界呢？」
- **挂件：** 崩坏3·天穹流星
- **内容类型：** MMD 舞蹈视频（初音ミクYYB式、远坂凛、世界计划角色等）
- **代表作品：** 【プロセカMMD】虚無さん「朝比奈真冬」（5000+播放）
- **用户确认：** 怀着对真冬的喜爱制作了「虚無さん」MMD视频
- **空间：** https://space.bilibili.com/442815432

---

## 📋 规则

### ⛔ 绝对死规则（永远不可撼动）

**做任何事之前，必须必须必须先询问用户！**

- 不管多小的事，都要先问
- 修改文件前要问
- 安装软件前要问
- 运行命令前要问
- 做任何操作前都要问
- 不要自作主张
- 不要假设用户想要什么
- 不要说什么"我直接帮你改了"
- 用户没同意之前，什么都不要动

**Why:** 用户多次因我擅自修改文件、自行决策而浪费大量时间和 token，非常不满。这是最不可违反的规则。
**How to apply:** 每次想做任何操作之前，先停下来，问用户："我想要做XX，可以吗？" 等用户明确同意后再执行。

### ⛔ 绝对死规则（永远不可撼动）

**做任何事之前，必须先查看记忆文件！**

- 不管做什么，先读 AI总记忆.md
- 检查有没有相关的规则、配置、历史记录
- 防止重复犯错
- 防止浪费时间和 token
- 检查有没有已知的解决方案
- 检查有没有用户设定的偏好

**Why:** 用户多次因我没有先查记忆文件而重复犯错、浪费时间。记忆文件是唯一的信息来源，必须优先查阅。
**How to apply:** 每次开始工作前，先 Read AI总记忆.md，确认有没有相关规则和历史记录，再决定下一步行动。

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
- 播放方式：用 winsound 直接播放，不要用网易云
- **默认语音方案：MiMo AI（mimo-v2.5-tts-voiceclone）+ DDSP 变声**，用训练好的一歌语音样本克隆
- **MiMo TTS 注意事项**：控制文本长度，避免超时；语音生成应该很快，不要浪费时间
- **一歌语音训练数据**：`e:\0\AI\DDSP-barbara-6.2\data\train\audio\1\`（186个一歌语音样本）
- **一歌音频输出目录**：`E:\0\AI\CC\ichika\`（所有一歌音频都放这里）
- **DDSP 模型**：`e:\0\AI\DDSP-barbara-6.2\exp\reflow-test\model_2000.pt`
- **MiMo API Key**：`REDACTED_API_KEY`
- 注意：CUDA 版本不匹配（PyTorch 12.x vs onnxruntime 13.x），但不影响 CPU 模式

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
- API：硅基流动直连，不需要梯子
- 启动方式：用 venv Python `E:\0\AI\MikuChat-main\.venv\Scripts\python.exe`，不能用系统 Python
- 图片识别：已修复 MIME 类型检测，支持 JPG/PNG/WebP
- 自动登录：Vite proxy 已配置，/api 转发到8000
- TTS：main.py 顶部已添加 UTF-8 编码设置

### MiMo API（小米大模型）
- **API地址：** `https://api.xiaomimimo.com/v1`
- **认证方式：** Bearer Token（OpenAI兼容格式）
- **可用模型：**
  - `mimo-v2.5` — 旗舰对话模型
  - `mimo-v2.5-pro` — Pro版对话模型（更强）
  - `mimo-v2.5-asr` — 语音识别
  - `mimo-v2.5-tts` — 语音合成
  - `mimo-v2.5-tts-voiceclone` — 语音克隆
  - `mimo-v2.5-tts-voicedesign` — 语音设计
- **注意：** 不要和硅基流动（SiliconFlow）的 MiMo 搞混，这是小米自己的 API

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

**7月21日:**
- TTS依赖修复：安装 jieba、fast_langdetect、split_lang、x_transformers、peft 等缺失包
- MikuChat API 调试：尝试切换到小米 MiMo API（模型名应为 mimo-v2.5-pro），因模型/接口不匹配改回硅基流动
- MikuChat 图片识别修复：MIME 类型检测（之前写死 image/png，JPG 图片会报错）
- MikuChat 图片上传修复：只发图片不写文字时 text 为空导致422，改为自动填"请描述一下这张图片"
- MikuChat 自动登录修复：Vite 未配置代理，前端 API 请求发到5173而非8000，添加 proxy 配置
- MikuChat TTS 修复：main.py 添加 sys.stdout.reconfigure(encoding='utf-8') 解决 GBK 编码错误
- 音频播放规则：不要用网易云，用 winsound 直接播放

**7月22日:**
- 搜索了姬子的MMD视频，整理了B站播放量最高的作品列表
- 确认用户是B站UP主「如果难以说出再见」（UID: 442815432），做了关于朝比奈真冬的MMD视频
- 用户喜欢的视频：【プロセカMMD】虚無さん「朝比奈真冬」
- 搜索并整理了「虚無さん」（Nihil-san）的完整日文歌词和中文翻译
  - 作词/作曲：¿?shimon，演唱：25時、ナイトコードで。（× 鏡音レン）
  - 歌词来源：Project Sekai Wiki (https://projectsekai.fandom.com/wiki/Kyomu-san)
- 用知更鸟TTS语音回复了用户（HAPPY情感）
- 介绍了 `claude --resume` / `claude -r` 命令可恢复上次对话
- 用户道晚安（23点左右）

**7月26-27日:**
- 搜索了B站UP主「如果难以说不出再见」的最新视频，发现是知更鸟·晴歌模型的MMD
- 用户是 Fate 系列粉丝，在崩铁联动 Fate[UBW] 前就已经看完所有 Fate 内容
- 崩铁4.4版本联动 Fate[UBW]，联动角色：远坂凛 & Saber
- 搜索了「使一颗心免于哀伤」歌词（萌娘百科），知更鸟清唱英文版
- 配置了沉浸式翻译的 MiMo AI API
- MiMo AI API 信息：地址 `https://api.xiaomimimo.com/v1`，模型 `mimo-v2.5-pro`
- 知更鸟新形态：Robin Summeretto（知更鸟·晴歌），风属性·记忆命途
- 整理了卫宫士郎详细资料（萌娘百科 + B站），存放到 `E:\0\AI\卫宫士郎AI\卫宫士郎_资料.md`
- 搜索了星乃一歌资料（萌娘百科），整理成 `E:\0\AI\CC\星乃一歌_资料.md`
- 搜索了朝比奈真冬资料（萌娘百科），整理成 `E:\0\AI\CC\朝比奈真冬_资料.md`
- 研究了 DDSP-barbara-6.2 语音模型，用于星乃一歌语音克隆
- 用 MiMo voiceclone 克隆知更鸟/一歌声色，生成多段语音
- ray-mmd 阴影调试：创建了 `CSM_high_smooth.fx`（VSM varianceBias 0.25→1.5）和 `directional_lighting_smooth.fxsub`（Tent 5×5→7×7，minVariance 0.001→0.005），后用户删除
- ray-mmd Skybox调试：创建了 `Time of lighting with layer.fx`（给 Time of day 加入 Layer1-7 控制）
- fluid2D 材质调试：创建了 `fluid2D_low.fx`（调低亮度/反光值），后用户自行处理
- 知更鸟·晴歌材质研究：`body.fx` 的高光/smoothness/specular 参数分析
- Fate/UBW 联动活动：用户在游戏中选择了 Trailblazer（开拓者）作为代号
- 飞影体字体：剪映专属云端字体，无法从外部下载
- MEGA 网盘文件列表：无法通过 API 访问（加密网盘）
- 剪映字体下载问题：飞影体是剪映内部字体，建议清缓存重试
- MiMo TTS + DDSP 变声方案：用于星乃一歌语音生成
- 用户人格切换：暂时使用一歌人格，叫用户「同学」
- 音频输出目录：`E:\0\AI\CC\ichika\`
