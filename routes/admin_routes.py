from flask import Blueprint, render_template
from models.question_model import count_questions, list_questions
from models.ranking_model import top_scores
from models.user_model import list_users
from routes.auth_routes import admin_required

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/")
@admin_required
def dashboard():
    return render_template("admin/admin_dashboard.html", total_questions=count_questions(), users=list_users()[:5], top=top_scores(limit=5))


@admin_bp.route("/questions")
@admin_required
def manage_questions():
    return render_template("admin/manage_questions.html", questions=list_questions())


@admin_bp.route("/users")
@admin_required
def manage_users():
    return render_template("admin/manage_users.html", users=list_users())


@admin_bp.route("/statistics")
@admin_required
def statistics():
    return render_template("admin/statistics.html", total_questions=count_questions(), top=top_scores(limit=10))
