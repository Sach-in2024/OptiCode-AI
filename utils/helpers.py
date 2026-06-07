import re


def clean_code(code: str) -> str:
    """
    Remove markdown code blocks if Gemini
    accidentally generates them.
    """

    code = re.sub(r"```[a-zA-Z]*", "", code)
    code = code.replace("```", "")

    return code.strip()


def get_file_extension(language: str) -> str:
    """
    Return file extension for download.
    """

    mapping = {
        "Python": "py",
        "C++": "cpp",
        "C": "c",
        "Java": "java",
        "JavaScript": "js",
        "Go": "go",
        "Rust": "rs"
    }

    return mapping.get(language, "txt")


def generate_filename(
    language: str,
    solution_type: str
) -> str:
    """
    Generate downloadable filename.
    """

    extension = get_file_extension(language)

    return f"{solution_type.lower()}_solution.{extension}"


def format_complexity(
    complexity: str
) -> str:
    """
    Clean complexity text.
    """

    return complexity.strip()


SUPPORTED_LANGUAGES = [
    "Python",
    "C++",
    "C",
    "Java",
    "JavaScript",
    "Go",
    "Rust"
]