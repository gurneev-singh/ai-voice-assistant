# main.py
import time
import sys
import config
from voice_input import VoiceInput
from ai_brain    import AIBrain
from speaker     import Speaker


def main():
    print("=" * 50)
    print(f"  🤖  {config.ASSISTANT_NAME} — AI Voice Assistant")
    print("=" * 50)
    print(f"  Wake word : '{config.WAKE_WORD}'")
    print(f"  Model     : {config.GROQ_MODEL}")
    print(f"  Say '{config.WAKE_WORD} goodbye' to quit")
    print("=" * 50 + "\n")

    speaker = Speaker()
    brain   = AIBrain()
    voice   = VoiceInput()

    greeting = f"Hi! I'm {config.ASSISTANT_NAME}, your AI assistant. Say '{config.WAKE_WORD}' to talk to me."
    speaker.say(greeting)
    speaker.wait_until_done()

    try:
        while True:
            detected = voice.listen_for_wake_word()
            if not detected:
                continue

            print(f"\n[MAIN] ✅ Wake word detected!")
            speaker.say("Yes?")
            speaker.wait_until_done()

            question = voice.record_question()

            if not question:
                speaker.say("I didn't hear anything. Say my name to try again.")
                speaker.wait_until_done()
                continue

            if any(word in question.lower() for word in ["goodbye", "bye", "quit", "exit", "stop"]):
                speaker.say("Goodbye! Have a great day!")
                speaker.wait_until_done()
                break

            if "forget everything" in question.lower() or "clear memory" in question.lower():
                brain.clear_history()
                speaker.say("Done. I've forgotten our conversation.")
                speaker.wait_until_done()
                continue

            print(f"[MAIN] 🧠 Thinking...")
            response = brain.think(question)
            speaker.say(response)
            speaker.wait_until_done()

            print(f"\n--- Ready. Say '{config.WAKE_WORD}' again ---\n")

    except KeyboardInterrupt:
        print("\n[MAIN] Shutting down.")
        speaker.say("Goodbye!")
        speaker.wait_until_done()

    finally:
        speaker.stop()
        print("[MAIN] Done.")


if __name__ == "__main__":
    main()