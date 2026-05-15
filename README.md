# JLPT Test System (N1-N5)

Dự án Flask để luyện thi JLPT với đăng nhập, đăng ký, chọn cấp độ N1–N5, làm bài 10–50 câu, chấm điểm, lịch sử và bảng xếp hạng.

## Chạy bằng VS Code

```bash

cd C:\web_app\JLPT-TEST-WEB
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python database/create_db.py
python database/seed_questions.py
python app.py

```

Mở trình duyệt: http://127.0.0.1:5000

https://jlpt-test-system.onrender.com
Tài khoản admin mặc định:

- Email: admin@jlpt.local
- Mật khẩu: Duyduc1112

Nội dung
Flask routes cho auth, exam, result, history, ranking và admin.
SQLite database với users, questions, results.
Dữ liệu mẫu cho N1–N5.
Giao diện HTML/CSS/JS có timer làm bài.
