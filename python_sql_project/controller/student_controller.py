import service.student_service as std_svc
from model.student import Student

def create_student(ids, os_grade, cv_grade, db_grade):
    std = Student(ids, os_grade, cv_grade, db_grade)
    result = std_svc.create(std)
    return result
