from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QHBoxLayout, QMessageBox
from PyQt6.QtCore import Qt
from gui.add_courses_window import AddCoursesWindow

class StudentProfileWindow(QWidget):
    """Profile window for students"""
    
    def __init__(self, student, course_controller, on_logout):
        super().__init__()
        self.student = student
        self.course_controller = course_controller
        self.on_logout = on_logout
        self.init_ui()
        self.load_basket()
    
    def init_ui(self):
        """Initialize the UI components"""
        self.setWindowTitle(f'Student Profile - {self.student[1]}')
        self.resize(600, 400)
        
        main_layout = QVBoxLayout()
        
        header = QLabel(f'Welcome, {self.student[1]}!')
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(header)
        
        faculty_label = QLabel(f'Faculty: {self.student[4]}')
        main_layout.addWidget(faculty_label)
        
        basket_label = QLabel('Your Course Basket:')
        main_layout.addWidget(basket_label)
        
        self.basket_list = QListWidget()
        main_layout.addWidget(self.basket_list)
        
        buttons_layout = QHBoxLayout()
        
        add_courses_btn = QPushButton('Add Courses')
        add_courses_btn.clicked.connect(self.add_courses)
        buttons_layout.addWidget(add_courses_btn)
        
        confirm_btn = QPushButton('Confirm Registration')
        confirm_btn.clicked.connect(self.confirm_registration)
        buttons_layout.addWidget(confirm_btn)
        
        logout_btn = QPushButton('Logout')
        logout_btn.clicked.connect(self.on_logout)
        buttons_layout.addWidget(logout_btn)
        
        main_layout.addLayout(buttons_layout)
        self.setLayout(main_layout)
    
    def load_basket(self):
    
        self.basket_list.clear()
        self.basket_list.addItem("Course 1")
        self.basket_list.addItem("Course 2")
    
    def add_courses(self):
        """Open add courses window"""
        self.add_courses_window = AddCoursesWindow(self.course_controller)
        self.add_courses_window.show()
    
    def confirm_registration(self):
        """Confirm course registration"""
        QMessageBox.information(self, 'Registration', 'Courses registered successfully!')