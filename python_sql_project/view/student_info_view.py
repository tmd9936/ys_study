import controller.student_info_controller as stdcon

def create_student_info_view():
    ids = input('학번 : ')
    name = input('이름 : ')
    tel = input('전화 번호 : ')
    address = input('주소 : ')
    
    stdcon.create_student_info(ids, name, tel, address)
    print('입력완료!')

def get_all_student_info_view():
    std_infos = stdcon.get_all_student_info()
    print('-------------------------------------------------------')
    print('학번  이름  전화번호  주소  성적입력여부')
    print('-------------------------------------------------------')
    for std_info in std_infos:
        print(std_info)

def get_one_student_info_view():
    ids = input('학번 검색 : ')
    if ids.upper() == 'X':
        return None
    std_info = stdcon.get_one_student_info(ids)
    return std_info


    