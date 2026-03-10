# ai_brain.py
# ──────────────────────────────────────────────────────────────
# Sends user messages to Groq and returns AI responses.
# Maintains conversation history so the assistant remembers
# what was said earlier in the conversation.
# ──────────────────────────────────────────────────────────────

from groq import Groq
import config


class AIBrain:
    def __init__(self):
        self.client  = Groq(api_key=config.GROQ_API_KEY)
        self.history = []   # conversation memory
        print(f"[BRAIN] {config.ASSISTANT_NAME} AI brain ready.")

    def think(self, user_message: str) -> str:
        """
        Send a message and get a response.
        Automatically maintains conversation history.
        """
        # Add user message to history
        self.history.append({
            "role"   : "user",
            "content": user_message,
        })

        # Keep history within limit (trim oldest messages)
        if len(self.history) > config.MAX_HISTORY:
            self.history = self.history[-config.MAX_HISTORY:]

        try:
            response = self.client.chat.completions.create(
                model    = config.GROQ_MODEL,
                messages = [
                    {"role": "system", "content": config.SYSTEM_PROMPT},
                    *self.history,
                ],
                max_tokens  = 200,   # short responses for voice
                temperature = 0.7,
            )

            reply = response.choices[0].message.content.strip()

            # Add assistant reply to history
            self.history.append({
                "role"   : "assistant",
                "content": reply,
            })

            return reply

        except Exception as e:
            err = str(e)
            if "429" in err:
                return "I'm rate limited right now. Please wait a moment and try again."
            if "401" in err:
                return "My API key seems invalid. Please check the config file."
            return f"Sorry, I encountered an error: {err[:60]}"

    def clear_memory(self):
        """Forget the conversation history."""
        self.history = []
        print("[BRAIN] Memory cleared.")