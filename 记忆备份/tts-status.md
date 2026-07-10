---
name: tts-status
description: TTS语音功能已重建并正常运行
metadata: 
  node_type: memory
  type: project
  originSessionId: af1f1c3c-41b6-4553-9ffa-aaebda45d1d1
---

# TTS 语音服务状态

## 现状
- ✅ **知更鸟 TTS 已重建并正常运行**
- 修复了 BERT fp16→fp32 在 CPU 上的段错误
- 当前位于 `E:\0\AI\CC\robin_tts.py`
- 可在文字回复外额外语音播报

## 调用方式
- 单次合成：`python robin_tts.py "文本" 情感`
- 常驻服务：`python robin_tts.py --serve`（端口 18765）

## 说明
- CPU 模式，首次加载约 5-10 分钟，合成约 30-60 秒
- 可用情感：NORMAL / HAPPY / SURPRISED / SAD / ANGRY / FEAR
- 合成后自动播放

**Why:** 避免后续误以为 TTS 不可用。
**How to apply:** 需要语音时直接调用，无需额外确认。
