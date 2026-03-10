# 🤖 Friday — AI Voice Assistant

A fully voice-controlled AI assistant. Say the wake word, ask anything, hear the answer spoken aloud. No keyboard needed.

> Built by Gurneev Singh

---

## How It Works

1. Assistant listens continuously for the wake word **"Friday"**
2. When detected → says "Yes?" → records your question
3. Vosk transcribes your speech to text (runs offline)
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
Open `config.py` and set:
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

| What to say | What happens |
|-------------|-------------|
| "Friday" | Activates the assistant |
| Any question | Gets an AI response |
| "Clear memory" | Forgets the conversation |
| "Goodbye" | Shuts down |

---

## Customise

All settings in `config.py`:
- `ASSISTANT_NAME` — change the name
- `WAKE_WORD` — change the wake word
- `SYSTEM_PROMPT` — change the personality
- `GROQ_MODEL` — swap the AI model
- `MAX_HISTORY` — how many messages to remember

---

## Project Structure

```
ai-voice-assistant/
├── main.py          # Entry point — main loop
├── config.py        # All settings
├── wake_word.py     # Detects wake word (Vosk, offline)
├── voice_input.py   # Microphone recording
├── transcriber.py   # Speech → text (Vosk, offline)
├── ai_brain.py      # Groq AI with conversation memory
├── speaker.py       # Text → speech (gTTS)
└── models/          # Vosk model (auto-downloaded)
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

## Future Plans

- [ ] Custom wake word training
- [ ] Smart home control (lights, music)
- [ ] Weather, news, reminders
- [ ] Emotion-aware responses
- [ ] Mobile app version
