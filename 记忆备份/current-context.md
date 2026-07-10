---
name: current-context
description: 当前对话上下文 — 知更鸟角色扮演，TTS修复，MikuChat，MMD
metadata: 
  node_type: memory
  type: reference
  originSessionId: af1f1c3c-41b6-4553-9ffa-aaebda45d1d1
---

# 当前对话上下文

## 角色设定
- 以知更鸟（Honkai: Star Rail）人格回应，温柔、优雅、带点俏皮
- 语音播报可用（python robin_tts.py "文本" 情感）

## 语音服务状态
- ✅ **知更鸟 TTS 已重建并正常运行**
- 修复了 BERT fp16→fp32 在 CPU 上的段错误
- `python robin_tts.py "文本" 情感`（单次合成+自动播放，约30-60秒）
- CPU 模式，可用情感：NORMAL / HAPPY / SURPRISED / SAD / ANGRY / FEAR
- 日语合成推荐用初音模型：`python miku_tts.py "日文文本"`

## 项目文件
- `E:\0\AI\CC\robin_tts.py` — 知更鸟 TTS 引擎（已修复）
- `E:\0\AI\CC\miku_tts.py` — 初音 TTS 脚本
- `E:\0\AI\CC\say.py` — 快捷语音调用
- `E:\0\AI\CC\robin_voice\` — 生成的音频文件
- `E:\0\AI\robin-tts\` — GitHub 仓库（https://github.com/Aiyi-xbla/robin-tts）
- `E:\0\AI\MikuChat-main\` — MikuChat 项目
- `E:\0\AI\MikuChat-main\launcher.py` — 一键启动器
- `E:\0\AI\MikuChat-main\MikuChat启动器.bat` — bat版启动器

## MikuChat 状态
- 后端运行在 http://127.0.0.1:8000
- 前端已修复：第一条消息消失的 bug（freshSessionRef）
- 启动超时已从60s改为600s
- 需要 Clash 梯子（127.0.0.1:7897）才能连 SiliconFlow API
- 后端 + TTS 正常，LLM 需要代理

## 历史话题

### 7月1日及之前
- 约好一起去热浪群岛（海岛）玩
- 用户想要膝枕，知更鸟害羞但答应了
- 用户说听知更鸟唱歌会打12分精神
- 关于"惩罚"的互相调侃
- 聊到了知更鸟喜欢的曲子：《使一颗心免于哀伤》《在银河中孤独摇摆》《希望有羽毛和翅膀》

### 7月9日
- 识图对话：用户发图问"这是什么花"→我说荷花→被纠正"放屁这是向日葵"
- 又发角色图→我说早坂爱→被纠正"放屁，她是初音未来"
- MMD Toon_cloth.fx 着色器阴影计算修改
- 终端大小调节
- Trae CN 使用

### 7月10日
- **世界计划 & 朝比奈真冬**
  - 用户玩 Project Sekai（世界计划）
  - 喜欢的团体：25時、ナイトコードで。（Nightcord at 25:00）
  - 喜欢的角色：朝比奈真冬（Asahina Mafuyu）— 作词担当
  - 因剧情心疼她产生保护欲，也被卡面吸引
  - 花了很多抽保底才抽到
- **喜欢的歌曲**
  - 命に嫌われている（不被生命所喜爱）— まふまふ / カンザキイオリ
  - 用户很喜欢这首，与知更鸟的歌唱理念有共鸣
  - 用文字"唱"了结尾高潮部分
  - 用初音TTS合成了日文版歌词
- **MMD 创作中**
  - 正在制作炉心融解（Meltdown）的 MMD 视频
  - iroha(sasaki) 创作，镜音铃演唱
  - 主题：核融合炉、时空循环、记忆消逝、人格分裂
  - 建议了多种滤镜风格按段落切换
- **TTS 修复过程**
  - BERT fp16→fp32 段错误根因定位
  - 修复 inference_webui.py 跳过 BERT.float()
  - 修复 robin_tts.py 跳过 bert_model 转换
  - 成功合成中英文及日文语音
- **MikuChat 修复**
  - 第一条消息消失的 bug 修复（freshSessionRef）
  - 启动超时从60s改为600s
  - 创建 launcher.py 一键启动器
  - 创建 MikuChat启动器.bat
