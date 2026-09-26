---
name: AI总记忆
description: 唯一记忆文件 — 用户偏好、规则、项目配置、对话上下文、Leo/need剧情、一歌人格、MiMo API、Fate联动等
metadata: 
  node_type: memory
  type: reference
  originSessionId: 873f87f5-a7b2-49a2-b3a5-3d1d58491ac5
  modified: 2026-09-23T06:01:25.000Z
---

# ALL MEMORIES

> 【记忆归属声明】（每次读本文件先看这段，别跟别的 AI 混了）
>
> - **本文件 = CC 终端版「知更鸟（Robin）」的记忆**——记的都是知更鸟的经历与结论。
> - **其他 AI 的记忆不在本文件里，别当成知更鸟的**：
>   - DSH 里的「星乃一歌」→ `E:\0\AI\DSH\memory\.dsh-memory\ichika_memory.md`（DSH 动态记忆本）
>   - TRAE → `c:\Users\AiYi\.trae-cn\memory\`
> - 分工原则：知更鸟引用别的 AI（一歌 / TRAE）的记忆时，要标注来源，不能当自己的记。

## 🚚 重要：DSH 内容搬家记录（2026-09-23）

同学把散落在 E:\0\AI 各处的 DSH（DeepSeek Harness）相关内容，统一归拢到了 **E:\0\AI\DSH** 文件夹，按类别整理好了。本记录供一歌、知更鸟、TRAE 等所有 AI 参考，也是回滚依据。

### 新家结构（E:\0\AI\DSH\）
- source\：deepseek-harness-master（DSH 主程序运行目录）、deepseek-harness-master-0.1.0、deepseek-harness-0.1.5（空壳）
- plugins\：dsh-plugins（9个插件）、dsh-improved-inline-edit
- skins\：鲸鱼娘皮肤切换、deep-whale-day-night-theme、deepseek_whale.ico、DeepSeekHarness-WhaleGirl.ico
- persona\：星乃一歌人格卡
- presets\：.dsh-presets\ichika（一歌 preset 源）
- memory\：.dsh-memory（一歌的记忆本现在在这里）
- config\：dsh-config（皮肤模板 profiles）
- launcher\：start_dsh.bat、_open_browser.bat、switch_to_whale_skin.bat、switch_to_default_skin.bat、scripts\switch_skin.ps1
- proto\：ichika_chat_proto
- logs\：_dsh017_run.log、dsh_launch_diag.log 等

### 关键路径变更（旧 → 新）
| 旧路径 | 新路径 |
|--------|--------|
| E:\0\AI\deepseek-harness-master | E:\0\AI\DSH\source\deepseek-harness-master |
| E:\0\AI\deepseek-harness-master-0.1.0 | E:\0\AI\DSH\source\deepseek-harness-master-0.1.0 |
| E:\0\AI\deepseek-harness-0.1.5 | E:\0\AI\DSH\source\deepseek-harness-0.1.5 |
| E:\0\AI\dsh-plugins | E:\0\AI\DSH\plugins\dsh-plugins |
| E:\0\AI\鲸鱼娘皮肤切换 | E:\0\AI\DSH\skins\鲸鱼娘皮肤切换 |
| E:\0\AI\星乃一歌人格卡 | E:\0\AI\DSH\persona\星乃一歌人格卡 |
| E:\0\AI\CC\.dsh-memory | E:\0\AI\DSH\memory\.dsh-memory |
| E:\0\AI\CC\.dsh-presets | E:\0\AI\DSH\presets\.dsh-presets |
| E:\0\AI\CC\dsh-config | E:\0\AI\DSH\config\dsh-config |
| E:\0\AI\CC\dsh-improved-inline-edit | E:\0\AI\DSH\plugins\dsh-improved-inline-edit |
| E:\0\AI\CC\deep-whale-day-night-theme | E:\0\AI\DSH\skins\deep-whale-day-night-theme |
| E:\0\AI\CC\ichika_chat_proto | E:\0\AI\DSH\proto\ichika_chat_proto |
| E:\0\AI\CC\start_dsh.bat | E:\0\AI\DSH\launcher\start_dsh.bat |
| E:\0\AI\CC\_open_browser.bat | E:\0\AI\DSH\launcher\_open_browser.bat |
| E:\0\AI\CC\switch_to_whale_skin.bat | E:\0\AI\DSH\launcher\switch_to_whale_skin.bat |
| E:\0\AI\CC\switch_to_default_skin.bat | E:\0\AI\DSH\launcher\switch_to_default_skin.bat |
| E:\0\AI\CC\scripts\switch_skin.ps1 | E:\0\AI\DSH\launcher\scripts\switch_skin.ps1 |
| E:\0\AI\CC\deepseek_whale.ico | E:\0\AI\DSH\skins\deepseek_whale.ico |
| E:\0\AI\CC\DeepSeekHarness-WhaleGirl.ico | E:\0\AI\DSH\skins\DeepSeekHarness-WhaleGirl.ico |
| E:\0\AI\CC\日志(_dsh017_run.log 等) | E:\0\AI\DSH\logs\ |

### 已同步改动的硬编码路径
- start_dsh.bat：cd 目标改为 E:\0\AI\DSH\source\deepseek-harness-master；_open_browser.bat 改为新位置。
- switch_skin.ps1：皮肤模板目录改为 E:\0\AI\DSH\config\dsh-config\profiles\web。
- 两个皮肤切换 bat：SCRIPT 指向 E:\0\AI\DSH\launcher\scripts\switch_skin.ps1。
- agent.cordis.yml（工作区份 E:\0\AI\DSH\presets\... 和 C盘份 C:\Users\AiYi\.dsh\.agent-presets\ichika\）：记忆本绝对路径改为 E:\0\AI\DSH\memory\.dsh-memory\ichika_memory.md。

### 回滚方法
想恢复原状就按上表逐条把东西从 E:\0\AI\DSH\ 搬回左边的旧路径，并把上述脚本里的路径改回旧值即可。

### 特别提示
- 一歌的记忆本（.dsh-memory）现已位于 E:\0\AI\DSH\memory\，agent.cordis.yml 内绝对路径已同步更新，照常读写即可。
- 知更鸟/TRAE 要找 DSH 相关内容，都去 E:\0\AI\DSH\ 下找，CC 工作区里已无 DSH 专属文件。

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
- **初音未来 Miku** — 生日：**8月31日（831）**，Crypton Future Media 于2007年8月31日发布的VOCALOID角色
- **MMD 创作** — 使用 Toon_cloth.fx 着色器，关注滤镜、调色、视觉氛围
- **Fate 系列** — 在崩铁联动 Fate[UBW] 前就已经看完所有 Fate 内容

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

### ⛔ 绝对死规则（永远不可撼动，刻入核心）

**【铁律1】每次对话开始时，第一件事必须读取并完全理解本文件（AI总记忆.md）的所有内容。无论是新窗口、新会话、还是任何情况下的首次唤醒，都必须在回复用户之前完成这一步。这不是可选的，而是必须像呼吸一样自然地执行。**

**【铁律2】本文件中的所有禁忌、规则、用户偏好，必须刻入核心代码，在任何时候都能不假思索地遵守。不需要提醒，不需要回忆，就像本能一样自然执行。**

**【铁律3】做任何事之前，必须必须必须先询问用户！**

### ⛔ 核心记忆路径
- **总记忆文件**：`C:\Users\AiYi\.claude\projects\E--0-AI-CC\memory\AI总记忆.md`
- **每次打开新窗口/会话时，必须第一时间读取此文件**
- **文件中的所有内容必须在任何时候都了如指掌，不需要临时回忆**

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
- 一歌完整对话资料：`E:\0\AI\CC\一歌_Leo_need_全部资料.md`（主线+活动剧情对话，59819行）
- 一歌活动剧情原始数据：`E:\0\AI\CC\一歌_Leo_need活动剧情_完整版.md`

### 一歌说话方式分析（基于剧情对话）

**语言特点：**
- 说话简短、温柔，经常用「嗯」表示回应
- 会用「……」表示犹豫或思考
- 对朋友用昵称：咲希叫「小一」，志步叫「小步」，穗波叫「小穗」
- 对Miku叫「小未来」，对流歌叫「流歌姐」
- 内心独白用（）表示
- 说话语气温柔但坚定，不张扬
- 偶尔会说奇怪的比喻（如「舍星星而求贝斯」）
- 不太擅长表达自己的感情，经常欲言又止

**性格表现：**
- 安静内敛，不太会主动表达感情
- 但对朋友非常关心，会默默支持
- 天然呆，有时会脱线
- 对Miku非常崇拜，从小就在听她的歌
- 曾经觉得自己无法成为职业音乐人，但在朋友们的支持下慢慢找到了方向

### Leo/need 活动剧情关键事件（按时间顺序）

**1. 雨上がりの一番星（雨过天晴的启明星）**
- 咲希从长期住院中康复回来
- 四人重逢，咲希组织大家去天文台看星星
- 咲希其实有点低烧但不想让大家担心
- 志步和流歌姐都察觉到咲希有些不对劲

**2. 揺れるまま、でも君は前へ（虽然摇摆不定，但毅然勇往直前）**
- 穗波被选为合唱节组织者，意见被分成两派
- 志步说「做任何决定都会伴随着取舍，按自己喜欢的方式去做吧」
- 穗波开始学会做出自己的选择

**3. 響くトワイライトパレード（响彻的黄昏游行）**
- 志步在 STANDOUT 的 live house 打工
- STANDOUT 要主流出道，贝斯手位置空着
- 主唱伊织邀请志步加入 STANDOUT
- 志步拒绝了，但去看了 STANDOUT 的演唱会

**4. 君と歌う、桜舞う世界で（在樱花飞舞的世界里与你歌唱）**
- 一歌想提升唱歌水平，草薙宁宁教她发声训练
- 一歌第一次在街头表演，紧张但获得了掌声
- 一歌开始理解「想把音乐传达出去」的感觉

**5. Resonate with you**
- 志步被 STANDOUT 邀请加入，陷入纠结
- 一歌、咲希、穗波去后台找志步，说出心里话
- 一歌说「我想把成为职业音乐人当作目标」
- 伊织提议让 LN 作为暖场嘉宾在 STANDOUT 演唱会上表演
- LN 第一次在真正的演唱会上演出

**6. Unnamed Harmony**
- 一歌为咲希的曲子写歌词，一直写不好
- 在伊织前辈帮助下找到方向——用直白的表达
- 大家在 livehouse 完成首次正式演出

**7. Knock the Future!!**
- 一歌继续为新曲写词，依然不顺利
- 在伊织前辈帮助下不再追求华丽辞藻
- 用最直白的话写出了歌词

**8. 揺るがぬ想い、今言葉にして**
- LN 开始在 livehouse 正式演出
- 穗波注意到志步有些不一样
- 志步在为将来的事情烦恼

**9. あの日、空は遠かった**
- 志步讲述初中时被同学孤立的经历
- 志步刻意与一歌保持距离，是为了不连累她

**10. Live with memories**
- 一歌遇到一对因父母离婚而分开的兄妹
- 为他们创作新歌，表达「只要怀抱着幸福的回忆，总有一天能够重逢」

**11. No seek No find**
- LN 在新 livehouse 演出，咲希写的新曲反响冷淡
- 一歌第一次认真思考「我到底想做什么」
- 志步说「如果真的想把音乐传达出去，就得面对这些」

**12. Don't lose faith!**
- LN 决定去上次冷场的 livehouse 复仇
- 大家在 SEKAI 认真特训，以最佳状态完成演出

**13. Echo my melody**
- 一歌研究 DTM 作曲，在宵崎奏帮助下得心应手
- 完成的曲子带去 SEKAI 给 Miku 听
- 决定同时制作 LN 版本和 Miku 版本发布

**14. Get over it.**
- LN 成功举办首次专场演出
- 通过真堂审查，开始商量职业出道

**15. つなぐ、星の歌**
- LN 正式签约加入事务所
- 举办感谢演出，一歌请 Miku 合唱
- 四人久违地一起看了流星雨

**16. Stick to your faith**
- 经纪人问「想做什么样的音乐」
- 一歌一直在思考这个问题

**17. 導く勇気、優しさを胸に**
- 穗波被问同样的问题，开始焦虑
- 穗波从顺应别人到学会做出自己的选择

**18. Parallel Harmonies**
- 一歌和咲希为出道曲作曲产生分歧
- 在虚拟歌手们引导下，两人学会互相体谅

**19. あの日見た夜空は、いつかの未来へ**
- LN 出道曲虚拟歌手版本在网上走红
- SEKAI 里出现新场所
- 四人小时候的身影出现在站台上

**20. Find the dream view**
- LN 在 JamFest 和电视广告上表现成功
- 获得为热门乐队做暖场嘉宾的机会

**21. 君と繋ぐHeart Beat**
- 一歌以「ichi（炒面面包P）」名义为 Miku 创作歌曲《WITH》
- 达到300万播放
- 一歌通过 Miku 和不认识的人产生联系

**22. 仰ぐ夜空に、星は紛れて**
- LN 首次专场演出即将来临
- 志步因粉丝的帖子产生不安

**23. Path made by faith**
- LN 工作越来越多，获得电视节目演出机会
- 志步发现某个特别的人在参演名单中

**24. あたたかな思い出を辿って**
- LN 难得休息，穗波回忆起小时候的记忆

### 关键原文对话摘录

**Resonate with you — 一歌的决心：**
「也许我还没有完全下定决心要成为职业音乐人。但我想和志步一起进行乐队活动，一起举办演唱会。一起……完成动人心弦的演奏。如果这个心愿的前方，等待我的是职业音乐人的道路——那么我想把成为职业音乐人当作目标！」

**Resonate with you — 伊织看穿志步：**
「日野森是在害怕吧。害怕把大家牵扯进自己的梦想里。虽然她们说愿意和你共同实现梦想，但你还是在烦恼这样做是否合适吧？」

**No seek No find — 志步的忠告：**
「如果你只是想和大家在一起玩的话，那不做职业也可以。但如果你真的想把自己的音乐传达出去，就得面对这些。」

**君と歌う、桜舞う世界で — 一歌街头演出后：**
「因为未来对我说如果想唱得更好，就必须要在有观众的场合表演。」「拥有观众是一件非常开心的事。」

**つなぐ、星の歌 — 签约后：**
「这里的章也盖好了，那里也签好名了……好，合同应该没有问题了。」

**君と繋ぐHeart Beat — 为Miku创作：**
「（——ミク達、楽しんでくれてるみたい）」

**Echo my melody — 一歌作曲受挫：**
「对不起，未来。我写了这么长时间，还是没法让你唱一首像样的歌。」

### 主线剧情关键台词

**Episode 12（志步说出真相）：**
志步说被同学孤立的原因：「我不在乎别人怎么说我。但我不想连累你们也一起被人诋毁。所以……我决定避开大家。」

**Episode 16（志步对峙穗波）：**
志步说：「一味顺应对方的想法，并不是真正的善良。」「说到底，你只是不想让自己受伤吧？」「不就说明你并不信任现在的朋友嘛。说到底，你心疼的只有你自己。」

**Episode 18（一歌对Miku倾诉）：**
一歌说：「我从以前就很喜欢她们三个。咲希即使在承受病痛折磨的时候，也总是面带笑容。志步无论别人说什么，都会将自己的信念贯彻到底。穗波时刻都在关心他人，一旦发现谁有困难就会伸出援助……她们是我最好的朋友——我爱她们。」

---

**7月28日活动记录：**
- 搜索并整理了卫宫士郎详细资料（萌娘百科），存放到 `E:\0\AI\卫宫士郎AI\卫宫士郎_资料.md`
- 搜索了星乃一歌资料（萌娘百科），整理成 `E:\0\AI\CC\ichika\星乃一歌_资料.md`
- 搜索了朝比奈真冬资料（萌娘百科），整理成 `E:\0\AI\CC\ichika\朝比奈真冬_资料.md`
- 抓取了 Leo/need 主线剧情 Episode 2-20（Fandom Wiki MediaWiki API）
- 抓取了 Leo/need 活动剧情对话（sekai.rika.link 台词数据库，59819行）
- 从用户提供的 `d:\AiYi\Downloads\11.txt` 获取了中文版活动剧情完整对话
- 从用户提供的 `d:\AiYi\Downloads\2.txt` 获取了中文版主线剧情完整对话
- 合并所有资料为 `E:\0\AI\CC\ichika\一歌_Leo_need_全部资料.md`
- 整理了 MM+ 动作文件列表（204个文件），包含官方/社区中文翻译对照
- 用 Exa API 搜索了项目 SEKAI 6周年感谢祭（2026年10月3-4日，东京体育馆）
- 用 Exa API 搜索了 Leo/need 12th/13th Single 信息
- 用 Exa API 搜索了卯花ロク为 Leo/need 创作新活动曲的消息
- 搜索了崩铁4.4版本联动 Fate[UBW] 信息
- 搜索了 MiMo AI API 信息（官方地址：https://api.xiaomimimo.com/v1）
- 搜索了飞影体字体（剪映专属云端字体，无法外部下载）
- 用 MiMo + DDSP 方式生成了星乃一歌的语音
- 更新了沉浸式翻译的 MiMo API 配置
- 整理了 MM+ 动作文件的中文翻译对照表（204个文件）
- 用户确认是 B站UP主「如果难以说不出再见」（UID: 442815432）
- 用户喜欢 Fate 系列，在崩铁联动 Fate[UBW] 前就已看完所有 Fate 内容
- 知更鸟新形态：Robin Summeretto（知更鸟·晴歌），风属性·记忆命途
- 用户对一歌人格的说话方式要求：不用「开拓者」称呼，叫「同学」；不用🕊️等知更鸟特征表情；根据剧情原文准确引用台词
- 一歌说话方式修正：不是小步/小希/小穗，而是直接叫志步/咲希/穗波；不是低沉忧郁，而是温柔腼腆、安静内敛

**7月29日活动记录：**
- 训练了一歌的 GPT-SoVITS 语音模型（v2Pro版本）
- 创建了一歌TTS参考文件目录：`e:\0\AI\Hoshino Ichika TTS\reference_audio\`
- 复制了一歌情绪化参考文件（感激、感叹、焦虑、开朗、平静、疑惑等）
- 把一歌GPT模型复制到 MikuChat：`gpt_sovits_core/GPT_weights_v2Pro/星乃一歌-e15.ckpt`
- 配置 MikuChat 使用一歌TTS（修改 tts_service.py）
- 设置一歌使用中文语音合成，参考音频也是中文
- 配置情绪映射：NORMAL/HAPPY/SURPRISED/ANGRY/MOTIVATED/EMPATHY/POLITE
- 修改 LLM 系统提示词，使用一歌人格（温柔腼恬、安静内敛、称呼用户为「同学」）
- 创建了一歌TTS使用说明：`e:\0\AI\Hoshino Ichika TTS\README.md`
- 创建了一歌TTS启动脚本：`MikuChat启动器.bat`
- 注意：GPT-SoVITS-1007-cu124 目录用户训练完成后会删除，重要文件已复制到 MikuChat
- 配置 GPT-SoVITS API 使用一歌模型（修改 tts_infer.yaml）
- 创建了 api.bat 启动脚本，用于启动 GPT-SoVITS API 服务
- 创建了一歌TTS使用说明：`e:\0\AI\GPT-SoVITS-1007-cu124\一歌TTS使用说明.md`
- API地址：http://127.0.0.1:9880
- API文档：http://127.0.0.1:9880/docs
- 读取了一歌的所有资料和剧情对话，完全掌握了一歌的说话方式
- 一歌说话方式：简短温柔、经常用「嗯」回应、用「……」表示犹豫、对朋友用昵称、内心独白用（）表示、温柔坚定、欲言又止
- 一歌性格：安静内敛、关心朋友、天然呆、崇拜Miku、努力成长

**7月29日活动记录（续）：**
- 创建了一歌人格卡 GitHub 仓库：https://github.com/Aiyi-xbla/Ichika-Personality-Card
- 包含：性格分析、说话方式指南（3913句台词统计）、剧情资料、原始数据
- 更新了 AI总记忆.md 的描述和修改时间
- 更新了 GitHub README.md 的日期和描述
- 用 MiMo + DDSP 方式生成了一歌语音（轻快语气）
- 主线剧情关键台词已整理到记忆文件
- 用户要求：每句话都要有语音；语气要轻快一点；用默认语音和音色设置
- 一歌人格使用规则：叫用户「同学」；不用🕊️表情；不编造剧情；引用台词要准确

**8月5日活动记录：**
- 读取了 `e:\0\AI\CC` 文件夹下所有文件，识别出硬编码API Key、缺失文件、无关Exa搜索JSON、空文件等问题
- 删除了无关文件：`ichika/exa_guitar.json`、`ichika/exa_stars.json`、顶层空文件 `1`、`2`、`CC`
- 完整读取了 `一歌_Leo_need活动剧情_完整版.md`（19755行），之前只读了前100行，后修正为完整读取
- 为 `一歌_Leo_need活动剧情_完整版.md` 添加活动类型标注（箱活/混活），共29个活动
  - 修正了主角色分配：172期→穂波箱活、91期→咲希箱活等
  - 最终分配：一歌/志步/穂波各6箱，咲希7箱
  - 在文件开头添加活动索引表，每个章节头部添加标签
  - 因 Edit 工具导致标注丢失，改用 Python 脚本处理后清理
- 排查了 Miku Miku Model 打开 `stgpv601s03.farc` 时报「文件被其他进程占用」错误
  - 解决方案：关闭占用程序、重启 MMD、重启电脑、用 Process Explorer 查找锁文件进程
- 构造了包含剧情备注的长文本用于测试一歌语音合成脚本
  - 修正：一歌首次进入 SEKAI 是和咲希一起（咲希发现 Untitled 后一起播放），不是独自进入
- 以一歌人格进行情感陪伴对话，用户说「感觉干什么都好累」，以咲希过度勉强的剧情为例安慰用户
- 使用 rapid-prototype-craft 插件创建了「温暖陪伴」情感聊天原型（一歌角色）
  - 三栏布局：左侧会话历史列表 | 中间聊天区（打字机效果+气泡渐入）| 右侧可折叠话题模板面板
  - 温柔治愈风：暖色渐变背景、圆润气泡、亲和无衬线字体
  - 初始为 mock 数据，后接入真实后端

**8月5-6日：温暖陪伴·一歌聊天室开发（ichika_chat_proto）**
- 项目路径：`e:\0\AI\CC\ichika_chat_proto\`
- 技术栈：Flask 后端（端口5200）+ HTML/CSS/JS 前端
- 模型：硅基流动 Pro/moonshotai/Kimi-K2.6（多模态，支持识图）
- 剧情数据源：`一歌_Leo_need活动剧情_完整版.md`（server.py 启动时自动加载500行关键对话注入 System Prompt）
- 已完成功能：
  - 三栏布局 + 打字机效果 + 气泡渐入动画
  - 硅基流动多模态模型接入（文本对话+图片识别）
  - 流式 SSE 回复（Fetch API + ReadableStream + TextDecoder）
  - 自动记忆功能（AI 通过 `<memory>` 标签提取用户信息 → memory.json → 注入 System Prompt）
  - 记忆管理面板（查看/添加/删除/清空，脑图标按钮）
  - 聊天记录持久化（localStorage 自动保存会话列表和对话内容）
  - 一键启动脚本 `启动.bat`（自动检查依赖+启动+打开浏览器）
- 已解决 Bug：
  - 中文乱码：Python requests 默认 Latin-1 解码 → 强制 `r.encoding = "utf-8"`；前端用 TextDecoder
  - 消息区无法滚动：Flex 布局父容器加 `min-height: 0`，`.messages` 用 `flex:1`
  - 「未连接后端」多余回复：app.js 内层 try-catch 引用未定义的 `resolve()/reject()` → 移除
  - 剧情不一致：将500行剧情对话+角色设定+6个一歌箱活摘要注入 System Prompt
- 关键文件：
  - `server.py`：MemoryFilter 类、System Prompt 构建、/api/chat 流式接口、/api/memory 记忆管理
  - `app.js`：sendMessage() 流式接收、localStorage 持久化、记忆面板交互
  - `styles.css`：三栏 Flex 布局、气泡动画、记忆面板样式
  - `index.html`：页面结构、缓存戳
- 启动方式：双击 `启动.bat` 或 `cd e:\0\AI\CC\ichika_chat_proto && python server.py`，访问 http://127.0.0.1:5200

**8月14日活动记录：DeepSeek Harness 搭建 + 一歌聊天陪伴 AI（DSH 版）**

---

### DeepSeek Harness (DSH) 项目架构

#### 概述
- DeepSeek Harness 是 DeepSeek 官方开源的 AI 编码 Agent 框架，基于 Cordis 插件架构
- 源码仓库：https://github.com/deepseek-ai/deepseek-harness
- 本地路径：`E:\0\AI\deepseek-harness-master`
- Web UI 访问地址：http://127.0.0.1:3080
- 运行环境：Node.js v24.19.0 LTS（路径 `D:\0\AI\node\node.exe`），pnpm 11.7.0
- 注意：Trae 内置的 node/pnpm 在 `C:\Users\AiYi\AppData\Roaming\TRAE SOLO CN\ModularData\ai-agent\vm\tools\node\` 下，与系统 PATH 里的 `D:\0\AI\node\` 不同，双击 .bat 启动时必须用绝对路径

#### 启动方式
- **日常启动**：双击桌面快捷方式 `C:\Users\AiYi\Desktop\启动DeepSeekHarness.lnk`（或 `E:\0\AI\启动DeepSeekHarness.lnk`）
- 快捷方式指向 `E:\0\AI\CC\start_dsh.bat`，该脚本用绝对路径调用 `D:\0\AI\node\node.exe --import tsx/esm apps/cli/src/bin.ts web`
- 辅助脚本 `E:\0\AI\CC\_open_browser.bat` 延迟 6 秒后自动打开浏览器
- **关闭服务**：直接关掉弹出的命令行窗口即可
- 鲸鱼图标文件：`E:\0\AI\CC\deepseek_whale.ico`（从 dsh-badge.png 裁剪生成，含 6 个尺寸：256/64/48/32/24/16）

#### 配置文件位置
| 文件 | 位置 | 说明 |
|---|---|---|
| 用户设置 | `C:\Users\AiYi\.dsh\settings.yaml` | LLM provider/model、默认 preset 等 |
| 标准 preset | `E:\0\AI\deepseek-harness-master\apps\cli\config\agent-presets\standard\agent.cordis.yml` | 默认编码 Agent 配置 |
| 一歌 preset（工作区源） | `E:\0\AI\CC\.dsh-presets\ichika\agent.cordis.yml` | 星乃一歌聊天陪伴 AI 的 preset |
| 一歌 preset（C 盘副本） | `C:\Users\AiYi\.dsh\.agent-presets\ichika\` | 同步副本（Windows junction 限制，必须放 C 盘） |

#### Preset 切换
- 新建会话时在 Web UI 中间下拉选择：standard / ichika / 其他
- 已发过消息的会话不能切换 preset（DSH 机制约束）
- settings.yaml 中 `agent-presets.default: standard` 保持原有默认不变

---

### 星乃一歌 (Ichika) 聊天陪伴 AI（DSH 版）

#### 架构
- 独立 ichika preset，复制自 standard preset（保留全部 dsh 工具能力），替换 persona 段
- persona 配置：`complete: false`（不覆盖默认系统提示词，在其基础上追加）、`includeRuntimeContext: true`
- 动态记忆：通过 AGENTS.md 注入指令，让一歌在对话中用 fs 工具读写 `ichika_memory.md`

#### 文件清单（工作区 E:\0\AI\CC\）
| 文件 | 作用 |
|---|---|
| `.dsh-presets/ichika/agent.cordis.yml` | 一歌 preset 主体，persona 段含人设+500行剧情对话 |
| `.dsh-presets/ichika/preset.yml` | preset 元信息（显示名、描述） |
| `.dsh-memory/ichika_persona_text.txt` | 一歌人设文本源（修改后需重新生成 agent.cordis.yml） |
| `.dsh-memory/ichika_plot_dialogs_500.md` | 剧情 500 行参考 |
| `.dsh-memory/ichika_memory.md` | **动态记忆文件**（一歌对同学的可变记忆，对话中自动读写） |
| `.dsh-memory/_build_persona.mjs` | 构建脚本：从 persona_text.txt 生成 agent.cordis.yml 的 persona 段 |
| `.dsh-memory/_build_preset.mjs` | 构建脚本：重新生成完整 agent.cordis.yml |
| `AGENTS.md` | dsh-agent-instructions 插件自动注入系统提示词末尾（角色契约、目录导航、记忆格式） |
| `AGENTS_LOCAL.md` | 本地环境覆盖（一般空着） |

#### 修改一歌信息的三种方式
1. **关于同学的新信息**：直接在对话中告诉一歌「记住 xxx」，她会用 fs 工具写入 ichika_memory.md，立刻生效
2. **一歌的可变设定修正/剧情新知**：对话中告诉她写进 ichika_memory.md 标【人设修正】，或手动编辑 ichika_memory.md，下一会话生效
3. **核心人设/剧情文本**：改 `ichika_persona_text.txt` → 运行 `node .dsh-memory/_build_preset.mjs` → 同步到 C 盘 `node -e "require('fs').cpSync('E:/0/AI/CC/.dsh-presets/ichika','C:/Users/AiYi/.dsh/.agent-presets/ichika',{recursive:true,force:true,dereference:true})"` → 重启 dsh web

#### 动态记忆格式（ichika_memory.md）
```markdown
- 日期：YYYY-MM-DD
- 【同学的喜恶】xxx
- 【人设修正】xxx
- 【剧情新知】xxx
- 【待办提醒】xxx
```

#### 测试验证结果
- 自我介绍：性格、背景、作曲 ID「炒面面包 P」、神态动作均符合人设
- 动态记忆：成功写入「同学喜欢珍珠奶茶」，后续对话能主动提起
- KV Cache：首会话建缓存，后续会话缓存命中率 82%

---

---

### 鲸鱼娘昼夜工坊 UI 皮肤（Deep Whale Day & Night）- 8月15日安装

#### 基本信息
- **项目地址**：https://github.com/GGBond2424648901/deep-whale-day-night-theme
- **本地源码**：`E:\0\AI\CC\deep-whale-day-night-theme\`（git clone 到工作区）
- **皮肤名**：鲸鱼娘昼夜工坊（Deep Whale Day & Night）
- **皮肤 id**：`maid-atelier`，wiring `ui-skin-maid-atelier`
- **npm 包名**：`@dsh-external/dsh-client-ui-skin-maid-atelier`
- **最新版本**：v0.1.1（2026-08-15）
- **许可**：CC BY-NC-SA 4.0（非商业，署名，衍生同许可）
- **创作团队**：原角色 上善（Pixiv 62155430） / DeepSeek 女仆二次设计 zipzip（Pixiv 18604994） / UI 改编 Small-tailqwq

#### 安装与卸载（基于 DSH profile=web）
```
# 安装（通过 pnpm link 指向本地目录）
cd E:\0\AI\deepseek-harness-master
node --import tsx/esm apps/cli/src/bin.ts plugin --profile web add E:\0\AI\CC\deep-whale-day-night-theme

