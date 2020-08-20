import service.student_service as std_svc
from model.student import Student

def create_student(ids, os_grade, cv_grade, db_grade):
    std = Student(ids, os_grade, cv_grade, db_grade)
    result = std_svc.create(std)
    return result

def get_all_student():
    result = std_svc.get_all()
    return result

def get_student_num():
    result = std_svc.get_num()
    return result

def get_one_student(ids):
    result = std_svc.get_one(ids)
    return result

def update_student(ids, os_grade, cv_grade, db_grade):
    std = Student(ids, os_grade, cv_grade, db_grade)
    result = std_svc.update(std)
    return result

def delete_student(ids):
    result = std_svc.delete(ids)
    return result