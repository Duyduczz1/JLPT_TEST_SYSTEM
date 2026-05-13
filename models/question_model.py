from utils.db_helper import execute, fetch_all, fetch_one


def create_question(level, question, option_a, option_b, option_c, option_d, answer, explanation=""):
    return execute(
        """
        INSERT INTO questions (level, question, option_a, option_b, option_c, option_d, answer, explanation)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (level, question, option_a, option_b, option_c, option_d, answer, explanation),
    )


def get_questions(level, limit=None):
    query = "SELECT * FROM questions WHERE level = ? ORDER BY RANDOM()"
    params = [level]
    if limit:
        query += " LIMIT ?"
        params.append(limit)
    return fetch_all(query, tuple(params))


def count_questions(level=None):
    if level:
        return fetch_one("SELECT COUNT(*) AS total FROM questions WHERE level = ?", (level,))["total"]
    return fetch_one("SELECT COUNT(*) AS total FROM questions")["total"]


def list_questions():
    return fetch_all("SELECT * FROM questions ORDER BY level, id DESC")
