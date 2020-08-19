import sqlite3

conn = sqlite3.connect('./resource/database.db', isolation_level=None)

cur = conn.cursor()

# 학생 정보 테이블 생성
cur.execute("CREATE TABLE IF NOT EXISTS student_info( \
                ids INTEGER PRIMARY KEY,\
                name TEXT, \
                tel TEXT,\
                address TEXT)")



# 학생 테이블 생성
cur.execute("CREATE TABLE IF NOT EXISTS student( \
                ids INTEGER,\
                os_grade INTEGER, \
                cv_grade INTEGER,\
                db_grade INTEGER, \
                CONSTRAINT ids_fk FOREIGN KEY(ids) \
                    REFERENCES student_info(ids))")
