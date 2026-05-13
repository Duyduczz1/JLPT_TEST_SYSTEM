from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "database" / "jlpt.db"
SECRET_KEY = "change-this-secret-key"
UPLOAD_FOLDER = BASE_DIR / "uploads" / "avatars"
ALLOWED_LEVELS = ["N5", "N4", "N3", "N2", "N1"]
ALLOWED_TEST_SIZES = [10, 20, 30, 40, 50]
