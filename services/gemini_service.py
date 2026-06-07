import os
from groq import Groq
from dotenv import load_dotenv


MODEL_NAME = "llama-3.3-70b-versatile"


class GeminiService:
    """
    Handles all Groq API interactions.
    Replaces Gemini with Groq's LLaMA model.
    """

    _client = None

    @classmethod
    def _get_client(cls):
        if cls._client is None:
            load_dotenv()
            api_key = os.getenv("GROQ_API_KEY")
            if not api_key:
                raise ValueError(
                    "GROQ_API_KEY not found. "
                    "Please add it to your .env file."
                )
            cls._client = Groq(api_key=api_key)
        return cls._client

    @staticmethod
    def generate_response(prompt: str) -> str:
        try:
            client = GeminiService._get_client()

            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=4096,
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            return f"Groq Error: {str(e)}"

    @staticmethod
    def health_check() -> bool:
        try:
            client = GeminiService._get_client()
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": "Reply with only: OK"}],
                max_tokens=10,
            )
            return "OK" in response.choices[0].message.content
        except Exception:
            return False
