---
name: hiragana-lipsync-setup
description: Hiragana LipSync MMD口型工具配置完成
metadata: 
  node_type: memory
  type: project
  originSessionId: 873f87f5-a7b2-49a2-b3a5-3d1d58491ac5
---

# Hiragana LipSync 配置记录

## 项目位置
`E:\0\MMD\嘴型自动生成Hiragana-LipSync-main`

## 用途
从日语WAV/MP3音频自动生成MMD口型VMD文件（あいうえおん6种口型）

## 完成的工作

### 1. 依赖安装
- **Python**: C:\Python312\python.exe (3.12.9)
- **PySide6 6.11.1** — GUI界面
- **scipy 1.18.0** — 音频重采样
- **PyTorch 2.11.0+cu128** — CUDA版，支持RTX 4060

### 2. 模型下载
从 HuggingFace `TylorShine/wavlm-base-plus-hiragana-ctc-v2` 下载到 `model/` 文件夹：
- `model.safetensors` (366MB)
- `config.json`, `preprocessor_config.json`
- `configuration_dual_ctc.py`, `modeling_dual_ctc.py`
- `phoneme_tokenizer/` — 音素tokenizer
- `kana_tokenizer/`

### 3. 修改的文件
- **`src/window.py`** — GPU复选框默认勾选（`setChecked(True)`）
- **`src/core.py`** — VMD导出路径改为 `d:/AiYi/Downloads`
- **`启动.bat`** — 修复路径问题（用 `pushd` 替代 `cd /d "%~dp0"`）

### 4. GPU信息
- NVIDIA GeForce RTX 4060 Laptop GPU (8GB VRAM)
- CUDA 12.8
- GPU版PyTorch已安装，默认启用GPU加速

## 使用方法
双击 `启动.bat`，拖入日语WAV/MP3文件，点击「生成VMD」
