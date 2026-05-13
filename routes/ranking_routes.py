from flask import Blueprint, render_template, request
from routes.auth_routes import login_required
from services.exam_service import available_levels
from services.ranking_service import get_rankings

ranking_bp = Blueprint("ranking", __name__, url_prefix="/ranking")


@ranking_bp.route("/")
@login_required
def ranking():
    level = request.args.get("level") or None
    return render_template("ranking.html", rankings=get_rankings(level), levels=available_levels(), selected_level=level)
