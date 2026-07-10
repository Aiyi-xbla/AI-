"""
初音ミク (Hatsune Miku) TTS — 临时调用脚本
"""
import os, sys, uuid

MIKUCHAT_DIR = r"E:\0\AI\MikuChat-main"
BACKEND_DIR = os.path.join(MIKUCHAT_DIR, "backend")
GSV_CORE_DIR = os.path.join(BACKEND_DIR, "gpt_sovits_core")
GSV_SUB_DIR = os.path.join(GSV_CORE_DIR, "GPT_SoVITS")
PRETRAINED_DIR = os.path.join(GSV_SUB_DIR, "pretrained_models")

MIKU_DIR = os.path.join(BACKEND_DIR, "models", "gpt_sovits", "miku")
GPT_W = os.path.join(MIKU_DIR, "weights", "MikuEX-e15.ckpt")
SOVITS_W = os.path.join(MIKU_DIR, "weights", "MikuEX_e8_s200.pth")
REF_DIR = os.path.join(MIKU_DIR, "reference")

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "robin_voice")
os.makedirs(OUTPUT_DIR, exist_ok=True)

os.environ["gpt_path"] = GPT_W
os.environ["sovits_path"] = SOVITS_W
os.environ["is_half"] = "False"

import torch
device = "cuda" if torch.cuda.is_available() else "cpu"
os.environ["device"] = device
print(f"[Miku TTS] 设备: {device}")

os.environ["bert_path"] = os.path.join(PRETRAINED_DIR, "chinese-roberta-wwm-ext-large")
os.environ["cnhubert_base_path"] = os.path.join(PRETRAINED_DIR, "chinese-hubert-base")

os.chdir(GSV_CORE_DIR)
sys.path.insert(0, GSV_CORE_DIR)
sys.path.insert(0, GSV_SUB_DIR)
sys.path.insert(0, BACKEND_DIR)

import GPT_SoVITS.inference_webui as gsv

# 加载初音模型
print("加载 Miku GPT...")
gsv.change_gpt_weights(gpt_path=GPT_W)

print("加载 Miku SoVITS...")
gen = gsv.change_sovits_weights(sovits_path=SOVITS_W, prompt_language="日文", text_language="日文")
try: next(gen)
except: pass

# 找语言key
ref_lang = target_lang = None
try:
    for k, v in gsv.dict_language.items():
        if v == "all_ja": ref_lang = k
        if v == "ja": target_lang = k
except:
    ref_lang = "日文"
    target_lang = "日文"

# 用第一个参考音频
ref_wavs = [f for f in os.listdir(REF_DIR) if f.endswith('.wav')]
ref_wav = os.path.join(REF_DIR, ref_wavs[0])
ref_text = ref_wavs[0].replace('.wav','').strip()

text = sys.argv[1] if len(sys.argv) > 1 else "こんにちは、初音ミクです。"
print(f"合成: {text}")

result = gsv.get_tts_wav(
    ref_wav_path=ref_wav,
    prompt_text=ref_text,
    prompt_language=ref_lang,
    text=text,
    text_language=target_lang,
    top_p=1, temperature=1, how_to_cut="凑四句一切",
)

result_list = list(result)
os.chdir(BACKEND_DIR)

if result_list:
    sr, audio = result_list[-1]
    import soundfile as sf
    out = os.path.join(OUTPUT_DIR, f"miku_{uuid.uuid4().hex[:8]}.wav")
    sf.write(out, audio, sr)
    print(f"✅ {out}")

    import winsound
    winsound.PlaySound(out, winsound.SND_FILENAME)
    print("🔊 播放中...")
else:
    print("❌ 合成失败")
