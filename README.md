# 🤖 Jarvis — AI Voice Assistant

A fully voice-controlled AI assistant. Say the wake word, ask anything, hear the answer spoken aloud. No keyboard needed.

> Built by Gurneev Singh

---

## How It Works

1. Assistant listens continuously for the wake word **"Jarvis"**
2. When detected → says "Yes?" → records your question
3. Vosk transcribes your speech to text (runs fully offline)
4. Groq LLaMA AI thinks and generates a response
5. gTTS speaks the answer aloud
6. Goes back to listening

---

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add your Groq API key
Copy `config.example.py` to `config.py` and set:
```python
GROQ_API_KEY = "your-key-here"
```
Get a free key at: https://console.groq.com

### 3. Run
```bash
python main.py
```
On first run, the Vosk speech model (~50 MB) downloads automatically.

---

## Usage

| Say | What happens |
|-----|-------------|
| `"Jarvis"` | Wakes up the assistant |
| Any question | Gets an AI response spoken aloud |
| `"Jarvis forget everything"` | Clears conversation memory |
| `"Jarvis goodbye"` | Shuts down |

---

## Project Structure

```
ai-voice-assistant/
├── main.py              # Entry point — main loop
├── config.py            # Your settings (not in repo)
├── config.example.py    # Settings template
├── voice_input.py       # Wake word detection + mic recording + Vosk STT
├── ai_brain.py          # Groq LLaMA AI with conversation memory
├── speaker.py           # gTTS text-to-speech output
├── requirements.txt
└── vosk-model/          # Speech model (auto-downloaded, not in repo)
```

---

## Tech Stack

| Library | Purpose | Cost |
|---------|---------|------|
| Vosk | Wake word + speech recognition | Free / offline |
| Groq (LLaMA 3.3) | AI brain | Free |
| gTTS + playsound | Voice output | Free |
| sounddevice | Microphone input | Free |

**Fully offline STT** — speech recognition never sends audio to any server.

---

## Customise

All settings in `config.py`:
- `ASSISTANT_NAME` — change the name
- `WAKE_WORD` — change the wake word
- `SYSTEM_PROMPT` — change the personality
- `GROQ_MODEL` — swap the AI model
- `MAX_HISTORY` — how many exchanges to remember
- `RECORD_SECONDS` — how long to listen after wake word

---

## Future Plans

- [ ] Custom wake word training
- [ ] Smart home control (lights, music)
- [ ] Weather, news, reminders
- [ ] Emotion-aware responses
- [ ] Mobile app version

---

## Built by

Gurneev Singh
