# utils/db_api.py
import sqlite3
from config import DB_NAME

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        users_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            limit INTEGER DEFAULT 0,
            active_projects INTEGER DEFAULT 0
        )
        """
        self.cursor.execute(users_query)

        projects_query = """
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            name TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        """
        self.cursor.execute(projects_query)

        self.conn.commit()

    def user_exists(self, user_id):
        self.cursor.execute(f"SELECT * FROM users WHERE id={user_id}")
        result = self.cursor.fetchone()
        return bool(result)

    def add_user(self, user_id):
        self.cursor.execute(f"INSERT INTO users (id) VALUES ({user_id})")
        self.conn.commit()

    def can_create_project(self, user_id):
        self.cursor.execute(f"SELECT * FROM users WHERE id={user_id}")
        user = self.cursor.fetchone()
        return user[1] > user[2]  # Проверяем, что limit > active_projects

    def create_project(self, user_id, project_name):
        self.cursor.execute(f"INSERT INTO projects (user_id, name) VALUES ({user_id}, '{project_name}')")
        self.conn.commit()
        self.cursor.execute(f"UPDATE users SET active_projects = active_projects + 1 WHERE id={user_id}")
        self.conn.commit()
