import sqlite3
from contextlib import contextmanager

DATABASE_FILE = "./database/db.db"

@contextmanager
def get_connection():
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()
        yield connection, cursor
    except Exception as e:
        raise Exception(f"Database connection error: {e}")
    finally:
        connection.commit()
        connection.close()