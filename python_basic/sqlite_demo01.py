"""
SQLite : DB서버가 필요 없는(DB서버를 설치 불필요)
임베디드 관계형 데이터베이스로 경량의 사용이 쉽고, 
편리하며 비용이 들지않는(오픈소스) DB엔진이다.
자신이 서비스하는 애플리케이션 영역 내부에 공존하는 형태의 
데이터 베이스
모바일이나 임베디드 기기에서 많이 사용되며, 신뢰성이 높다.

"""

import sqlite3
import datetime

# 날짜 생성하기
now = datetime.datetime.now()
print('now :', now)

nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDateTime:', nowDateTime)

# sqlite3 버전
print('sqlite version ', sqlite3.version)

# DB 생성 & Auto Commit 설정
conn = sqlite3.connect('./resource/database.db', isolation_level= None)

# isolation_level=None 넣어주면 conn.commit() 생략할 수 있다.

# Cursor 생성(연결, 바인딩)
c = conn.cursor()
print('type : ', type(c))

# 테이블 생성
# Data Type : Text, NUMERIC, INTEGER, REAL, BLOB

c.execute("CREATE TABLE IF NOT EXISTS users(\
            id INTEGER PRIMARY KEY, \
            username TEXT, \
            email TEXT, \
            tel TEXT, \
            website TEXT, \
            reg_date TEXT)")

# 데이터 삽입하기 
# ? 뒤에 컴마 찍고 튜플형태로 넣음
c.execute("INSERT INTO users VALUES(\
            1, \
            'KIM', \
            'test@naver.com',\
            '010-1233-1232',\
            'www.test.com', \
            ?)", (nowDateTime,))

c.execute("INSERT INTO users VALUES(\
            2, \
            'Park', \
            'test2@naver.com',\
            '010-1231-1232',\
            'www.test.com', \
            ?)", (nowDateTime,))

# executeMany를 이용한 삽입(튜플, 리스트)
user_list = (
    (3,'Choi','test@google.com', '010-1234-1234', \
        'www.chol.com',nowDateTime),
    (4,'Lee','test4@google.com', '010-9221-1234', \
        'www.lee.com',nowDateTime),
    (5,'Joo','test5@google.com', '010-6655-1234', \
        'www.joo.com',nowDateTime),
)

c.executemany("INSERT INTO users(id, username, email,\
                tel, website, reg_date) VALUES(?,?,?,?,?,?)"
                , user_list)

# 테이블의 전체 데이터를 삭제하기
# conn.execute("DELETE FROM users")

# 삭제 결과값을 확인하는 함수 사용
# print('users db deleted : ', conn.execute('DELETE FROM users').rowcount, '행')

# 커밋 : isolation_level : None 일 경우 자동 커밋
# isolation_level : None이 아닐 경우에는
# conn.commit()명령으로 DB에 반영해줘야 함.
# conn.rollback()

# 접속 해제하기
conn.close()









