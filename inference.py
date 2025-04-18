import os
import torch
import torchaudio
import pandas as pd
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts

# --------- CONFIG ---------
INPUT_FILE = "input.xlsx"  # Change to 'input.csv' if using CSV
TEXT_COLUMN = "text"       # Name of the column that holds the Arabic text
SPEAKER_WAV = "sample/18_153.wav"
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)
# ---------------------------

print("Loading model...")
config = XttsConfig()
config.load_json("TrainedModel/GPT_XTTS_v2.0_LJSpeech_FT-April-12-2025_03+33PM-0000000/config.json")
model = Xtts.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir="TrainedModel/GPT_XTTS_v2.0_LJSpeech_FT-April-12-2025_03+33PM-0000000/", use_deepspeed=False)
model.to(torch.device("cpu"))

print("Computing speaker latents...")
gpt_cond_latent, speaker_embedding = model.get_conditioning_latents(audio_path=[SPEAKER_WAV])

# Load the text lines
print(f"Reading input file: {INPUT_FILE}")
if INPUT_FILE.endswith(".csv"):
    df = pd.read_csv(INPUT_FILE)
elif INPUT_FILE.endswith(".xlsx"):
    df = pd.read_excel(INPUT_FILE)
else:
    raise ValueError("Unsupported input file format. Use .csv or .xlsx")

# Inference loop
for idx, text in enumerate(df[TEXT_COLUMN]):
    print(f"[{idx+1}/{len(df)}] Generating audio for: {text}")
    out = model.inference(
        text,
        "ar",
        gpt_cond_latent,
        speaker_embedding,
        temperature=0.7,
    )
    out_path = os.path.join(OUTPUT_DIR, f"output_{idx+1:03}.wav")
    torchaudio.save(out_path, torch.tensor(out["wav"]).unsqueeze(0), 24000)
    print(f"Saved: {out_path}")

print("✅ All audio files generated.")
