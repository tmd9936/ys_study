import sqlite3
from model.student import Student
from model.student_with_name import Student_with_name
import common.consts as consts

def create(student):
    with sqlite3.connect(consts.DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO student(\
                    ids,\
                    os_grade,\
                    cv_grade,\
                    db_grade\
                ) VALUES(?,?,?,?)",(student.ids, student.os_grade,
                            student.cv_grade, student.db_grade))
        conn.commit()
        return cur.rowcount

def get_all():
    with sqlite3.connect(consts.DB_PATH) as  conn:
        cur = conn.cursor()
        cur.execute("SELECT std.ids, \
                            info.name,\
                            IFNULL(std.os_grade, 0),\
                            IFNULL(std.cv_grade, 0),\
                            IFNULL(std.db_grade, 0)\
                    FROM student std, student_info info \
                    WHERE std.ids = info.ids")
        
        result = []
        for stu in cur.fetchall():
            std = Student_with_name(stu[0], stu[1], stu[2], stu[3],
                            stu[4])
            result.append(std)
        
        return result

def get_num():
    with sqlite3.connect(consts.DB_PATH) as  conn:
        cur = conn.cursor()
        cur.execute("SELECT count(*) \
                    FROM student")
        
        result = cur.fetchone()
        return result

def get_one(ids):
    with sqlite3.connect(consts.DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT ids, \
                            IFNULL(os_grade, 0),\
                            IFNULL(cv_grade,0),\
                            IFNULL(db_grade,0) \
                    FROM student \
                    WHERE ids = ?",(ids,))
        
        query = cur.fetchone()
        if query == None:
            return False
        else:
            return Student(*query)
        
def update(stu):
    with sqlite3.connect(consts.DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("UPDATE student\
                    SET os_grade = ?, \
                        cv_grade = ?,\
                        db_grade = ? \
                    WHERE ids = ?",
                    (stu.os_grade, stu.cv_grade, stu.db_grade, stu.ids))
        
        result = cur.rowcount
        return result

def delete(ids):
    with sqlite3.connect(consts.DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM student \
                    WHERE ids = ?",(ids,))
        
        result = cur.rowcount
        return result