from services.gemini_service import GeminiService
from services.prompts import COMPLEXITY_PROMPT


class ComplexityAgent:
    """
    Analyze Time and Space Complexity
    of the optimal solution.
    """

    @staticmethod
    def analyze(problem: str, optimal_code: str) -> dict:

        prompt = COMPLEXITY_PROMPT.format(
            problem=problem,
            optimal_code=optimal_code
        )

        response = GeminiService.generate_response(prompt)

        result = {
            "time_complexity": "",
            "space_complexity": ""
        }

        current_section = None

        for line in response.split("\n"):

            line = line.strip()

            if not line:
                continue

            if line.startswith("TIME_COMPLEXITY:"):

                current_section = "time_complexity"

                value = line.replace(
                    "TIME_COMPLEXITY:",
                    ""
                ).strip()

                if value:
                    result["time_complexity"] = value

                continue

            elif line.startswith("SPACE_COMPLEXITY:"):

                current_section = "space_complexity"

                value = line.replace(
                    "SPACE_COMPLEXITY:",
                    ""
                ).strip()

                if value:
                    result["space_complexity"] = value

                continue

            if current_section:
                result[current_section] += line + " "

        result = {
            key: value.strip()
            for key, value in result.items()
        }

        for key in result:
            if not result[key]:
                result[key] = "Unknown"

        return result