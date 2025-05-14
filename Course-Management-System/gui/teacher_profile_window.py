from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QPushButton, QMessageBox, QSplitter
from PyQt6.QtCore import Qt
from gui.edit_student_window import EditStudentWindow
from gui.edit_courses_window import EditCoursesWindow
from controllers.auth_controller import AuthController

class TeacherProfileWindow(QWidget):
    
    def __init__(self, teacher, student_controller, course_controller, on_logout):
        super().__init__()
        self.teacher = teacher
        self.student_controller = student_controller
        self.course_controller = course_controller
        self.on_logout = on_logout
        self.init_ui()
        self.load_students()
    
    def init_ui(self):
        self.setWindowTitle(f'Teacher Profile - {self.teacher[1]}')
        self.resize(800, 600)
        
        main_layout = QVBoxLayout()
        
        header = QLabel(f'Welcome, Teacher {self.teacher[1]}!')
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(header)
        
        splitter = QSplitter(Qt.Orientation.Vertical)
        
        self.student_list = QListWidget()
        self.student_list.itemSelectionChanged.connect(self.on_student_selected)
        splitter.addWidget(self.student_list)
        
        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout()
        
        self.edit_student_btn = QPushButton('Edit Student')
        self.edit_student_btn.setEnabled(False)
        self.edit_student_btn.clicked.connect(self.edit_student)
        buttons_layout.addWidget(self.edit_student_btn)
        
        self.delete_student_btn = QPushButton('Delete Student')
        self.delete_student_btn.setEnabled(False)
        self.delete_student_btn.clicked.connect(self.delete_student)
        buttons_layout.addWidget(self.delete_student_btn)
        
        edit_courses_btn = QPushButton('Edit Courses')
        edit_courses_btn.clicked.connect(self.edit_courses)
        buttons_layout.addWidget(edit_courses_btn)
        
        logout_btn = QPushButton('Logout')
        logout_btn.clicked.connect(self.on_logout)
        buttons_layout.addWidget(logout_btn)
        
        buttons_widget.setLayout(buttons_layout)
        splitter.addWidget(buttons_widget)
        
        main_layout.addWidget(splitter)
        self.setLayout(main_layout)
    
    def load_students(self):
        self.student_list.clear()
        students = self.student_controller.get_all_students()
        for student in students:
            self.student_list.addItem(f"{student[1]} ({student[3]}) - {student[4]}")
    
    def on_student_selected(self):
        selected = self.student_list.currentRow() != -1
        self.edit_student_btn.setEnabled(selected)
        self.delete_student_btn.setEnabled(selected)
    
    def edit_student(self):
        selected_index = self.student_list.currentRow()
        students = self.student_controller.get_all_students()
        selected_student = students[selected_index]
        
        self.edit_window = EditStudentWindow(
            selected_student,
            self.student_controller,
            self.load_students
        )
        self.edit_window.show()
    
    def delete_student(self):
        selected_index = self.student_list.currentRow()
        students = self.student_controller.get_all_students()
        selected_student = students[selected_index]
        
        reply = QMessageBox.question(
            self, 'Confirm Delete',
            f'Are you sure you want to delete student {selected_student[1]}?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            success = self.student_controller.delete_student(selected_student[1])
            if success:
                QMessageBox.information(self, 'Success', 'Student deleted successfully')
                self.load_students()
            else:
                QMessageBox.warning(self, 'Error', 'Failed to delete student')
    
    def edit_courses(self):
        self.courses_window = EditCoursesWindow(self.course_controller)
        self.courses_window.show()