from database.database_connection import DatabaseConnection
import sqlite3

class TeacherDAO:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def add_teacher(self, username, password, email):
        cursor = self.db.get_cursor()
        try:
            cursor.execute("INSERT INTO teachers (username, password, email) VALUES (?, ?, ?)",
                        (username, password, email))
            self.db.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def get_teacher(self, username):
        cursor = self.db.get_cursor()
        cursor.execute("SELECT * FROM teachers WHERE username=?", (username,))
        return cursor.fetchone()
    
    def validate_teacher(self, username, password):
        teacher = self.get_teacher(username)
        return teacher if teacher and teacher[2] == password else None