from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from gui.login_window import LoginWindow
from gui.teacher_profile_window import TeacherProfileWindow
from gui.student_profile_window import StudentProfileWindow
from controllers.auth_controller import AuthController
from controllers.student_controller import StudentController
from controllers.course_controller import CourseController

class CourseManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.auth_controller = AuthController()
        self.student_controller = StudentController()
        self.course_controller = CourseController()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.login_window = LoginWindow(self.auth_controller, self.on_teacher_login, self.on_student_login)
        self.stacked_widget.addWidget(self.login_window)
        self.show_login_window()
    
    def show_login_window(self):
        self.stacked_widget.setCurrentWidget(self.login_window)
        self.resize(600, 300)
        self.setWindowTitle('Course Management System - Login')
    
    def on_teacher_login(self, teacher):
        self.teacher_profile_window = TeacherProfileWindow(teacher, self.student_controller, self.course_controller, self.show_login_window)
        if self.stacked_widget.indexOf(self.teacher_profile_window) == -1:
            self.stacked_widget.addWidget(self.teacher_profile_window)
        self.stacked_widget.setCurrentWidget(self.teacher_profile_window)
        self.resize(800, 600)
    
    def on_student_login(self, student):
        self.student_profile_window = StudentProfileWindow(student, self.course_controller, self.show_login_window)
        if self.stacked_widget.indexOf(self.student_profile_window) == -1:
            self.stacked_widget.addWidget(self.student_profile_window)
        self.stacked_widget.setCurrentWidget(self.student_profile_window)
        self.resize(600, 400)