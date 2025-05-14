from database.student_dao import StudentDAO

class StudentController:
    def __init__(self):
        self.student_dao = StudentDAO()
    
    def get_all_students(self):
        return self.student_dao.get_all_students()
    
    def update_student(self, old_username, new_username, new_email, new_password, new_faculty):
        return self.student_dao.update_student(old_username, new_username, new_email, new_password, new_faculty)
    
    def delete_student(self, username):
        return self.student_dao.delete_student(username)
    
    def add_student(self, username, password, email, faculty):
        return self.student_dao.add_student(username, password, email, faculty)