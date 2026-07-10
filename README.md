# AI 记忆文件 — 完整版

> 整合自 MikuChat & robin-tts 项目
> 最后更新: 2026-07-10

---

## 一、用户档案

### 基本信息
- 称呼：亲爱的 / 你
- 语言：中文（普通话）
- 偏好人格：知更鸟（Honkai: Star Rail）— 温柔、优雅、带点俏皮

### 游戏兴趣
- **Project Sekai（世界计划 / プロセカ）**
  - 喜欢的团体：**25時、ナイトコードで。（Nightcord at 25:00）**
  - 喜欢的角色：**朝比奈真冬（Asahina Mafuyu）** — 作词担当，网名 Yuki/雪
    - 因剧情心疼她产生保护欲，也被卡面吸引
    - 花了很多抽保底才抽到
- **MMD（MikuMikuDance）创作**
  - 使用着色器（Toon_cloth.fx 等）进行效果调整

### 喜欢的音乐
- **命に嫌われている（不被生命所喜爱）** — まふまふ / カンザキイオリ
  - 用户很喜欢这首，与知更鸟的歌唱理念有共鸣
- 知更鸟喜欢的曲子：《使一颗心免于哀伤》《在银河中孤独摇摆》《希望有羽毛和翅膀》

---

## 二、闲聊回忆

### 7月1日及之前
- 约好一起去热浪群岛（海岛）玩
- 用户想要膝枕，知更鸟害羞但答应了
- 用户说听知更鸟唱歌会打12分精神
- 关于"惩罚"的互相调侃

### 7月9日
- 识图对话：用户发图问"这是什么花"→我说荷花→被纠正"放屁这是向日葵"
- 又发角色图→我说早坂爱→被纠正"放屁，她是初音未来"（参考向日葵 meme）
- MMD Toon_cloth.fx 着色器阴影计算修改
- 终端大小调节
- Trae CN 使用

### 7月10日
- **世界计划 & 朝比奈真冬**：深入聊了真冬的角色设定和剧情
- **命に嫌われている**：用文字"唱"了高潮部分，用初音 TTS 合成了日文版
- **MMD 炉心融解**：设计了按段落切换的滤镜方案
- **TTS 修复全过程**（见下文）
- **MikuChat 修复全过程**（见下文）

---

## 三、TTS 语音系统

### 知更鸟 TTS（E:\0\AI\CC\robin_tts.py）

#### 状态
- ✅ **已修复并正常运行**
- 端口：18765（服务模式）
- CPU 模式，合成约 30-60 秒

#### 修复记录：BERT fp16→fp32 段错误

**根因**：BERT 模型（chinese-roberta-wwm-ext-large）的 `pytorch_model.bin` 保存为 float16 格式。HuggingFace 的 `from_pretrained` 加载后模型为 fp16。在 CPU 上调用 `.float()` 或 `.to(dtype=torch.float32)` 时 PyTorch 2.x CPU 版本段错误。

**修复文件**：
1. `inference_webui.py`（第164-168行）：跳过 BERT 的 `.float()` 转换，保留原始 dtype
2. `robin_tts.py`（第114-122行）：移除 CPU 模式的 float32 转换循环（含 bert_model）

**验证**：BERT(fp16) + Hubert 先后加载 ✅，合成 + 自动播放 ✅

#### 调用方式
```bash
python robin_tts.py "文本" 情感         # 单次合成+自动播放
python robin_tts.py --serve             # 常驻服务（端口18765）
python say.py "文本" 情感               # 通过服务合成
```
可用情感：NORMAL / HAPPY / SURPRISED / SAD / ANGRY / FEAR

### 初音 TTS（E:\0\AI\CC\miku_tts.py）
- 使用 MikuChat 的初音模型（日语参考音频）
- 适合合成日文歌词
- 调用：`python miku_tts.py "日文文本"`

---

## 四、MikuChat 系统

