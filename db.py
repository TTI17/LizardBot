import sqlite3
from datetime import datetime

DB_NAME = "bot.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # Таблица чатов
    cur.execute("""
    CREATE TABLE IF NOT EXISTS chats (
        chat_id INTEGER PRIMARY KEY,
        title TEXT,
        username TEXT,
        type TEXT,
        member_count INTEGER,
        admin_count INTEGER,
        owner_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Таблица пользователей
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER,
        first_name TEXT,
        last_name TEXT,
        username TEXT,
        status TEXT,
        chat_id INTEGER,
        messages_count INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (user_id, chat_id),
        FOREIGN KEY (chat_id) REFERENCES chats(chat_id)
    )
    """)

    # Таблица сообщений
    cur.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER,
        user_id INTEGER,
        text TEXT,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (chat_id) REFERENCES chats(chat_id),
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
    """)

    conn.commit()
    conn.close()

# Добавить чат
def add_chat(chat_id, title, username, type_, member_count, admin_count, owner_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT OR REPLACE INTO chats (chat_id, title, username, type, member_count, admin_count, owner_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (chat_id, title, username, type_, member_count, admin_count, owner_id))
    conn.commit()
    conn.close()

# Добавить пользователя
def add_user(user_id, first_name, last_name, username, status, chat_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT OR REPLACE INTO users (user_id, first_name, last_name, username, status, chat_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, first_name, last_name, username, status, chat_id))
    conn.commit()
    conn.close()

# Увеличить счётчик сообщений
def increment_message_count(user_id, chat_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE users
        SET messages_count = messages_count + 1
        WHERE user_id = ? AND chat_id = ?
    """, (user_id, chat_id))
    conn.commit()
    conn.close()

# Сохранить сообщение
def add_message(chat_id, user_id, text):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO messages (chat_id, user_id, text)
        VALUES (?, ?, ?)
    """, (chat_id, user_id, text))
    conn.commit()
    conn.close()

# Получить статистику по чату
def get_chat_stats(chat_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM users WHERE chat_id = ?", (chat_id,))
    total_users = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM users WHERE chat_id = ? AND role = 'admin'", (chat_id,))
    total_admins = cur.fetchone()[0]

    conn.close()
    return {
        "total_users": total_users,
        "total_admins": total_admins
    }

def get_group_stats(chat_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.title,
               COUNT(u.user_id) as members_count,
               SUM(CASE WHEN u.role IN ('administrator', 'creator') THEN 1 ELSE 0 END) as admins_count,
               c.joined_count,
               c.left_count
        FROM chats c
        LEFT JOIN users u ON c.chat_id = u.chat_id
        WHERE c.chat_id = ?
        GROUP BY c.chat_id
    """, (chat_id,))
    row = cur.fetchone()
    conn.close()
    return row