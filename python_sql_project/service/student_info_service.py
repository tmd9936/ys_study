import sqlite3
import common.consts as consts
from model.student_info import Student_Info


def create(std_info):
    with sqlite3.connect(consts.DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO student_info(\
                'ids',\
                'name',\
                'tel',\
                'address'\
                ) VALUES (?,?,?,?)",(std_info.ids, std_info.name,
                    std_info.tel, std_info.address))
        conn.commit()
        

def get_all():
    with sqlite3.connect(consts.DB_PATH) as conn:
        cur = conn.cursor()
        result= []

        cur.execute(
            "SELECT ids, name, tel, address,\
                (SELECT COUNT(*) FROM STUDENT std\
                    WHERE std.ids = std_info.ids) as cnt\
            FROM student_info std_info")
    
        for std_info in cur.fetchall():
            if std_info[4] == 0:
                is_grade = '미입력'
            else:
                is_grade = '입력완료'

            result.append(Student_Info(
                std_info[0],std_info[1],
                std_info[2],std_info[3],is_grade))


        return result

def get_one(ids):
    with sqlite3.connect(consts.DB_PATH) as conn:
        cur = conn.cursor()

        cur.execute(
            "SELECT ids, name, tel, address,\
                (SELECT COUNT(*) FROM STUDENT std\
                    WHERE std.ids = std_info.ids) as cnt\
            FROM student_info std_info\
            WHERE\
                std_info.ids = ?",(ids,))
        
        std_info = cur.fetchone()

        if std_info == None:
            return {'result' : False, 
                    'std_info' : None}
        else:
            if std_info[4] == 0:
                is_grade = consts.IS_GRADE_FALSE
            else:
                is_grade = consts.IS_GRADE_TRUE
            std_info = Student_Info(std_info[0],std_info[1],std_info[2],
                    std_info[3], is_grade)
            
            return {'result' : True, 
                    'std_info' : std_info}
        
    
        



