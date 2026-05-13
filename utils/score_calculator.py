def calculate_score(total, correct):
    if total <= 0:
        return 0
    return round((correct / total) * 100, 2)


def passed(score):
    return score >= 60
