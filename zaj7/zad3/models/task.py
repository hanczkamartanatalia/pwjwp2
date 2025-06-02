import sqlite3
import os

DB_NAME = 'tasks.db'


def init_db():
    if not os.path.exists(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE Task (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                done BOOLEAN NOT NULL DEFAULT 0
            )
        ''')
        conn.commit()
        conn.close()


class Task:

    def __init__(self, id, content, done):
        self.id = id
        self.content = content
        self.done = bool(done)

    @staticmethod
    def appendTask(content: str):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Task (content, done) VALUES (?, ?)", (content, False))
        conn.commit()
        conn.close()

    @staticmethod
    def removeTask(content: str):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Task WHERE content = ?", (content,))
        conn.commit()
        conn.close()

    @staticmethod
    def setASDone(content: str):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("UPDATE Task SET done = 1 WHERE content = ?", (content,))
        conn.commit()
        cursor.execute("SELECT * FROM Task WHERE content = ?", (content,))
        task = cursor.fetchone()
        conn.close()
        return task

    @staticmethod
    def getAllTasks():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Task")
        rows = cursor.fetchall()
        conn.close()
        return [Task(*row) for row in rows]

# init_db()
