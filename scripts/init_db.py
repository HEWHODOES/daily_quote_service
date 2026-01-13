
from db_connection import get_quotes_db

#initialising database for quotes_project

conn = get_quotes_db()
cursor = conn.cursor()

# --sql and --endsql only highlighting syntax

cursor.execute("""--sql
    CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               user_name TEXT NOT NULL,
               email TEXT NOT NULL UNIQUE,
               password_hash TEXT NOT NULL ,
               created_at TEXT DEFAULT (datetime('now')),
               deleted_at TEXT DEFAULT NULL 
               )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               category_name TEXT NOT NULL UNIQUE)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS quotes (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               quote TEXT NOT NULL,
               author TEXT DEFAULT NULL,
               source TEXT DEFAULT NULL,
               created_at TEXT DEFAULT (datetime('now'))
               )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS quote_categories (
               quote_id INTEGER NOT NULL ,
               category_id INTEGER NOT NULL ,
               PRIMARY KEY (quote_id, category_id),
               FOREIGN KEY (quote_id) REFERENCES quotes(id) ON DELETE CASCADE,
               FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
               )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_preferences (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               user_id INTEGER NOT NULL,
               category_id INTEGER NOT NULL,
               time_window TEXT NOT NULL CHECK(time_window IN ('fix', 'range')),
               fixed_time TEXT,
               range_start TEXT,
               range_end TEXT,
               paused INTEGER NOT NULL DEFAULT 0,
               FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
               FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
               )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS quote_history (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               user_id INTEGER NOT NULL,
               quote_id INTEGER NOT NULL,
               sent_at TEXT DEFAULT (datetime('now')),
               FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
               FOREIGN KEY (quote_id) REFERENCES quotes(id) ON DELETE CASCADE
               )
--endsql""")

conn.commit()
conn.close()
print("database initialised")