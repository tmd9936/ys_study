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
    print('5. 학생 성적 수정')
    print('6. 학생 성적 삭제')
    print('X. 프로그램 종료 ')
    print('----------------------------------------')
    
    num = input('메뉴 선택 : ')

    if num == consts.CREATE_STUDENT_INFO_COMMAND:
        print('1. 학생 정보 입력(종료:X)')
        std_info_view.create_student_info_view()
        return True
    elif num ==  consts.PRINT_STUDENT_INFO_COMMAND:
        print('2. 학생 정보 출력(종료:X)')
        std_info_view.get_all_student_info_view()
        return True
    elif num == consts.CREATE_STUDENT_COMMAND:
        print('3. 학생 성적 입력(종료:X)')
        student_create_view_manager()
        return True
    elif num == consts.PRINT_STUDENT_COMMAND:
        print('4. 학생 성적 출력(종료:X)')
        std_view.get_all_student_view()
        return True
    elif num == consts.UPDATE_STUDENT_COMMAND:
        print('5. 학생 성적 수정(종료:X)')
        student_view_manager(num)
        return True
    elif num == consts.DELETE_STUDENT_COMMAND:
        print('6. 학생 성적 삭제(종료:X)')
        student_view_manager(num)
        return True
    elif num.upper()== 'X':
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


def student_view_manager(num):
    while True:
        std_one = std_view.get_one_student_view()
        if std_one == None:
            break
        elif std_one == False:
            print('존재하지 않는 학번입니다..')
            continue
        else:
            print('--------------------------------------------------')
            print('학번  이름  운영체제 컴퓨터비전 데이터베이스 ')
            print('--------------------------------------------------')
            print(std_one)
            if num == consts.UPDATE_STUDENT_COMMAND:
                inp = input('위의 학생의 성적을 수정 하시겠습니까? (수정:Y, 넘기기: 다른 아무키) ')
                if inp.upper() == 'Y':
                    result = std_view.update_student_view(std_one.ids)
            if num == consts.DELETE_STUDENT_COMMAND:
                inp = input('위의 학생의 성적을 삭제 하시겠습니까? (삭제:Y, 넘기기: 다른 아무키) ')
                if inp.upper() == 'Y':
                    result = std_view.delete_student_view(std_one.ids)

                

            
        
