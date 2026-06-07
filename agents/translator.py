from services.gemini_service import GeminiService
from services.prompts import TRANSLATOR_PROMPT
from utils.helpers import clean_code


class TranslatorAgent:
    """
    Translate code from one programming
    language to another.
    """

    @staticmethod
    def translate(code: str, language: str) -> dict:

        try:

            prompt = TRANSLATOR_PROMPT.format(
                code=code,
                language=language
            )

            response = GeminiService.generate_response(
                prompt
            )

            translated_code = clean_code(
                response
            )

            return {
                "success": True,
                "language": language,
                "translated_code": translated_code
            }

        except Exception as e:

            return {
                "success": False,
                "language": language,
                "translated_code": "",
                "error": str(e)
            }