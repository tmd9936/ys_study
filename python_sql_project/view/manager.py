import view.student_info_view as std_info_view
import view.student_view as std_view
import common.consts as consts


def menu():
    print('----------------------------------------')
    print('            학사관리 시스템              ')
    print('----------------------------------------')
    print('1. 학생 정보 입력')
    print('2. 학생 정보 출력')
    print('3. 학생 성적 입력')
    print('4. 학생 성적 출력')
    print('X. 프로그램 종료 ')
    print('----------------------------------------')
    
    num = input('메뉴 선택 : ')

    if num == '1':
        print('1. 학생 정보 입력(종료:X)')
        std_info_view.create_student_info_view()
        return True
    elif num ==  '2':
        print('2. 학생 정보 출력(종료:X)')
        std_info_view.get_all_student_info_view()
        return True
    elif num == '3':
        print('3. 학생 성적 입력(종료:X)')
        student_create_view_manager()
        return True
    elif num == '4':
        return True
    elif num == 'X':
        return False

def student_create_view_manager():  
    while True:      
        std_info_one = std_info_view.get_one_student_info_view()
        if std_info_one == None:
            break
        if not std_info_one.get('result'):
            print('존재하지 않는 학번입니다..')
            continue
        else:
            std_info = std_info_one.get('std_info')
            print(std_info)

            if std_info.is_grade == consts.IS_GRADE_TRUE:
                continue
            else:
                std_view.create_student_view(std_info.ids)


