from contextlib import contextmanager
import sqlite3

from ...utils import fs

@contextmanager
def db_session():
    """Context manager for database sessions."""
    conn = sqlite3.connect(fs.get_primary_db_path())
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    finally:
        conn.close()

def initialize_db():
    with db_session() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                uuid TEXT NOT NULL,
                type TEXT NOT NULL,
                status TEXT NOT NULL,
                metadata TEXT,
                description TEXT
            )
        ''')

        conn.execute('''
            CREATE INDEX IF NOT EXISTS idx_tasks_uuid ON tasks(uuid)
        ''')
        conn.execute('''
            CREATE INDEX IF NOT EXISTS idx_tasks_type ON tasks(type)
        ''')
        conn.execute('''
            CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks(status)
        ''')

        conn.execute('''
            CREATE TABLE IF NOT EXISTS assets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                uuid TEXT NOT NULL,
                filename TEXT NOT NULL,
                metadata TEXT,
                path TEXT NOT NULL,
                content_type TEXT NOT NULL,
                content_hash TEXT NOT NULL,
                status TEXT NOT NULL,
                extracted_text TEXT NOT NULL
            )
        ''')
        conn.execute('''
            CREATE INDEX IF NOT EXISTS idx_assets_content_hash ON assets(content_hash)
        ''')
        conn.execute('''
            CREATE INDEX IF NOT EXISTS idx_assets_uuid ON assets(uuid)
        ''')
        conn.execute('''
            CREATE INDEX IF NOT EXISTS idx_assets_filename ON assets(filename)
        ''')
        conn.execute('''
            CREATE INDEX IF NOT EXISTS idx_assets_status ON assets(status)
        ''')