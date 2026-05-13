
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
# Lấy dữ liệu form
#
# session:
# Lưu trạng thái đăng nhập
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

    # Xử lý đăng nhập
    login_user,

    # Xử lý đăng ký
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
# LẤY THÔNG TIN USER HIỆN TẠI
# ==========================================================

def current_user():

    # Lấy user_id trong session
    user_id = session.get("user_id")

    # Nếu có user_id thì lấy user
    return get_user_by_id(user_id) if user_id else None

# ==========================================================
# DECORATOR:
# KIỂM TRA ĐĂNG NHẬP
# ==========================================================

def login_required(view):

    @wraps(view)

    def wrapped(*args, **kwargs):

        # Nếu chưa đăng nhập
        if not session.get("user_id"):

            # Hiển thị thông báo
            flash(

                "Vui lòng đăng nhập trước.",

                "warning"

            )

            # Chuyển về trang login
            return redirect(

                url_for("auth.login")

            )

        # Nếu đã đăng nhập
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

        # Nếu không phải admin
        if not user or user["role"] != "admin":

            # Hiển thị thông báo
            flash(

                "Bạn không có quyền truy cập trang admin.",

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

    # Hiển thị thông báo
    flash(

        "Đã đăng xuất.",

        "info"

    )

    # Quay về trang chủ
    return redirect(

        url_for("index")

    )

