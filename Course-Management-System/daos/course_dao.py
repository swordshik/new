from database.database_connection import DatabaseConnection
import sqlite3

class CourseDAO:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def add_course(self, name, year, faculties):
        cursor = self.db.get_cursor()
        try:
            cursor.execute("INSERT INTO courses (name, year, faculties) VALUES (?, ?, ?)",
                        (name, year, ",".join(faculties)))
            self.db.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def get_all_courses(self):
        cursor = self.db.get_cursor()
        cursor.execute("SELECT * FROM courses")
        return cursor.fetchall()
    
    def get_course_by_id(self, course_id):
        cursor = self.db.get_cursor()
        cursor.execute("SELECT * FROM courses WHERE id=?", (course_id,))
        return cursor.fetchone()
    
    def update_course(self, course_id, name, year, faculties):
        cursor = self.db.get_cursor()
        try:
            cursor.execute('''UPDATE courses SET name=?, year=?, faculties=? WHERE id=?''',
                        (name, year, ",".join(faculties), course_id))
            self.db.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def delete_course(self, course_id):
        cursor = self.db.get_cursor()
        cursor.execute("DELETE FROM courses WHERE id=?", (course_id,))
        self.db.connection.commit()
        return cursor.rowcount > 0