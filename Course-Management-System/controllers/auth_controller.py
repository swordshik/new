from database.teacher_dao import TeacherDAO
from database.student_dao import StudentDAO

class AuthController:
    def __init__(self):
        self.teacher_dao = TeacherDAO()
        self.student_dao = StudentDAO()
    
    def login_teacher(self, username, password):
        return self.teacher_dao.validate_teacher(username, password)
    
    def login_student(self, username, password):
        return self.student_dao.validate_student(username, password)