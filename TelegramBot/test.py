"""import sqlite3
from datetime import datetime

database = sqlite3.connect("bot.sqlite")
cursor = database.cursor()


cursor.execute("SELECT streak FROM users WHERE id=?", (1044276987,))
user_streak = cursor.fetchone()[0]
print(user_streak)