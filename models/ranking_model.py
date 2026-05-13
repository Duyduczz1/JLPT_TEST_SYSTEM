from utils.db_helper import fetch_all


def top_scores(level=None, limit=20):
    query = """
        SELECT u.name, r.level, r.score, r.correct_answers, r.total_questions, r.created_at
        FROM results r JOIN users u ON u.id = r.user_id
    """
    params = []
    if level:
        query += " WHERE r.level = ?"
        params.append(level)
    query += " ORDER BY r.score DESC, r.correct_answers DESC, r.created_at ASC LIMIT ?"
    params.append(limit)
    return fetch_all(query, tuple(params))
