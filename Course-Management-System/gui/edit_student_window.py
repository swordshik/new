from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QHBoxLayout)

class EditStudentWindow(QWidget):
    
    def __init__(self, student, student_controller, on_update):
        super().__init__()
        self.student = student
        self.student_controller = student_controller
        self.on_update = on_update
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('Edit Student')
        self.resize(400, 300)
        
        layout = QVBoxLayout()
        
        self.username_edit = QLineEdit(self.student[1])
        self.username_edit.setPlaceholderText('Username')
        layout.addWidget(self.username_edit)
        
        self.email_edit = QLineEdit(self.student[3])
        self.email_edit.setPlaceholderText('Email')
        layout.addWidget(self.email_edit)
        
        self.password_edit = QLineEdit(self.student[2])
        self.password_edit.setPlaceholderText('Password')
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_edit)
        
        self.faculty_edit = QLineEdit(self.student[4])
        self.faculty_edit.setPlaceholderText('Faculty')
        layout.addWidget(self.faculty_edit)
        
        buttons_layout = QHBoxLayout()
        
        save_btn = QPushButton('Save Changes')
        save_btn.clicked.connect(self.save_changes)
        buttons_layout.addWidget(save_btn)
        
        cancel_btn = QPushButton('Cancel')
        cancel_btn.clicked.connect(self.close)
        buttons_layout.addWidget(cancel_btn)
        
        layout.addLayout(buttons_layout)
        self.setLayout(layout)
    
    def save_changes(self):
        new_username = self.username_edit.text()
        new_email = self.email_edit.text()
        new_password = self.password_edit.text()
        new_faculty = self.faculty_edit.text()
        
        success = self.student_controller.update_student(
            self.student[1], new_username, new_email, new_password, new_faculty
        )
        
        if success:
            QMessageBox.information(self, 'Success', 'Student updated successfully')
            self.on_update()
            self.close()
        else:
            QMessageBox.warning(self, 'Error', 'Failed to update student')
