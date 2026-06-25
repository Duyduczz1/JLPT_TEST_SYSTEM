# =========================
# スコアに基づく推薦
# =========================
def recommendation(score):
    # Nếu điểm >= 85: mức tốt, có thể nâng level
    if score >= 85:
        return "とても良い成績です！上のレベルや問題数を増やしてみましょう。"

    # Nếu điểm >= 60: đạt yêu cầu qua môn
    if score >= 60:
        return "合格ラインに達しています。語彙や文法をさらに復習しましょう。"

    # Nếu điểm < 60: cần ôn lại cơ bản
    return "基礎を復習し、まずは10〜20問の問題から始めましょう。"