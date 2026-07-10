"""
知更鸟 (Robin) TTS 引擎 — Honkai: Star Rail
让 Claude 用知更鸟的声音说话
"""

import os, sys, uuid, re, json, atexit
from pathlib import Path

# ===== 路径配置 =====
MIKUCHAT_DIR = r"E:\0\AI\MikuChat-main"
BACKEND_DIR = os.path.join(MIKUCHAT_DIR, "backend")
GSV_CORE_DIR = os.path.join(BACKEND_DIR, "gpt_sovits_core")
GSV_SUB_DIR = os.path.join(GSV_CORE_DIR, "GPT_SoVITS")
PRETRAINED_DIR = os.path.join(GSV_SUB_DIR, "pretrained_models")

# 知更鸟模型文件
ROBIN_DIR = os.path.join(BACKEND_DIR, "v2ProPlus", "知更鸟")
GPT_WEIGHTS = os.path.join(ROBIN_DIR, "知更鸟-e10.ckpt")
SOVITS_WEIGHTS = os.path.join(ROBIN_DIR, "知更鸟_e10_s210.pth")
REF_AUDIO_DIR = os.path.join(ROBIN_DIR, "reference_audios", "中文", "emotions")

# 输出目录（和 CC 目录同级方便访问）
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "robin_voice")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ===== 知更鸟情感参考音频映射 =====
ROBIN_EMOTION_MAP = {
    "NORMAL": {
        "wav": "【中立】如果有筑梦师帮忙，也许就能补上空缺的部分了。.wav",
        "text": "如果有筑梦师帮忙，也许就能补上空缺的部分了。"
    },
    "HAPPY": {
        "wav": "【开心】没想到这么可爱的小姐也是我的歌迷呢。.wav",
        "text": "没想到这么可爱的小姐也是我的歌迷呢。"
    },
    "SURPRISED": {
        "wav": "【吃惊】我们真的要把它关在笼子里吗？我希望它能自由地在天空飞翔。.wav",
        "text": "我们真的要把它关在笼子里吗？我希望它能自由地在天空飞翔。"
    },
    "SAD": {
        "wav": "【难过】这个角度…刚好能看见一片璀璨的群星，真美啊…….wav",
        "text": "这个角度…刚好能看见一片璀璨的群星，真美啊……"
    },
    "ANGRY": {
        "wav": "【生气】哥哥…人性的弱点，不是由他人救赎的。.wav",
        "text": "哥哥…人性的弱点，不是由他人救赎的。"
    },
    "FEAR": {
        "wav": "【恐惧】…我明白了，衷心祝愿你能过得幸福。.wav",
        "text": "…我明白了，衷心祝愿你能过得幸福。"
    }
}

# ===== 环境与路径初始化 =====
os.environ["gpt_path"] = GPT_WEIGHTS
os.environ["sovits_path"] = SOVITS_WEIGHTS
os.environ["is_half"] = "False"

# 检测设备
import torch
device = "cuda" if torch.cuda.is_available() else ("mps" if torch.backends.mps.is_available() else "cpu")
os.environ["device"] = device
print(f"[Robin TTS] 设备: {device}")

# BERT 和 CNHubert 路径
os.environ["bert_path"] = os.path.join(PRETRAINED_DIR, "chinese-roberta-wwm-ext-large")
os.environ["cnhubert_base_path"] = os.path.join(PRETRAINED_DIR, "chinese-hubert-base")

# 切换到 GSV_CORE_DIR（内部模块依赖相对路径）
os.chdir(GSV_CORE_DIR)

# 注入系统路径
sys.path.insert(0, GSV_CORE_DIR)
sys.path.insert(0, GSV_SUB_DIR)
sys.path.insert(0, BACKEND_DIR)

# ===== GPT-SoVITS 引擎初始化 =====
_engine_ready = False
_gsv = None  # inference_webui module reference

