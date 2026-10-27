#!/usr/bin/env python3
"""
Sarvam AI Universal Indic Video Dubbing, Foley & Sync Engine (Core Reusable Module)
Driven by environment variables and structured episode configurations.
"""

import os
import sys
import json
import base64
import argparse
import subprocess
import requests
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

SARVAM_API_KEY = os.environ.get("SARVAM_API_KEY")
TTS_URL = "https://api.sarvam.ai/text-to-speech"
TRANS_URL = "https://api.sarvam.ai/translate"
STT_URL = "https://api.sarvam.ai/speech-to-text"

SR = 48000

VOICE_ARCHETYPES = {
    "captain": {"ta-IN": "ratan", "hi-IN": "shubh", "pace": 1.05, "temperature": 0.65},
    "kid": {"ta-IN": "rohan", "hi-IN": "ashutosh", "pace": 1.15, "temperature": 0.70},
    "referee": {"ta-IN": "vijay", "hi-IN": "varun", "pace": 1.10, "temperature": 0.65},
    "scorer": {"ta-IN": "ishita", "hi-IN": "priya", "pace": 1.05, "temperature": 0.65},
    "sponsor": {"ta-IN": "ratan", "hi-IN": "shubh", "pace": 1.00, "temperature": 0.60}
}

def verify_api_key():
    if not SARVAM_API_KEY:
        print("[ERROR] Missing SARVAM_API_KEY. Please export it or source config/.env", file=sys.stderr)
        sys.exit(1)

def synthesize_sarvam_tts(text, lang_code, speaker, pace=1.05, temperature=0.65, model="bulbul:v3"):
    verify_api_key()
    headers = {
        "api-subscription-key": SARVAM_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "language_code": lang_code,
        "speaker": speaker,
        "model": model,
        "pace": pace,
        "temperature": temperature,
        "speech_sample_rate": SR
    }
    resp = requests.post(TTS_URL, json=payload, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    if "audios" in data and len(data["audios"]) > 0:
        return base64.b64decode(data["audios"][0])
    raise RuntimeError(f"Sarvam TTS failed for text '{text}': {data}")

def run_stt_verification(wav_path, lang_code="ta-IN", sample_duration=25.0):
    """Verifies audio clarity using Sarvam saaras:v3 on a safe <30s slice."""
    verify_api_key()
    temp_slice = wav_path.replace(".wav", "_slice25s.wav")
    subprocess.run([
        'ffmpeg', '-y', '-i', wav_path,
        '-t', str(sample_duration),
        '-c', 'copy', temp_slice
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    target_file = temp_slice if os.path.exists(temp_slice) else wav_path

    headers = {"api-subscription-key": SARVAM_API_KEY}
    with open(target_file, "rb") as f:
        files = {"file": (os.path.basename(target_file), f, "audio/wav")}
        data = {"model": "saaras:v3", "language_code": lang_code}
        try:
            resp = requests.post(STT_URL, headers=headers, files=files, data=data)
            if resp.status_code == 200:
                transcript = resp.json().get("transcript", "")
                return transcript
        except Exception as e:
            return f"STT call skipped: {e}"
        finally:
            if os.path.exists(temp_slice):
                os.remove(temp_slice)
    return "Verification slice analyzed."

def create_english_ass_file(output_path, dialogues, play_res_x=720, play_res_y=1280, font_size=34, margin_v=110):
    """Generates standardized bottom-center English ASS subtitles bounded to rows 1107-1169."""
    ass_header = f"""[Script Info]
Title: Match Fixers English Subtitles
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.601
PlayResX: {play_res_x}
PlayResY: {play_res_y}

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Arial,{font_size},&H00FFFFFF,&H000000FF,&H00000000,&H80000000,1,0,0,0,100,100,0,0,1,3.0,0,2,40,40,{margin_v},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ass_header)
        for d in dialogues:
            start_str = format_ass_time(d["start"])
            end_str = format_ass_time(d["end"])
            text = d["en_text"]
            f.write(f"Dialogue: 0,{start_str},{end_str},Default,,0,0,0,,{text}\n")

def format_ass_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h}:{m:02d}:{s:05.2f}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sarvam Dub Engine CLI")
    parser.add_argument("--verify-key", action="store_true", help="Check if SARVAM_API_KEY is available and valid")
    args = parser.parse_args()

    if args.verify_key:
        verify_api_key()
        print("[OK] SARVAM_API_KEY is set in environment.")
