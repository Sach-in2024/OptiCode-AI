import sqlite3
from datetime import datetime

DB_NAME = "database/history.db"


class DatabaseManager:

    def __init__(self):
        self.conn = sqlite3.connect(
            DB_NAME,
            check_same_thread=False
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # BUG FIX: Removed trailing comma after last column (theoretical_optimal,)
        # which caused OperationalError: near ")" syntax error
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                problem_statement TEXT NOT NULL,
                language TEXT,
                topic TEXT,
                pattern TEXT,
                difficulty TEXT,
                time_complexity TEXT,
                space_complexity TEXT,
                brute_force_code TEXT,
                optimal_code TEXT,
                created_at TEXT,
                interview_optimal TEXT,
                theoretical_optimal TEXT
            )
            """
        )
        self.conn.commit()

    def save_solution(
        self,
        problem_statement,
        language,
        topic,
        pattern,
        difficulty,
        time_complexity,
        space_complexity,
        brute_force_code,
        optimal_code,
        interview_optimal="",
        theoretical_optimal=""
    ):
        # BUG FIX: Added interview_optimal and theoretical_optimal
        # to INSERT so all columns are populated
        self.cursor.execute(
            """
            INSERT INTO history (
                problem_statement,
                language,
                topic,
                pattern,
                difficulty,
                time_complexity,
                space_complexity,
                brute_force_code,
                optimal_code,
                created_at,
                interview_optimal,
                theoretical_optimal
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                problem_statement,
                language,
                topic,
                pattern,
                difficulty,
                time_complexity,
                space_complexity,
                brute_force_code,
                optimal_code,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                interview_optimal,
                theoretical_optimal
            )
        )
        self.conn.commit()

    def get_history(self):
        self.cursor.execute(
            "SELECT * FROM history ORDER BY id DESC"
        )
        return self.cursor.fetchall()

    def get_record(self, record_id):
        self.cursor.execute(
            "SELECT * FROM history WHERE id = ?",
            (record_id,)
        )
        return self.cursor.fetchone()

    def delete_record(self, record_id):
        self.cursor.execute(
            "DELETE FROM history WHERE id = ?",
            (record_id,)
        )
        self.conn.commit()

    def clear_history(self):
        self.cursor.execute("DELETE FROM history")
        self.conn.commit()

    def close(self):
        self.conn.close()
