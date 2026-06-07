from services.gemini_service import GeminiService
from services.prompts import OPTIMAL_PROMPT


class OptimalAgent:

    @staticmethod
    def generate(problem: str, language: str) -> dict:

        prompt = OPTIMAL_PROMPT.format(
            problem=problem,
            language=language
        )

        response = GeminiService.generate_response(prompt)

        result = {
            "interview_optimal": "",
            "theoretical_optimal": "",
            "code": "",
            "explanation": ""
        }

        current_section = None

        for line in response.split("\n"):

            line = line.rstrip()

            if not line:
                continue

            if line.startswith("INTERVIEW_OPTIMAL:"):

                current_section = "interview_optimal"

                value = line.replace(
                    "INTERVIEW_OPTIMAL:",
                    ""
                ).strip()

                if value:
                    result["interview_optimal"] = value

                continue

            elif line.startswith("THEORETICAL_OPTIMAL:"):

                current_section = "theoretical_optimal"

                value = line.replace(
                    "THEORETICAL_OPTIMAL:",
                    ""
                ).strip()

                if value:
                    result["theoretical_optimal"] = value

                continue

            elif line.startswith("CODE:"):

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

        return {
            key: value.strip()
            for key, value in result.items()
        }