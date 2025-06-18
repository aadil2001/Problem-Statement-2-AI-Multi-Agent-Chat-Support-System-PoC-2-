# db/database.py
import sqlite3

conn = sqlite3.connect('chat.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    message TEXT
)
''')

def log_ticket(user_id, message):
    cursor.execute("INSERT INTO tickets (user_id, message) VALUES (?, ?)", (user_id, message))
    conn.commit()
