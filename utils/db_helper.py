import sqlite3
from config import DATABASE


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def fetch_one(query, params=()):
    with get_connection() as conn:
        return conn.execute(query, params).fetchone()


def fetch_all(query, params=()):
    with get_connection() as conn:
        return conn.execute(query, params).fetchall()


def execute(query, params=()):
    with get_connection() as conn:
        cur = conn.execute(query, params)
        conn.commit()
        return cur.lastrowid
