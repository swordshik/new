from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtCore import Qt
from controllers.auth_controller import AuthController

class LoginWindow(QWidget):
    def __init__(self, controller, on_teacher_login, on_student_login):
        super().__init__()
        self.controller = controller
        self.on_teacher_login = on_teacher_login
        self.on_student_login = on_student_login
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('Course Management System - Login')
        self.resize(600, 300)
        main_layout = QHBoxLayout()
        
        teacher_group = QWidget()
        teacher_layout = QVBoxLayout()
        teacher_layout.addWidget(QLabel('Teacher Login', alignment=Qt.AlignmentFlag.AlignCenter))
        self.teacher_username = QLineEdit(placeholderText='Username')
        teacher_layout.addWidget(self.teacher_username)
        self.teacher_password = QLineEdit(placeholderText='Password', echoMode=QLineEdit.EchoMode.Password)
        teacher_layout.addWidget(self.teacher_password)
        teacher_login_btn = QPushButton('Login as Teacher', clicked=self.handle_teacher_login)
        teacher_layout.addWidget(teacher_login_btn)
        teacher_group.setLayout(teacher_layout)
        
        student_group = QWidget()
        student_layout = QVBoxLayout()
        student_layout.addWidget(QLabel('Student Login', alignment=Qt.AlignmentFlag.AlignCenter))
        self.student_username = QLineEdit(placeholderText='Username')
        student_layout.addWidget(self.student_username)
        self.student_password = QLineEdit(placeholderText='Password', echoMode=QLineEdit.EchoMode.Password)
        student_layout.addWidget(self.student_password)
        student_login_btn = QPushButton('Login as Student', clicked=self.handle_student_login)
        student_layout.addWidget(student_login_btn)
        student_group.setLayout(student_layout)
        
        main_layout.addWidget(teacher_group)
        main_layout.addWidget(student_group)
        self.setLayout(main_layout)
    
    def handle_teacher_login(self):
        username = self.teacher_username.text()
        password = self.teacher_password.text()
        teacher = self.controller.login_teacher(username, password)
        if teacher:
            self.on_teacher_login(teacher)
        else:
            QMessageBox.warning(self, 'Login Failed', 'Invalid teacher credentials')
    
    def handle_student_login(self):
        username = self.student_username.text()
        password = self.student_password.text()
        student = self.controller.login_student(username, password)
        if student:
            self.on_student_login(student)
        else:
            QMessageBox.warning(self, 'Login Failed', 'Invalid student credentials')