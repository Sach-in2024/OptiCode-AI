from database.db import DatabaseManager

db = DatabaseManager()

# BUG FIX: Added interview_optimal and theoretical_optimal
# to match the updated save_solution signature
db.save_solution(
    problem_statement="Two Sum",
    language="C++",
    topic="Array",
    pattern="Hash Map",
    difficulty="Easy",
    time_complexity="O(n)",
    space_complexity="O(n)",
    brute_force_code="Brute Code",
    optimal_code="Optimal Code",
    interview_optimal="Hash Map",
    theoretical_optimal="Hash Map"
)

history = db.get_history()

for row in history:
    print(row)
