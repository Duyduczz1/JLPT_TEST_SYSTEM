from flask import Blueprint, render_template, session
from models.history_model import user_history
from routes.auth_routes import login_required

history_bp = Blueprint("history", __name__, url_prefix="/history")


@history_bp.route("/")
@login_required
def history():
    return render_template("history.html", results=user_history(session["user_id"]))
