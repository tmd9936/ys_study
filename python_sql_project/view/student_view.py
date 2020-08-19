import controller.student_controller as std_con

def create_student_view(ids):
    os_grade = input('운영체제 : ')
    cv_grade = input('컴퓨터비전 : ')
    db_grade = input('데이터베이스 : ')

    result = std_con.create_student(ids, os_grade, cv_grade, db_grade)

    if result > 0:
        print('성적 입력 성공!!')
    else:
        print('실패...')


def get_all_student():
    pass