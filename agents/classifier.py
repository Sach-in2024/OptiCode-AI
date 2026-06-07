from services.gemini_service import GeminiService
from services.prompts import CLASSIFIER_PROMPT


class ClassifierAgent:
    """
    Detects:
    - Topic
    - Pattern
    - Difficulty
    """

    @staticmethod
    def classify(problem: str) -> dict:

        prompt = CLASSIFIER_PROMPT.format(
            problem=problem
        )

        response = GeminiService.generate_response(prompt)

        result = {
            "topic": "",
            "pattern": "",
            "difficulty": ""
        }

        current_section = None

        for line in response.split("\n"):

            line = line.strip()

            if not line:
                continue

            if line.startswith("TOPIC:"):
                current_section = "topic"

                value = line.replace(
                    "TOPIC:", ""
                ).strip()

                if value:
                    result["topic"] = value

                continue

            elif line.startswith("PATTERN:"):
                current_section = "pattern"

                value = line.replace(
                    "PATTERN:", ""
                ).strip()

                if value:
                    result["pattern"] = value

                continue

            elif line.startswith("DIFFICULTY:"):
                current_section = "difficulty"

                value = line.replace(
                    "DIFFICULTY:", ""
                ).strip()

                if value:
                    result["difficulty"] = value

                continue

            if current_section:
                result[current_section] += line + " "

        result = {
            key: value.strip()
            for key, value in result.items()
        }

        return result