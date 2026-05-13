from sqlite3 import IntegrityError
from models.user_model import create_user, verify_user


# =========================
# ĐĂNG KÝ USER
# =========================
def register_user(name, email, password):
    try:
        # Gọi hàm tạo user mới trong database
        create_user(name, email, password)

        # Đăng ký thành công
        return True, "Đăng ký thành công. Hãy đăng nhập."
    except IntegrityError:
        # Lỗi này xảy ra khi email đã tồn tại (unique constraint)
        return False, "Email đã tồn tại."


# =========================
# ĐĂNG NHẬP USER
# =========================
def login_user(email, password):
    # Kiểm tra email + password trong database
    user = verify_user(email, password)

    # Nếu không tìm thấy user hợp lệ
    if not user:
        return None, "Email hoặc mật khẩu không đúng."

    # Đăng nhập thành công
    return user, "Đăng nhập thành công."