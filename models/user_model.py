from werkzeug.security import check_password_hash, generate_password_hash
from utils.db_helper import execute, fetch_all, fetch_one


def create_user(name, email, password, role="user"):
    return execute(
        "INSERT INTO users (name, email, password_hash, role) VALUES (?, ?, ?, ?)",
        (name, email, generate_password_hash(password), role),
    )


def get_user_by_email(email):
    return fetch_one("SELECT * FROM users WHERE email = ?", (email,))


def get_user_by_id(user_id):
    return fetch_one("SELECT * FROM users WHERE id = ?", (user_id,))


def verify_user(email, password):
    user = get_user_by_email(email)
    if user and check_password_hash(user["password_hash"], password):
        return user
    return None


def list_users():
    return fetch_all("SELECT id, name, email, role, created_at FROM users ORDER BY created_at DESC")
