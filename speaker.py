# speaker.py
# ──────────────────────────────────────────────────────────────
# Text-to-speech using gTTS + playsound.
# Runs in background thread — never blocks the main loop.
# ──────────────────────────────────────────────────────────────

import threading
import queue
import os
import tempfile
from gtts import gTTS
from playsound import playsound


class Speaker:
    def __init__(self):
        self._queue     = queue.Queue()
        self._last_said = ""
        self._stop_flag = False
        self._speaking  = False

        self._thread = threading.Thread(target=self._worker, daemon=True)
        self._thread.start()
        print("[SPEAKER] TTS ready.")

    def say(self, text: str, priority: bool = False):
        if not text:
            return
        self._last_said = text
        print(f"[FRIDAY] 🔊 {text}")

        if priority:
            while not self._queue.empty():
                try:
                    self._queue.get_nowait()
                except queue.Empty:
                    break

        self._queue.put(text)

    def is_speaking(self) -> bool:
        return self._speaking

    def wait_until_done(self):
        """Block until the speaker finishes speaking."""
        while self._speaking or not self._queue.empty():
            import time
            time.sleep(0.1)

    def stop(self):
        self._stop_flag = True

    def _worker(self):
        while not self._stop_flag:
            try:
                text = self._queue.get(timeout=0.5)
            except queue.Empty:
                continue

            self._speaking = True
            try:
                self._speak(text)
            except Exception as e:
                print(f"[SPEAKER] Error: {e}")
            finally:
                self._speaking = False

    def _speak(self, text: str):
        tmp = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
        tmp.close()
        try:
            tts = gTTS(text=text, lang="en", slow=False)
            tts.save(tmp.name)
            playsound(tmp.name)
        finally:
            try:
                os.remove(tmp.name)
            except Exception:
                pass