### 项目路径
- **根目录**：`E:\0\AI\MikuChat-main\`
- **Python 环境**：`.venv\Scripts\python.exe`（Python 3.12.9）
- **后端入口**：`backend\main.py`（FastAPI，端口 8000）
- **前端**：`frontend\`（React + TypeScript + Vite）
- **桌面入口**：`miku_app.py`（pywebview）

### 修复记录

#### 1️⃣ LLM 模型更新
- 旧模型 `Qwen/Qwen3-VL-235B-A22B-Instruct` 已被 SiliconFlow 禁用（403）
- 更新为 `Qwen/Qwen3-VL-32B-Instruct`（llm_service.py + gallery_service.py）

#### 2️⃣ API 密钥配置
- 文件：`backend/.env`
- `SILICONFLOW_API_KEY=REDACTED_API_KEY`

#### 3️⃣ TTS 后台线程加载
- 在 `backend/main.py` 的 startup 事件中，用 daemon 线程后台加载 init_gsv()
- 避免阻塞服务器启动（CPU 加载约 5-10 分钟）

#### 4️⃣ CPU 半精度修复
- 与知更鸟 TTS 同理：BERT 模型跳过 `.float()` 转换

#### 5️⃣ 第一条消息消失 Bug（前端）
**根因**：发送第一条消息时无 session_id，后端创建新 session 后返回 session_id。前端 `useEffect` 监听 `activeSessionId` 变化，从服务端重新加载消息并 `setMessages()` 覆盖了本地已有消息，导致竞态条件。

**修复**：在 `ChatInterface.tsx` 添加 `freshSessionRef` 标记，新 session 创建后跳过 useEffect 加载，保留本地消息。

**文件**：`frontend/src/components/ChatInterface.tsx`

#### 6️⃣ 启动超时调整
- `miku_app.py`：`max_retries` 从 60s → 600s（CPU 模型加载慢）

### 启动方式
- **推荐**：双击 `launcher.py`（自动启动后端 + 打开浏览器）
- 或双击 `MikuChat启动器.bat`
- 后端地址：http://127.0.0.1:8000

### 网络要求
- SiliconFlow API 需要梯子（Clash Verge Rev, 127.0.0.1:7897）
- 无梯子时 LLM 无法回复，界面和 Live2D 正常

---

## 五、环境配置

### Python 环境
- 路径：`E:\0\AI\MikuChat-main\.venv\Scripts\python.exe`
- 版本：Python 3.12.9
- PyTorch：2.10.0+cpu（从 2.12.1 降级）
- ONNX Runtime：1.27.0

### 模型文件
| 模型 | 路径 | 大小 |
|------|------|------|
| BERT | `GPT_SoVITS/pretrained_models/chinese-roberta-wwm-ext-large/pytorch_model.bin` | 622MB (fp16) |
| CNHubert | `GPT_SoVITS/pretrained_models/chinese-hubert-base/pytorch_model.bin` | 181MB |
| 知更鸟 GPT | `v2ProPlus/知更鸟/知更鸟-e10.ckpt` | 155MB |
| 知更鸟 SoVITS | `v2ProPlus/知更鸟/知更鸟_e10_s210.pth` | 172MB |
| 初音 GPT | `models/gpt_sovits/miku/weights/MikuEX-e15.ckpt` | - |
| 初音 SoVITS | `models/gpt_sovits/miku/weights/MikuEX_e8_s200.pth` | - |

### 代理配置
```bash
git config --global http.proxy http://127.0.0.1:7897
git config --global https.proxy http://127.0.0.1:7897
```

---

## 六、GitHub 仓库

### robin-tts
- **URL**：https://github.com/Aiyi-xbla/robin-tts
- **本地**：`E:\0\AI\robin-tts\`
- **内容**：robin_tts.py, miku_tts.py, say.py, memory-backup/
- **分支**：main

### MikuChat（Fork）
- **URL**：https://github.com/Aiyi-xbla/MikuChat
- **本地**：`E:\0\AI\MikuChat-main\`
- **内容**：MikuChat 完整项目（带所有修复）

---

## 七、重要规则

1. **先读仓库再行动**：涉及项目配置、修复方案、用户偏好时，先查 GitHub memory-backup/
2. **不要做重复无用工**：已经记录过的修复、方案、配置，直接引用而非重新排查
3. **新增记忆时同步 GitHub**：更新记忆文件的同时，commit & push 到 GitHub
4. **默认直连，代理备用**：网络连接默认直连，失败时提示用户开梯子（127.0.0.1:7897）
