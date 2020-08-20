import controller.student_controller as std_con

def create_student_view(ids):
    os_grade = space_proccess(input('운영체제 : ').rstrip())
    cv_grade = space_proccess(input('컴퓨터 비전 : ').rstrip())
    db_grade = space_proccess(input('데이터베이스 : ').rstrip())


    result = std_con.create_student(ids, os_grade, cv_grade, db_grade)

    if result > 0:
        print('성적 입력 성공!!')
    else:
        print('실패...')


def get_all_student_view():
    print('--------------------------------------------------------------------')
    print('학번     이름      운영체제 컴퓨터비전 데이터베이스 총점   평균')
    print('--------------------------------------------------------------------')
    
    stds = std_con.get_all_student()
    for std in stds:
        print(std, end=', ')
        grade_sum = sum([std.os_grade, std.cv_grade, std.db_grade])
        print(grade_sum, round(grade_sum/3, 2))
    
    count = std_con.get_student_num()
    print('전체 학생수 : %s명' % count)


def get_one_student_view():
    ids = input('학번 입력 (종료 : X): ')
    
    if ids.upper() == 'X':
        return None
    result = std_con.get_one_student(ids)
    
    return result

def update_student_view(ids):
    os_grade = space_proccess(input('운영체제 : ').rstrip())
    cv_grade = space_proccess(input('컴퓨터 비전 : ').rstrip())
    db_grade = space_proccess(input('데이터베이스 : ').rstrip())

    result = std_con.update_student(ids, os_grade, cv_grade, db_grade)
    if result == '0':
        print('정상석으로 처리가 되지 않았습니다.')
    else:
        print('정상적으로 처리가 되었습니다.')
    
def delete_student_view(ids):
    result = std_con.delete_student(ids)
    if result == '0':
        print('정상석으로 처리가 되지 않았습니다.')
    else:
        print('정상적으로 처리가 되었습니다.')

def space_proccess(string):
    print("확인 : ",string)
    if string == '' or  string == ' ' or string == '\n' or string == '\r' or string == None:
        return '0'
    else:
        return string


