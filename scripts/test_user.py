
import os
from dotenv import load_dotenv
from db_connection import get_quotes_db

load_dotenv()

conn = get_quotes_db()
cursor = conn.cursor()

TEST_EMAIL = os.getenv("TEST_USER_EMAIL")

cursor.execute("INSERT INTO users (user_name, email) VALUES (?, ?)",
               ("Test User", TEST_EMAIL))
user_id = cursor.lastrowid

cursor.execute("SELECT id from categories WHERE category_name = ?", ("Motivation",))
category_id = cursor.fetchone()[0]

cursor.execute("""--sql
               INSERT INTO user_preferences
               (user_id, category_id, time_window, fixed_time)
               VALUES (?, ?, 'fix', '08:00')
               --endsql""", (user_id, category_id))

conn.commit()
conn.close()
print("test user created!")