from services.gemini_service import GeminiService
from services.prompts import REVIEW_PROMPT


class ReviewerAgent:
    """
    Reviews generated optimal solution
    and checks whether a better algorithm exists.
    """

    @staticmethod
    def review(problem: str, code: str) -> dict:

        prompt = REVIEW_PROMPT.format(
            problem=problem,
            code=code
        )

        response = GeminiService.generate_response(
            prompt
        )

        result = {
            "is_optimal": "",
            "better_algorithm": "",
            "reason": ""
        }

        current_section = None

        for line in response.split("\n"):

            line = line.strip()

            if not line:
                continue

            if line.startswith("IS_OPTIMAL:"):

                current_section = "is_optimal"

                value = line.replace(
                    "IS_OPTIMAL:",
                    ""
                ).strip()

                if value:
                    result["is_optimal"] = value

                continue

            elif line.startswith("BETTER_ALGORITHM:"):

                current_section = "better_algorithm"

                value = line.replace(
                    "BETTER_ALGORITHM:",
                    ""
                ).strip()

                if value:
                    result["better_algorithm"] = value

                continue

            elif line.startswith("REASON:"):

                current_section = "reason"

                value = line.replace(
                    "REASON:",
                    ""
                ).strip()

                if value:
                    result["reason"] = value

                continue

            if current_section:
                result[current_section] += " " + line

        return {
            key: value.strip()
            for key, value in result.items()
        }