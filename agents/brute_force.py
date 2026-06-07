from services.gemini_service import GeminiService
from services.prompts import BRUTE_FORCE_PROMPT


class BruteForceAgent:
    """
    Generates brute force solution
    for a DSA problem.
    """

    @staticmethod
    def generate(problem: str, language: str) -> dict:

        prompt = BRUTE_FORCE_PROMPT.format(
            problem=problem,
            language=language
        )

        response = GeminiService.generate_response(prompt)

        result = {
            "code": "",
            "explanation": ""
        }

        current_section = None

        for line in response.split("\n"):

            line = line.rstrip()

            if not line:
                continue

            if line.startswith("CODE:"):
                current_section = "code"

                value = line.replace(
                    "CODE:",
                    ""
                ).strip()

                if value:
                    result["code"] += value + "\n"

                continue

            elif line.startswith("EXPLANATION:"):
                current_section = "explanation"

                value = line.replace(
                    "EXPLANATION:",
                    ""
                ).strip()

                if value:
                    result["explanation"] += value + "\n"

                continue

            if current_section:
                result[current_section] += line + "\n"

        result["code"] = result["code"].strip()

        result["explanation"] = result[
            "explanation"
        ].strip()

        return result