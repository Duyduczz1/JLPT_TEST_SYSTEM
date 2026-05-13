import random

from config import ALLOWED_LEVELS, ALLOWED_TEST_SIZES
from models.question_model import get_questions


def available_levels():
    return ALLOWED_LEVELS


def available_test_sizes():
    return ALLOWED_TEST_SIZES


def build_exam(level, amount):
    """
    Lấy ngẫu nhiên `amount` câu hỏi từ kho 100 câu của cấp độ `level`.

    Quy trình:
    1. Kiểm tra level và amount hợp lệ.
    2. Lấy toàn bộ 100 câu của cấp độ từ DB.
    3. Dùng random.sample() để chọn ngẫu nhiên đúng số lượng yêu cầu.
    4. Trả về danh sách câu hỏi đã xáo trộn.
    """
    if level not in ALLOWED_LEVELS or amount not in ALLOWED_TEST_SIZES:
        return []

    # Lấy toàn bộ câu hỏi của cấp độ (không giới hạn LIMIT)
    all_questions = get_questions(level)

    if not all_questions:
        return []

    # Nếu kho câu hỏi ít hơn yêu cầu, trả về tất cả (đã xáo trộn)
    if len(all_questions) <= amount:
        return random.sample(all_questions, len(all_questions))

    # Lấy ngẫu nhiên đúng số lượng câu từ kho 100 câu
    return random.sample(all_questions, amount)
