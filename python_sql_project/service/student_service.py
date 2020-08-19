import sqlite3
from model.student import Student
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