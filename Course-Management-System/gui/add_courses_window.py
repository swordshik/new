from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QMessageBox)

class AddCoursesWindow(QWidget):
    
    def __init__(self, course_controller):
        super().__init__()
        self.course_controller = course_controller
        self.init_ui()
        self.load_courses()
    
    def init_ui(self):
        self.setWindowTitle('Add Courses to Basket')
        self.resize(500, 400)
        
        layout = QVBoxLayout()
        
        self.course_list = QListWidget()
        self.course_list.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        layout.addWidget(self.course_list)
        
        buttons_layout = QHBoxLayout()
        
        add_btn = QPushButton('Add Selected to Basket')
        add_btn.clicked.connect(self.add_to_basket)
        buttons_layout.addWidget(add_btn)
        
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
    
    def add_to_basket(self):
        selected_items = self.course_list.selectedItems()
        if selected_items:
            QMessageBox.information(
                self, 'Success', 
                f'Added {len(selected_items)} courses to your basket'
            )
            self.close()
        else:
            QMessageBox.warning(self, 'Error', 'Please select at least one course')
