from utils.db_helper import execute, fetch_all, fetch_one


def create_result(user_id, level, total_questions, correct_answers, score):
    return execute(
        """
        INSERT INTO results (user_id, level, total_questions, correct_answers, score)
        VALUES (?, ?, ?, ?, ?)
        """,
        (user_id, level, total_questions, correct_answers, score),
    )


def get_result(result_id):
    return fetch_one(
        """
        SELECT r.*, u.name AS user_name
        FROM results r JOIN users u ON u.id = r.user_id
        WHERE r.id = ?
        """,
        (result_id,),
    )


def get_results_by_user(user_id):
    return fetch_all("SELECT * FROM results WHERE user_id = ? ORDER BY created_at DESC", (user_id,))
