from flask import Blueprint, redirect, render_template, request, session, url_for
from models.result_model import get_result
from routes.auth_routes import login_required
from services.recommendation_service import recommendation
from services.scoring_service import score_exam

result_bp = Blueprint("result", __name__, url_prefix="/result")


@result_bp.route("/submit/<level>", methods=["POST"])
@login_required
def submit(level):
    answers = {key.replace("answer_", ""): value for key, value in request.form.items() if key.startswith("answer_")}
    result_id, details = score_exam(session["user_id"], level, answers)
    session["last_details"] = [
        {
            "question": d["question"]["question"],
            "selected": d["selected"],
            "answer": d["question"]["answer"],
            "is_correct": d["is_correct"],
            "explanation": d["question"]["explanation"],
        }
        for d in details
    ]
    return redirect(url_for("result.show", result_id=result_id))


@result_bp.route("/<int:result_id>")
@login_required
def show(result_id):
    result = get_result(result_id)
    details = session.pop("last_details", [])
    return render_template("result.html", result=result, details=details, recommendation=recommendation(result["score"]))
