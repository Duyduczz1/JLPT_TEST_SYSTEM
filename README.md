# JLPT Test System (N1-N5)

Du an Flask de luyen thi JLPT voi dang nhap, dang ky, chon cap do N1-N5, lam bai 10-50 cau, cham diem, lich su va bang xep hang.

## Chay bang VS Code

```bash
cd C:\web_app\JLPT-TEST-SYSTEM_test01
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python database/create_db.py
python database/seed_questions.py
python app.py
```

Mo trinh duyet: http://127.0.0.1:5000

Tai khoan admin mac dinh:

- Email: admin@jlpt.local
- Mat khau: admin123

## Noi dung

- Flask routes cho auth, exam, result, history, ranking va admin.
- SQLite database voi users, questions, results.
- Du lieu mau cho N1-N5.
- Giao dien HTML/CSS/JS co timer lam bai.
