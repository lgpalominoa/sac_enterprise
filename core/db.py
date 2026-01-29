import sqlite3
from contextlib import contextmanager

DB_NAME = "sac_enterprise.db"

@contextmanager
def get_db():
    conn = sqlite3.connect(DB_NAME)
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()
