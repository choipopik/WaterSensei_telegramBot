import sqlite3
from datetime import datetime, timedelta

database = sqlite3.connect("bot.sqlite")
cursor = database.cursor()

current_time = datetime.now()


def add_user(message):
    cursor.execute("SELECT id FROM users WHERE id=?", (message.chat.id,))
    user = cursor.fetchone()
    if user is None:
        cursor.execute("INSERT INTO users VALUES(?,?,?,?)",
                       (message.chat.id, message.chat.first_name, '2024-01-01', 0))
        database.commit()
    else:
        pass


def upd_date(message):
    cursor.execute("UPDATE users SET last_click=? WHERE id=?", (current_time.date(), message.chat.id,))
    database.commit()


def get_last_date(user_id):
    cursor.execute("SELECT last_click FROM users WHERE id=?", (user_id,))
    user_last_date = cursor.fetchone()[0]
    return user_last_date


def get_streak(user_id):
    cursor.execute("SELECT streak FROM users WHERE id=?", (user_id,))
    user_streak = cursor.fetchone()[0]
    return user_streak


def plus_streak(message, cur_streak):
    print(cur_streak)
    cursor.execute("UPDATE users SET streak=? WHERE id=?", (int(cur_streak) + 1, message.chat.id,))
    database.commit()


def break_streak(message):
    cursor.execute("UPDATE users SET streak=? WHERE id=?", (0, message.chat.id,))
    database.commit()


def get_ids():
    cursor.execute(f"SELECT id FROM users")
    rows = cursor.fetchall()
    return [row[0] for row in rows]


def get_table(message):
    cursor.execute("SELECT * FROM users ORDER BY streak")
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]

    if rows:
        table_message = "<b>Таблица лидеров</b>\n"
        table_message += " | ".join(column_names) + "\n"
        table_message += "-" * (len(" | ".join(column_names))) + "\n"
        for row in rows:
            table_message += " | ".join(map(str, row)) + "\n"
    else:
        table_message = "Таблица пуста."

    return table_message
