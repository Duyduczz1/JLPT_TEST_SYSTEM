# ==========================================================
# IMPORT THƯ VIỆN
# ==========================================================

# Blueprint:
# Dùng để chia route thành từng module riêng
#
# flash:
# Hiển thị thông báo tạm thời
#
# redirect:
# Chuyển hướng sang route khác
#
# render_template:
# Render file HTML
#
# url_for:
# Tạo URL động
from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    url_for
)

# ==========================================================
# IMPORT DECORATOR KIỂM TRA ĐĂNG NHẬP
# ==========================================================

# login_required:
# Bắt buộc người dùng phải đăng nhập
from routes.auth_routes import login_required

# ==========================================================
# IMPORT CÁC HÀM XỬ LÝ ĐỀ THI
# ==========================================================

from services.exam_service import (

    # JLPT レベル一覧を取得
    available_levels,

    # 問題数一覧を取得
    available_test_sizes,

    # 試験を作成
    build_exam

)

# ==========================================================
# TẠO BLUEPRINT CHO PHẦN THI
# ==========================================================

# __name__:
# Tên module hiện tại
#
# url_prefix="/exam":
# Tất cả route sẽ bắt đầu bằng /exam
#
# Ví dụ:
# /exam/levels
# /exam/N5/tests
exam_bp = Blueprint(
    "exam",
    __name__,
    url_prefix="/exam"
)

# ==========================================================
# ROUTE:
# HIỂN THỊ DANH SÁCH CẤP ĐỘ JLPT
# ==========================================================

@exam_bp.route("/levels")

# Bắt buộc đăng nhập
@login_required
def levels():

    # Render trang levels.html
    return render_template(

        "levels.html",

        # Truyền danh sách cấp độ
        levels=available_levels()

    )

# ==========================================================
# ROUTE:
# HIỂN THỊ DANH SÁCH SỐ CÂU HỎI
# ==========================================================

@exam_bp.route("/<level>/tests")

# Bắt buộc đăng nhập
@login_required
def tests(level):

    # Render trang tests.html
    return render_template(

        "tests.html",

        # Cấp độ JLPT hiện tại
        level=level,

        # Danh sách số lượng câu
        sizes=available_test_sizes()

    )

# ==========================================================
# ROUTE:
# HIỂN THỊ BÀI THI
# ==========================================================

@exam_bp.route("/<level>/<int:amount>")

# Bắt buộc đăng nhập
@login_required
def exam(level, amount):

    # ======================================================
    # TẠO DANH SÁCH CÂU HỎI
    # ======================================================

    questions = build_exam(level, amount)

    # ======================================================
    # 問題があるかどうかをチェック
    # ======================================================

    if not questions:

        # 警告メッセージを表示
        flash(

            "適切な問題が見つかりませんでした。",

            "warning"
        )

        # Quay về trang chọn cấp độ
        return redirect(

            url_for("exam.levels")

        )

    # ======================================================
    # HIỂN THỊ TRANG THI
    # ======================================================

    return render_template(

        "exam.html",

        # Cấp độ JLPT
        level=level,

        # 問題数
        amount=amount,

        # Danh sách câu hỏi
        questions=questions

    )