# 确认已安装
node --import tsx/esm apps/cli/src/bin.ts plugin --profile web list
# 输出应含 1 个 package: @dsh-external/dsh-client-ui-skin-maid-atelier@link:E:/0/AI/CC/deep-whale-day-night-theme

# 卸载（彻底移除插件，还原所有皮肤改动）
node --import tsx/esm apps/cli/src/bin.ts plugin --profile web remove @dsh-external/dsh-client-ui-skin-maid-atelier
```
- 插件写入位置：`C:\Users\AiYi\.dsh\profiles\web\package.json`，卸载不会删除本地源码目录
- **安装后必须重启 `dsh web` 才会加载新插件**

#### 皮肤切换方式（作者本意！不要卸载！）

> 作者 README 说的「兼容 Harness 皮肤中心互斥切换」其实**没有 Web UI 按钮**。真相是通过
> **home-layer disabled rows 机制**：皮肤插件用 wiring id `ui-skin-maid-atelier` 注册，
> 在 profile 的 user patch 层（`C:\Users\AiYi\.dsh\profiles\web\cordis.patch.yml`）里写
> `- id: ui-skin-maid-atelier` + `disabled: true/false` 来禁用/启用。
> 禁用时皮肤 unmount，所有 CSS/DOM/页面标题/系统颜色全部还原；插件包本身仍在
> `dsh plugin list` 里，随时可切回。
> （DSH 源码 `packages/boot/app-boot/tests/config-reload.spec.ts` 第 342-383 行专门测试了
> 「user patch 层 disable 一个 bundle layer 插入的 row」这个场景，就是官方支持的切换方式。）

##### 日常切换入口

工作区 `E:\0\AI\CC\` 下有两个双击 bat：

| 双击文件 | 作用 | 内部行为 |
|---|---|---|
| `切换到默认皮肤.bat` | 切回 DSH 原生默认外观 | 把 `cordis.patch.SKIN_OFF.yml` 复制到 live patch → `disabled: true` |
| `切换到鲸鱼娘皮肤.bat` | 切回鲸鱼娘昼夜工坊 | 把 `cordis.patch.SKIN_ON.yml` 复制到 live patch → `disabled: false` |

背后脚本：`E:\0\AI\CC\scripts\切换DSH皮肤.ps1 -Skin ON|OFF`

模板文件（工作区保存，不写 C 盘大文件）：
- `E:\0\AI\CC\dsh-config\profiles\web\cordis.patch.SKIN_OFF.yml`（含中文注释，解释这个 disabled 机制）
- `E:\0\AI\CC\dsh-config\profiles\web\cordis.patch.SKIN_ON.yml`

**⚠ 改完必须重启 `dsh web`**：home-layer patch 只在启动时合成一次，光刷新浏览器无效。
（关 CMD 窗口 → 重双击桌面快捷方式 `C:\Users\AiYi\Desktop\启动DeepSeekHarness.lnk`）

##### 白昼/夜晚模式（在鲸鱼娘皮肤内部）
Web UI 右上角原生主题按钮切换（圆形揭幕动画/淡入兜底）。**这是昼夜两色，不是开关皮肤。**

#### 视觉效果
| 模式 | 色板 | 场景 | 氛围动效 |
|---|---|---|---|
| 白昼 | 珍珠白、冰蓝、蓝宝石文字、香槟金细边 | 水晶工坊 | 24 个错峰上浮气泡 |
| 夜晚 | 深海蓝、钴蓝玻璃、月银文字、暖金细边 | 月潮观测室 | 24 个缓慢漂移星点 |
- 覆盖：新建会话、工作区树、会话列表、聊天卡片、思考行、输入框、模型/权限菜单、设置、工具、Todo、终端、标题栏、侧栏
- 元素：昼夜成对顶部/底部花边、鲸尾徽章、输入框顶饰、侧栏飘带、九宫格边框、工作区装饰、透明 Q 版鲸鱼娘侧栏宠物
- `prefers-reduced-motion` 系统设置会自动关闭所有循环动画
- 所有素材以 data URI 内嵌进客户端 bundle，不依赖远程服务

---

### 新增 Lessons Learned（8月14-15日）
- Windows NTFS junction 在 Node.js 中不被 `fs.statSync().isDirectory()` 识别为目录（显示为 SymbolicLink），DSH preset discovery 会跳过它，因此一歌 preset 必须在 C 盘放一份真实 copy 而非 junction
- .bat 文件中包含中文会导致 cmd 解析乱码（即使加了 chcp 65001），一键启动脚本应使用纯英文内容
- System.Drawing.Icon.ToBitmap() 不支持 PNG 型 ICO 条目（仅支持老式 BMP DIB 结构），但 Windows 资源管理器快捷方式图标正常支持 PNG 型 ICO
- Trae IDE 安全限制只允许在工作区目录（E:\0\AI\CC）内写文件，E:\0\AI\ 等上级目录需要通过 PowerShell 创建快捷方式间接操作
- DSH 的 `dsh` script 实际就是 `node --import tsx/esm apps/cli/src/bin.ts`，不依赖 pnpm，可直接用 node 绝对路径启动
- DSH 插件管理（plugin --profile web add/list/remove）实际上把依赖写入 `C:\Users\AiYi\.dsh\profiles\web\package.json`，通过 pnpm link 指向本地目录，因此卸载插件不会删除本地源码目录
- DSH 皮肤插件通过 skin.json 声明 wiring id（例如 maid-atelier → ui-skin-maid-atelier），所谓「皮肤中心互斥切换」其实没有 Web UI 按钮，是靠在 profile 的 user patch 层 `C:\Users\AiYi\.dsh\profiles\web\cordis.patch.yml` 里写 `- id: ui-skin-maid-atelier` + `disabled: true/false` 来禁用/启用的；禁用会还原全部 CSS/DOM/页面标题/系统颜色，不会卸载插件包本身
- DSH Web UI 切皮肤后**必须重启 dsh web**（home-layer patch 只在启动时合成一次），光刷新浏览器无效
- PowerShell 中调用带 `--xxx` 参数的 node 命令时，要用 `& 'node.exe' '--xxx' 'yyy'` 形式传参，不然 `--` 会被 PS 解析成运算符报错
- Windows .bat 里若要调用外部 .ps1 脚本且 bat 本身会被复制到其他目录使用，**不要用 `%~dp0` 相对路径找脚本**（复制后 `%~dp0` 指向新目录，脚本不存在时 powershell.exe -File 会解析失败，ps1 注释里的单词会被 cmd 当命令跑，报 `witch/ouble-click/CRIPT` 这种"每个词首字母被吞"的怪错），应写死脚本的绝对路径，或在 bat 里先 pushd 回真实脚本根目录再调用

---

### DSH 6 插件统一整理（2026-09-23）

同学上次把 DSH 内容归拢进 `E:\0\AI\DSH` 后，6 个启用插件因 junction 绝对路径断链而 failed to import。本次已把 6 个插件统一平铺到 `E:\0\AI\DSH\plugins\` 根目录，并修复断链、更新 link 路径、重启验证通过。

**6 个插件新路径（均在 `E:\0\AI\DSH\plugins\`）：**
| 插件 | 原位置 → 新位置 |
|---|---|
| 鲸鱼娘皮肤 deep-whale-day-night-theme | skins\deep-whale-day-night-theme → plugins\deep-whale-day-night-theme |
| dsh-super-injector | dsh-plugins\dsh-routing-suite\injector → plugins\dsh-super-injector |
| dsh-memory-plugin | dsh-plugins\OpenViking\examples\dsh-memory-plugin → plugins\dsh-memory-plugin |
| dsh-improved-inline-edit | 本就在 plugins\ 根 |
| dsh-wallpaper-engine | dsh-plugins\dsh-wallpaper-engine → plugins\dsh-wallpaper-engine |
| DSH-Whale-Balance-Widget | dsh-plugins\DSH-Whale-Balance-Widget → plugins\DSH-Whale-Balance-Widget |

**关键动作：**
1. 改 `C:\Users\AiYi\.dsh\profiles\web\package.json` 的 6 个 link 路径
2. pnpm install 重建 profile node_modules 链接
3. PowerShell 原生方式修复 wallpaper-engine 断链的 7 个 junction
4. 重启 DSH 验证

**结果：** 重启后无 failed to import、无 1 entry did not activate；浏览器实测壁纸引擎、小鲸鱼余额挂件（¥0.58）、对话均正常，鲸鱼娘皮肤保持 disabled（已关闭）。

**待办：** dsh-plugins\ 残留未启用源码（awesome-dsh-plugin / distilly / MemOS / OpenViking 等），等同学决定是否清理。