import random

from config import ALLOWED_LEVELS, ALLOWED_TEST_SIZES
from models.question_model import get_questions


def available_levels():
    return ALLOWED_LEVELS


def available_test_sizes():
    return ALLOWED_TEST_SIZES


def build_exam(level, amount):
    """
    指定レベルの100問から `amount` 問をランダムに選択します。

    手順:
    1. level と amount が有効かを確認します。
    2. DBからそのレベルの全100問を取得します。
    3. random.sample() で必要数をランダムに選びます。
    4. シャッフルされた問題リストを返します。
    """
    if level not in ALLOWED_LEVELS or amount not in ALLOWED_TEST_SIZES:
        return []

    # レベルの全問題を取得 (LIMITなし)
    all_questions = get_questions(level)

    if not all_questions:
        return []

    # 問題数が要求より少ない場合、全件をシャッフルして返します
    if len(all_questions) <= amount:
        return random.sample(all_questions, len(all_questions))

    # 100問から指定数をランダムに選択
    return random.sample(all_questions, amount)
