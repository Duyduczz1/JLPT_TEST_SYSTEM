from models.question_model import get_questions
from models.result_model import create_result
from utils.score_calculator import calculate_score


def score_exam(user_id, level, submitted_answers):
    question_ids = [int(qid) for qid in submitted_answers.keys()]
    all_questions = get_questions(level)
    questions = [q for q in all_questions if q["id"] in question_ids]
    correct = 0
    details = []

    for question in questions:
        selected = submitted_answers.get(str(question["id"]), "")
        is_correct = selected == question["answer"]
        correct += 1 if is_correct else 0
        details.append({"question": question, "selected": selected, "is_correct": is_correct})

    total = len(questions)
    score = calculate_score(total, correct)
    result_id = create_result(user_id, level, total, correct, score)
    return result_id, details
