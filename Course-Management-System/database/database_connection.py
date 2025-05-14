import sqlite3

class DatabaseConnection:
    _instance = None
    
    def __new__(cls, db_name='course_management.db'):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = sqlite3.connect(db_name)
            cls._instance.create_tables()
            cls._instance.add_test_data()
        return cls._instance
    
    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            faculty TEXT NOT NULL,
            basket TEXT DEFAULT '[]'
        )''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            year INTEGER NOT NULL,
            faculties TEXT NOT NULL
        )''')
        self.connection.commit()
    
    def add_test_data(self):
        cursor = self.connection.cursor()
        cursor.execute("INSERT OR IGNORE INTO teachers (username, password, email) VALUES (?, ?, ?)",
                    ("teacher1", "password123", "teacher1@example.com"))
        cursor.execute("INSERT OR IGNORE INTO students (username, password, email, faculty) VALUES (?, ?, ?, ?)",
                    ("student1", "password123", "student1@example.com", "Computer Science"))
        cursor.execute("INSERT OR IGNORE INTO students (username, password, email, faculty) VALUES (?, ?, ?, ?)",
                    ("student2", "password123", "student2@example.com", "Engineering"))
        cursor.execute("INSERT OR IGNORE INTO courses (name, year, faculties) VALUES (?, ?, ?)",
                    ("Introduction to Programming", 1, "Computer Science,Engineering"))
        cursor.execute("INSERT OR IGNORE INTO courses (name, year, faculties) VALUES (?, ?, ?)",
                    ("Advanced Databases", 3, "Computer Science"))
        self.connection.commit()
        cursor.close()
    
    def get_cursor(self):
        return self.connection.cursor()