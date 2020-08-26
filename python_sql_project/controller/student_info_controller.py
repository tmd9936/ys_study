import service.student_info_service as s_info_svc
from model.student_info import Student_Info

def create_student_info(ids, name, tel, address):
    std_info = Student_Info(ids,name,tel,address)
    try:
        s_info_svc.create(std_info)
    except:
        return False
    else:
        return True


def get_all_student_info():
    result = s_info_svc.get_all()
    return result

def get_one_student_info(ids):
    result = s_info_svc.get_one(ids)
    return result