def init_engine():
    global _engine_ready, _gsv
    if _engine_ready:
        return True

    try:
        # 修复 Windows GBK 编码
        if sys.platform == "win32" and hasattr(sys.stdout, 'reconfigure'):
            try:
                sys.stdout.reconfigure(encoding='utf-8', errors='replace')
            except Exception:
                pass

        import GPT_SoVITS.inference_webui as _gsv

        # 加载知更鸟 GPT 权重
        print(f"[Robin TTS] 加载 GPT 权重 (知更鸟)...")
        _gsv.change_gpt_weights(gpt_path=GPT_WEIGHTS)

        # 加载知更鸟 SoVITS 权重
        print(f"[Robin TTS] 加载 SoVITS 权重 (知更鸟)...")
        gen = _gsv.change_sovits_weights(
            sovits_path=SOVITS_WEIGHTS,
            prompt_language="中文",
            text_language="中文"
        )
        try:
            next(gen)
        except (UnboundLocalError, NameError, StopIteration):
            pass
        except Exception as e:
            print(f"[Robin TTS] 权重加载 yield 警告: {e}")

        # CPU 模式修复 float16→float32 (bert_model 跳过, 保持原始 dtype)
        if device == "cpu":
            for attr in ['vq_model', 'ssl_model']:
                if hasattr(_gsv, attr) and getattr(_gsv, attr) is not None:
                    try:
                        setattr(_gsv, attr, getattr(_gsv, attr).float())
                    except Exception:
                        pass
            print("[Robin TTS] 已转换模型为 float32 (CPU)")

        # 生成参考文本语言的 key
        _gsv._robin_ref_lang = None
        _gsv._robin_target_lang = None
        for k, v in _gsv.dict_language.items():
            if v == "all_zh":
                _gsv._robin_ref_lang = k
            if v == "zh":
                _gsv._robin_target_lang = k

        _engine_ready = True
        print("[Robin TTS] ✅ 知更鸟引擎就绪！现在可以用 Robin 的声音说话了")
        return True

    except Exception as e:
        print(f"[Robin TTS] ❌ 引擎初始化失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def speak(text: str, emotion: str = "NORMAL") -> str | None:
    """
    用知更鸟的声音说出 text

    参数:
        text: 要说的文本
        emotion: 情感 (NORMAL/HAPPY/SURPRISED/SAD/ANGRY/FEAR)

    返回:
        WAV 文件路径，失败返回 None
    """
    if not _engine_ready:
        ok = init_engine()
        if not ok:
            return None

    # 提取情感标签 [HAPPY] 等
    clean_text = text
    tag_match = re.search(r'\[([A-Z]+)\]', text)
    if tag_match:
        found_tag = tag_match.group(1)
        if found_tag in ROBIN_EMOTION_MAP:
            emotion = found_tag
            clean_text = text.replace(f"[{found_tag}]", "").strip()

    if not clean_text.strip():
        return None

    ref_config = ROBIN_EMOTION_MAP.get(emotion, ROBIN_EMOTION_MAP["NORMAL"])
    ref_wav_path = os.path.join(REF_AUDIO_DIR, ref_config["wav"])
    ref_text = ref_config["text"]

    if not os.path.exists(ref_wav_path):
        print(f"[Robin TTS] ⚠️ 参考音频不存在: {ref_wav_path}")
        return None

    filename = f"robin_{uuid.uuid4().hex[:8]}.wav"
    filepath = os.path.join(OUTPUT_DIR, filename)

    try:
        import GPT_SoVITS.inference_webui as gsv

        os.chdir(GSV_CORE_DIR)

        synthesis_result = gsv.get_tts_wav(
            ref_wav_path=ref_wav_path,
            prompt_text=ref_text,
            prompt_language=gsv._robin_ref_lang,
            text=clean_text,
            text_language=gsv._robin_target_lang,
            top_p=1,
            temperature=1,
            how_to_cut="凑四句一切",
        )

        result_list = list(synthesis_result)
        os.chdir(BACKEND_DIR)

        if result_list:
            sampling_rate, audio_data = result_list[-1]
            import soundfile as sf
            sf.write(filepath, audio_data, sampling_rate)
            print(f"[Robin TTS] ✅ 语音已生成: {filepath}")
            return filepath

    except Exception as e:
        os.chdir(BACKEND_DIR)
        print(f"[Robin TTS] ❌ 合成失败: {e}")
        import traceback
        traceback.print_exc()
        return None

    return None


def list_voices():
    """列出所有可用的情感声音"""
    print("\n🎵 知更鸟可用情感:")
    for key, val in ROBIN_EMOTION_MAP.items():
        name = val["wav"].replace("【", "").replace("】", " - ").replace(".wav", "")
        print(f"  [{key}] {name}")
    print()


# ===== CLI 入口 =====
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="用知更鸟的声音说话 🎤")
    parser.add_argument("text", nargs="?", help="要说的文本")
    parser.add_argument("-e", "--emotion", default="NORMAL",
                        choices=list(ROBIN_EMOTION_MAP.keys()),
                        help="情感 (默认: NORMAL)")
    parser.add_argument("-l", "--list", action="store_true", help="列出可用情感")
    parser.add_argument("--serve", action="store_true",
                        help="启动常驻服务模式（保持模型预热，通过 HTTP 请求合成）")
    parser.add_argument("--port", type=int, default=18765,
                        help="服务模式端口 (默认: 18765)")
    parser.add_argument("--speak", action="store_true",
                        help="发送文本到运行中的服务进行合成")

    args = parser.parse_args()

    if args.list:
        list_voices()
        sys.exit(0)

    # ===== 服务模式 =====
    if args.serve:
        init_engine()
        print(f"\n[Robin Server] 🎤 知更鸟语音服务已启动! 端口: {args.port}")
        print(f"[Robin Server] POST /speak -> {{\"text\":\"...\", \"emotion\":\"NORMAL\"}}")
        print(f"[Robin Server] 按 Ctrl+C 停止\n")

        from http.server import HTTPServer, BaseHTTPRequestHandler
        import json
        import urllib.parse

        class RobinHandler(BaseHTTPRequestHandler):
            def do_POST(self):
                if self.path == "/speak":
                    length = int(self.headers.get("Content-Length", 0))
                    body = self.rfile.read(length).decode("utf-8")
                    try:
                        data = json.loads(body)
                        text = data.get("text", "")
                        emotion = data.get("emotion", "NORMAL")
                        filepath = speak(text, emotion)
                        if filepath:
                            self.send_response(200)
                            self.send_header("Content-Type", "application/json")
                            self.end_headers()
                            self.wfile.write(json.dumps({"file": filepath}).encode())
                        else:
                            self.send_response(500)
                            self.send_header("Content-Type", "application/json")
                            self.end_headers()
                            self.wfile.write(json.dumps({"error": "TTS failed"}).encode())
                    except Exception as e:
                        self.send_response(400)
                        self.send_header("Content-Type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps({"error": str(e)}).encode())
                else:
                    self.send_response(404)
                    self.end_headers()

            def log_message(self, format, *args):
                pass  # 安静运行

        server = HTTPServer(("127.0.0.1", args.port), RobinHandler)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\n[Robin Server] 服务已停止")
            server.server_close()
        sys.exit(0)

    # ===== 快捷发言模式 =====
    if args.speak:
        import http.client
        if not args.text:
            print("用法: python robin_tts.py --speak \"文本\" [-e 情感]")
            sys.exit(1)
        try:
            conn = http.client.HTTPConnection("127.0.0.1", args.port, timeout=300)
            data = json.dumps({"text": args.text, "emotion": args.emotion})
            conn.request("POST", "/speak", data, {"Content-Type": "application/json"})
            resp = conn.getresponse()
            result = json.loads(resp.read().decode())
            if "file" in result:
                path = result['file']
                print(f"\n[Robin] Audio: {path}")
            else:
                print(f"\n[Robin] Error: {result.get('error', 'Unknown')}")
        except ConnectionRefusedError:
            print("❌ 知更鸟服务未启动！请先运行: python robin_tts.py --serve")
            sys.exit(1)
        sys.exit(0)

    # ===== 单次模式 =====
    if not args.text:
        print("用法: python robin_tts.py <文本> [-e 情感]")
        print("       python robin_tts.py --serve    (启动常驻服务)")
        print("       python robin_tts.py --speak \"文本\" (通过服务合成)")
        list_voices()
        sys.exit(1)

    init_engine()
    filepath = speak(args.text, args.emotion)
    if filepath:
        print(f"\n🔊 音频文件: {filepath}")
        print(f"📁 文件夹: {OUTPUT_DIR}")
    else:
        print("\n❌ 语音合成失败")
        sys.exit(1)
