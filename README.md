# Course Management System with PyQt6 and SQLite3

## Description
A desktop application for managing courses, students, and teachers in an educational institution. The system provides separate interfaces for teachers and students with appropriate access controls, built using Python with PyQt6 for the GUI and SQLite3 for database storage.

## Key Features
1. **User Authentication**: Separate login systems for teachers and students
2. **Teacher Dashboard**: Manage students and courses
3. **Student Dashboard**: View and register for courses
4. **Database Integration**: SQLite3 backend with three main tables (teachers, students, courses)
5. **CRUD Operations**: Create, Read, Update, Delete functionality for all entities
6. **Error Handling**: Proper validation and error messages
7. **Responsive UI**: Clean, intuitive interface built with PyQt6
8. **Data Validation**: Input verification for all forms
9. **Separation of Concerns**: MVC architecture with distinct layers
10. **Security**: Password protection for all accounts

## Project Requirements
The following 10 functionalities were essential for project completion:

1. **User Authentication System**
   - Separate login interfaces for teachers and students
   - Password protection
   - Error handling for invalid credentials

2. **Teacher Management**
   - Add new teachers to the system
   - Store teacher credentials securely

3. **Student Management**
   - Add/edit/delete student records
   - Track student faculty information
   - Manage course registration

4. **Course Management**
   - Create/edit/delete courses
   - Set course year and eligible faculties
   - View all available courses

5. **Teacher Dashboard**
   - View all students
   - Edit student information
   - Manage course offerings

6. **Student Dashboard**
   - View available courses
   - Add courses to registration basket
   - Confirm course registration

7. **Database Integration**
   - SQLite database setup
   - Three main tables (teachers, students, courses)
   - Proper relationships between tables

8. **Error Handling**
   - Form validation
   - Database operation feedback
   - User-friendly error messages

9. **UI/UX Design**
   - Intuitive navigation
   - Clear information display
   - Responsive design

10. **Security Features**
    - Password protection
    - Input sanitization
    - Access control by user type

## Installation
1. Ensure Python 3.8+ is installed
2. Install required packages:
   ```bash
   pip install PyQt6
