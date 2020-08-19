import sqlite3

# DB 파일 연결
conn = sqlite3.connect('./resource/database.db')


# 커서 생성(바인딩)
c = conn.cursor()

# 데이터 조회(전체 데이터)
c.execute("SELECT * FROM users")

# 조회한 결과를 가져오기 위한 함수들
# 하나만 가져오기
# print('first : \n', c.fetchone())

# 지정한 만큼 가져오기
# print('second : \n', c.fetchmany(size=3))

# 전체 행(row) 가져오기
#print('all : \n',c.fetchall())
print()

# 반복문 사용하기 1
# rows = c.fetchall()

# for row in rows:
#     print('조회 :', row)

# 반복문 사용하기2
# for row in c.fetchall():
#     print('조회 :', row)

# 반복문 사용하기3
for row in c.execute("SELECT * FROM users ORDER BY id desc"):
    print('조회 :', row)  

# where 패턴 1
param1 = (2,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1 :', c.fetchone())
# 현재 위치에서 더이상 레코드 없음
print('param1 :', c.fetchall())

# where 패턴 2
param2 = 3
# c.execute("SELECT * FROM users WHERE id='%s'" % param2)
c.execute(f"SELECT * FROM users WHERE id={param2}")
print('param2 :', c.fetchone())

# where 패턴 3
c.execute("SELECT * FROM users WHERE id=:Id", {'Id':4})
print('param3 :', c.fetchone())

# where 패턴 4
param4 = (2,5)
c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
print('param4 :', c.fetchall())

# where 패턴 5
c.execute("SELECT * FROM users WHERE id IN('%d','%d')" %(3,4))
print('param5 :', c.fetchall())

# where 패턴 6
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2",{'id1':2 , 'id2':5})
print('param6 :', c.fetchall())


# Dump 출력
with conn:
    with open('./resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump 완성!!')







# conn.close()