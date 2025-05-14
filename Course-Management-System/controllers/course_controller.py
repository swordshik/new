from daos.course_dao import CourseDAO

class CourseController:
    def __init__(self):
        self.course_dao = CourseDAO()
    
    def get_all_courses(self):
        return self.course_dao.get_all_courses()
    
    def update_course(self, course_id, name, year, faculties):
        return self.course_dao.update_course(course_id, name, year, faculties)
    
    def delete_course(self, course_id):
        return self.course_dao.delete_course(course_id)
    
    def add_course(self, name, year, faculties):
        return self.course_dao.add_course(name, year, faculties)