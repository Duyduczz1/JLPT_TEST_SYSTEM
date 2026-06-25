from sqlite3 import IntegrityError
from models.user_model import create_user, verify_user


# =========================
# ユーザー登録
# =========================
def register_user(name, email, password):
    try:
        # Gọi hàm tạo user mới trong database
        create_user(name, email, password)

        # 登録成功
        return True, "登録が完了しました。ログインしてください。"
    except IntegrityError:
        # このエラーはメールアドレスが既に存在する場合に発生します（unique constraint）
        return False, "メールアドレスは既に登録されています。"


# =========================
# ユーザーログイン
# =========================
def login_user(email, password):
    # Kiểm tra email + password trong database
    user = verify_user(email, password)

    # 有効なユーザーが見つからない場合
    if not user:
        return None, "メールアドレスまたはパスワードが正しくありません。"

    # ログイン成功
    return user, "ログインに成功しました。"