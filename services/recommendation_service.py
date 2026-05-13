# =========================
# GỢI Ý DỰA TRÊN ĐIỂM SỐ
# =========================
def recommendation(score):
    # Nếu điểm >= 85: mức tốt, có thể nâng level
    if score >= 85:
        return "Rất tốt! Bạn có thể thử cấp độ cao hơn hoặc tăng số câu hỏi."

    # Nếu điểm >= 60: đạt yêu cầu qua môn
    if score >= 60:
        return "Bạn đã đạt mức qua môn. Hãy ôn thêm từ vựng và ngữ pháp để chắc hơn."

    # Nếu điểm < 60: cần ôn lại cơ bản
    return "Nên ôn lại kiến thức cơ bản và làm các đề ngắn 10-20 câu trước."