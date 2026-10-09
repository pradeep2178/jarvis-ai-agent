from openai import OpenAI

from .config import OPENAI_API_KEY, OPENAI_MODEL


class AIClient:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

    def respond(self, user_prompt: str) -> str:
        if not self.client:
            return (
                "I am running in offline mode because no OpenAI API key was found. "
                "Try commands like 'what time is it', 'open notepad', or 'search for Python tutorials.'"
            )

        try:
            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are Jarvis, an advanced AI assistant inspired by Iron Man. "
                            "Speak confidently, politely, and concisely. Respond in a helpful, "
                            "friendly tone."
                        ),
                    },
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.7,
                max_tokens=250,
            )
            return response.choices[0].message.content.strip()
        except Exception as exc:  # pragma: no cover - runtime failure path
            return f"I hit an AI service error: {exc}"
