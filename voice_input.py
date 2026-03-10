# voice_input.py
import sounddevice as sd
import numpy as np
import json
import os
import zipfile
import urllib.request
import queue
import config
from vosk import Model, KaldiRecognizer


class VoiceInput:
    def __init__(self):
        self._ensure_model()
        self.model      = Model(os.path.join(config.VOSK_MODEL_DIR, config.VOSK_MODEL_NAME))
        self.recognizer = KaldiRecognizer(self.model, config.SAMPLE_RATE)
        print("[VOICE] Speech recognition ready (Vosk offline).")

    def listen_for_wake_word(self) -> bool:
        audio_queue = queue.Queue()

        def callback(indata, frames, time, status):
            audio_queue.put(bytes(indata))

        with sd.RawInputStream(
            samplerate = config.SAMPLE_RATE,
            blocksize  = 4000,
            dtype      = "int16",
            channels   = 1,
            callback   = callback,
        ):
            print(f"[VOICE] 👂 Listening for wake word: '{config.WAKE_WORD}'...")
            while True:
                data = audio_queue.get()
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    text   = result.get("text", "").lower()
                    if text:
                        print(f"[VOICE] Heard: '{text}'")
                    if config.WAKE_WORD.lower() in text:
                        return True

    def record_question(self) -> str:
        print(f"[VOICE] 🎤 Recording for up to {config.RECORD_SECONDS}s...")
        audio_data = sd.rec(
            int(config.RECORD_SECONDS * config.SAMPLE_RATE),
            samplerate = config.SAMPLE_RATE,
            channels   = 1,
            dtype      = "int16",
        )
        sd.wait()

        rec = KaldiRecognizer(self.model, config.SAMPLE_RATE)
        audio_bytes = audio_data.tobytes()
        chunk_size  = 4000

        for i in range(0, len(audio_bytes), chunk_size):
            rec.AcceptWaveform(audio_bytes[i : i + chunk_size])

        result = json.loads(rec.FinalResult())
        text   = result.get("text", "").strip()

        if text:
            print(f"[VOICE] You said: '{text}'")
        else:
            print("[VOICE] Could not understand.")

        return text

    def _ensure_model(self):
        model_path = os.path.join(config.VOSK_MODEL_DIR, config.VOSK_MODEL_NAME)
        if os.path.exists(model_path):
            return

        os.makedirs(config.VOSK_MODEL_DIR, exist_ok=True)
        zip_path = os.path.join(config.VOSK_MODEL_DIR, "model.zip")

        print(f"[VOICE] Downloading Vosk speech model (~50MB)...")
        urllib.request.urlretrieve(
            config.VOSK_MODEL_URL,
            zip_path,
            reporthook=self._download_progress,
        )
        print()

        print("[VOICE] Extracting model...")
        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall(config.VOSK_MODEL_DIR)

        os.remove(zip_path)
        print("[VOICE] ✓ Speech model ready.")

    @staticmethod
    def _download_progress(count, block_size, total_size):
        if total_size > 0:
            pct = count * block_size / total_size * 100
            print(f"\r[VOICE] Downloading: {min(pct, 100):.0f}%", end="", flush=True)