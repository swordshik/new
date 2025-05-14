from database.database_connection import DatabaseConnection
import sqlite3

class StudentDAO:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def add_student(self, username, password, email, faculty):
        cursor = self.db.get_cursor()
        try:
            cursor.execute("INSERT INTO students (username, password, email, faculty) VALUES (?, ?, ?, ?)",
                        (username, password, email, faculty))
            self.db.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def get_student(self, username):
        cursor = self.db.get_cursor()
        cursor.execute("SELECT * FROM students WHERE username=?", (username,))
        return cursor.fetchone()
    
    def get_all_students(self):
        cursor = self.db.get_cursor()
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()
    
    def validate_student(self, username, password):
        student = self.get_student(username)
        return student if student and student[2] == password else None
    
    def update_student(self, old_username, new_username, new_email, new_password, new_faculty):
        cursor = self.db.get_cursor()
        try:
            cursor.execute('''UPDATE students SET username=?, email=?, password=?, faculty=? WHERE username=?''',
                        (new_username, new_email, new_password, new_faculty, old_username))
            self.db.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def delete_student(self, username):
        cursor = self.db.get_cursor()
        cursor.execute("DELETE FROM students WHERE username=?", (username,))
        self.db.connection.commit()
        return cursor.rowcount > 0