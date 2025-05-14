from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QPushButton, QMessageBox)

class EditCoursesWindow(QWidget):
    
    def __init__(self, course_controller):
        super().__init__()
        self.course_controller = course_controller
        self.init_ui()
        self.load_courses()
    
    def init_ui(self):
        self.setWindowTitle('Edit Courses')
        self.resize(600, 400)
        
        layout = QVBoxLayout()
        
        self.course_list = QListWidget()
        self.course_list.itemSelectionChanged.connect(self.on_course_selected)
        layout.addWidget(self.course_list)
        
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText('Course Name')
        layout.addWidget(self.name_edit)
        
        self.year_edit = QLineEdit()
        self.year_edit.setPlaceholderText('Year')
        layout.addWidget(self.year_edit)
        
        self.faculties_edit = QLineEdit()
        self.faculties_edit.setPlaceholderText('Faculties (comma separated)')
        layout.addWidget(self.faculties_edit)
        
        buttons_layout = QHBoxLayout()
        
        self.edit_btn = QPushButton('Edit Course')
        self.edit_btn.setEnabled(False)
        self.edit_btn.clicked.connect(self.edit_course)
        buttons_layout.addWidget(self.edit_btn)
        
        add_btn = QPushButton('Add Course')
        add_btn.clicked.connect(self.add_course)
        buttons_layout.addWidget(add_btn)
        
        self.delete_btn = QPushButton('Delete Course')
        self.delete_btn.setEnabled(False)
        self.delete_btn.clicked.connect(self.delete_course)
        buttons_layout.addWidget(self.delete_btn)
        
        close_btn = QPushButton('Close')
        close_btn.clicked.connect(self.close)
        buttons_layout.addWidget(close_btn)
        
        layout.addLayout(buttons_layout)
        self.setLayout(layout)
    
    def load_courses(self):
        self.course_list.clear()
        courses = self.course_controller.get_all_courses()
        for course in courses:
            self.course_list.addItem(f"{course[1]} (Year: {course[2]}, Faculties: {course[3]})")
    
    def on_course_selected(self):
        selected = self.course_list.currentRow() != -1
        self.edit_btn.setEnabled(selected)
        self.delete_btn.setEnabled(selected)
        
        if selected:
            courses = self.course_controller.get_all_courses()
            selected_course = courses[self.course_list.currentRow()]
            
            self.name_edit.setText(selected_course[1])
            self.year_edit.setText(str(selected_course[2]))
            self.faculties_edit.setText(selected_course[3])
    
    def edit_course(self):
        selected_index = self.course_list.currentRow()
        courses = self.course_controller.get_all_courses()
        selected_course = courses[selected_index]
        
        name = self.name_edit.text()
        year = self.year_edit.text()
        faculties = [f.strip() for f in self.faculties_edit.text().split(',')]
        
        try:
            year = int(year)
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Year must be a number')
            return
        
        success = self.course_controller.update_course(
            selected_course[0], name, year, faculties
        )
        
        if success:
            QMessageBox.information(self, 'Success', 'Course updated successfully')
            self.load_courses()
        else:
            QMessageBox.warning(self, 'Error', 'Failed to update course')
    
    def add_course(self):
        name = self.name_edit.text()
        year = self.year_edit.text()
        faculties = [f.strip() for f in self.faculties_edit.text().split(',')]
        
        try:
            year = int(year)
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Year must be a number')
            return
        
        success = self.course_controller.add_course(name, year, faculties)
        
        if success:
            QMessageBox.information(self, 'Success', 'Course added successfully')
            self.load_courses()
        else:
            QMessageBox.warning(self, 'Error', 'Failed to add course (possibly already exists)')
    
    def delete_course(self):
        selected_index = self.course_list.currentRow()
        courses = self.course_controller.get_all_courses()
        selected_course = courses[selected_index]
        
        reply = QMessageBox.question(
            self, 'Confirm Delete',
            f'Are you sure you want to delete course {selected_course[1]}?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            success = self.course_controller.delete_course(selected_course[0])
            if success:
                QMessageBox.information(self, 'Success', 'Course deleted successfully')
                self.load_courses()
            else:
                QMessageBox.warning(self, 'Error', 'Failed to delete course')
