# ==========================================================
# IMPORT HÀM DATABASE
# ==========================================================

# execute   : dùng cho INSERT / UPDATE / DELETE
# fetch_all : lấy nhiều dòng dữ liệu
# fetch_one : lấy 1 dòng dữ liệu

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

    # INSERT dữ liệu vào bảng questions
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

        # Dữ liệu truyền vào tương ứng với dấu ?
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

    # SQL cơ bản:
    # - lấy tất cả câu hỏi theo level
    # - RANDOM() để random đề mỗi lần làm bài

    query = """
        SELECT *
        FROM questions
        WHERE level = ?
        ORDER BY RANDOM()
    """

    # Danh sách parameter truyền vào SQL
    params = [level]

    # Nếu có giới hạn số câu
    # Ví dụ:
    # limit = 10
    # -> chỉ lấy 10 câu

    if limit:

        query += " LIMIT ?"

        params.append(limit)

    # Trả về nhiều dòng dữ liệu
    return fetch_all(

        query,

        tuple(params)

    )


# ==========================================================
# ĐẾM SỐ CÂU HỎI
# ==========================================================

def count_questions(level=None):

    # Nếu có truyền level
    # -> đếm theo cấp độ

    if level:

        return fetch_one(

            """
            SELECT COUNT(*) AS total
            FROM questions
            WHERE level = ?
            """,

            (level,)

        )["total"]

    # Nếu không truyền level
    # -> đếm toàn bộ câu hỏi

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