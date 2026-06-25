
# ==========================================================
# IMPORT THƯ VIỆN
# ==========================================================

# wraps:
# Giữ nguyên tên và thông tin hàm gốc
from functools import wraps

# Blueprint:
# Tạo nhóm route riêng
#
# flash:
# Hiển thị thông báo
#
# redirect:
# Chuyển hướng trang
#
# render_template:
# Render file HTML
#
# request:
# フォームデータを取得
#
# session:
# ログイン状態を保存
#
# url_for:
# Tạo URL động
from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for
)

# ==========================================================
# IMPORT MODEL USER
# ==========================================================

# Lấy user theo ID
from models.user_model import get_user_by_id

# ==========================================================
# IMPORT SERVICE XỬ LÝ ĐĂNG NHẬP / ĐĂNG KÝ
# ==========================================================

from services.auth_service import (

    # ログインを処理する
    login_user,

    # 登録を処理する
    register_user

)

# ==========================================================
# TẠO BLUEPRINT CHO AUTH
# ==========================================================

auth_bp = Blueprint(

    "auth",

    __name__

)

# ==========================================================
# HÀM:
# 現在のユーザー情報を取得
# ==========================================================

def current_user():

    # セッションから user_id を取得
    user_id = session.get("user_id")

    # user_id があればユーザーを取得
    return get_user_by_id(user_id) if user_id else None

# ==========================================================
# DECORATOR:
# ログインチェック
# ==========================================================

def login_required(view):

    @wraps(view)

    def wrapped(*args, **kwargs):

        # ログインしていない場合
        if not session.get("user_id"):

            # メッセージを表示
            flash(

                "先にログインしてください。",

                "warning"

            )

            # ログインページへリダイレクト
            return redirect(

                url_for("auth.login")

            )

        # ログイン済みの場合
        return view(*args, **kwargs)

    return wrapped

# ==========================================================
# DECORATOR:
# KIỂM TRA QUYỀN ADMIN
# ==========================================================

def admin_required(view):

    @wraps(view)

    def wrapped(*args, **kwargs):

        # Lấy user hiện tại
        user = current_user()

        # 管理者でない場合
        if not user or user["role"] != "admin":

            # メッセージを表示
            flash(

                "管理者ページにアクセスする権限がありません。",

                "danger"

            )

            # Chuyển về dashboard
            return redirect(

                url_for("dashboard")

            )

        # Nếu là admin
        return view(*args, **kwargs)

    return wrapped

# ==========================================================
# ROUTE:
# ĐĂNG KÝ TÀI KHOẢN
# ==========================================================

@auth_bp.route(

    "/register",

    methods=["GET", "POST"]

)
def register():

    # ======================================================
    # NẾU USER NHẤN ĐĂNG KÝ
    # ======================================================

    if request.method == "POST":

        # Gọi service đăng ký
        ok, message = register_user(

            request.form["name"],

            request.form["email"],

            request.form["password"]

        )

        # Hiển thị thông báo
        flash(

            message,

            "success" if ok else "danger"

        )

        # Nếu thành công -> chuyển login
        # Nếu thất bại -> quay lại register
        return redirect(

            url_for(

                "auth.login" if ok else "auth.register"

            )

        )

    # ======================================================
    # HIỂN THỊ TRANG ĐĂNG KÝ
    # ======================================================

    return render_template(

        "register.html"

    )

# ==========================================================
# ROUTE:
# ĐĂNG NHẬP
# ==========================================================

@auth_bp.route(

    "/login",

    methods=["GET", "POST"]

)
def login():

    # ======================================================
    # NẾU USER NHẤN ĐĂNG NHẬP
    # ======================================================

    if request.method == "POST":

        # Kiểm tra tài khoản
        user, message = login_user(

            request.form["email"],

            request.form["password"]

        )

        # ==================================================
        # NẾU ĐĂNG NHẬP THÀNH CÔNG
        # ==================================================

        if user:

            # Lưu ID user vào session
            session["user_id"] = user["id"]

            # Lưu tên user
            session["user_name"] = user["name"]

            # Lưu role
            session["role"] = user["role"]

            # Chuyển tới dashboard
            return redirect(

                url_for("dashboard")

            )

        # ==================================================
        # NẾU ĐĂNG NHẬP THẤT BẠI
        # ==================================================

        flash(

            message,

            "danger"

        )

    # ======================================================
    # HIỂN THỊ TRANG LOGIN
    # ======================================================

    return render_template(

        "login.html"

    )

# ==========================================================
# ROUTE:
# ĐĂNG XUẤT
# ==========================================================

@auth_bp.route("/logout")
def logout():

    # Xóa toàn bộ session
    session.clear()

    # 情報メッセージを表示
    flash(

        "ログアウトしました。",

        "info"

    )

    # Quay về trang chủ
    return redirect(

        url_for("index")

    )

