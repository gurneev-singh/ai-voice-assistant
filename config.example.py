# config.example.py
# Copy this file to config.py and fill in your values

GROQ_API_KEY   = "YOUR_GROQ_API_KEY_HERE"   # https://console.groq.com
GROQ_MODEL     = "llama-3.3-70b-versatile"

ASSISTANT_NAME = "Jarvis"
WAKE_WORD      = "jarvis"

SYSTEM_PROMPT  = """You are Jarvis, a smart and friendly AI voice assistant.
You give short, clear, conversational answers — ideally 1-3 sentences.
Never use bullet points or markdown — speak naturally as if in a conversation.
If asked something you don't know, say so honestly."""

SAMPLE_RATE     = 16000
RECORD_SECONDS  = 5
SILENCE_TIMEOUT = 2.0

MAX_HISTORY = 10

VOSK_MODEL_URL  = "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"
VOSK_MODEL_DIR  = "vosk-model"
VOSK_MODEL_NAME = "vosk-model-small-en-us-0.15"