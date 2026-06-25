# ==========================================================
# IMPORT HÀM DATABASE
# ==========================================================

# execute   : INSERT / UPDATE / DELETE 用
# fetch_all : 複数行データ取得用
# fetch_one : 1行データ取得用

from utils.db_helper import execute, fetch_all, fetch_one


# ==========================================================
# THÊM CÂU HỎI MỚI
# ==========================================================

def create_question(
    level,
    question,
    option_a,
    option_b,
    option_c,
    option_d,
    answer,
    explanation=""
):

    # questionsテーブルにデータをINSERT
    return execute(

        """
        INSERT INTO questions (
            level,
            question,
            option_a,
            option_b,
            option_c,
            option_d,
            answer,
            explanation
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,

        # ? に対応するパラメータ
        (
            level,
            question,
            option_a,
            option_b,
            option_c,
            option_d,
            answer,
            explanation
        ),
    )


# ==========================================================
# LẤY DANH SÁCH CÂU HỎI THEO CẤP ĐỘ
# ==========================================================

def get_questions(level, limit=None):

    # SQL 基本:
    # - level による全問題取得
    # - RANDOM() で毎回異なる出題順にする

    query = """
        SELECT *
        FROM questions
        WHERE level = ?
        ORDER BY RANDOM()
    """

    # Danh sách parameter truyền vào SQL
    params = [level]

    # limit がある場合
    # 例:
    # limit = 10
    # -> 10問のみ取得

    if limit:

        query += " LIMIT ?"

        params.append(limit)

    # 複数行データを返す
    return fetch_all(

        query,

        tuple(params)

    )


# ==========================================================
# ĐẾM SỐ CÂU HỎI
# ==========================================================

def count_questions(level=None):

    # level が渡された場合
    # -> レベル別の件数をカウント

    if level:

        return fetch_one(

            """
            SELECT COUNT(*) AS total
            FROM questions
            WHERE level = ?
            """,

            (level,)

        )["total"]

    # level が渡されない場合
    # -> 全問題数をカウント

    return fetch_one(

        """
        SELECT COUNT(*) AS total
        FROM questions
        """

    )["total"]


# ==========================================================
# LẤY TOÀN BỘ DANH SÁCH CÂU HỎI
# ==========================================================

def list_questions():

    # ORDER BY:
    # - level : sắp xếp theo N1 -> N5
    # - id DESC : câu mới nhất lên đầu

    return fetch_all(

        """
        SELECT *
        FROM questions
        ORDER BY level, id DESC
        """

    )