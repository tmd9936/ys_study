# 테이블 수정 / 삭제

import sqlite3

# DB 접속 및 생성
conn = sqlite3.connect('./resource/database.db')

# cursor 바인딩
cur = conn.cursor()

# 데이터 수정1
# cur.execute("UPDATE users SET username = ? WHERE id = ?",('Cho', 3))
# print(cur.rowcount)

# 데이터 수정2
# cur.execute("UPDATE users SET username = :username WHERE id = :id",{'username':'Kang', 'id':5})

# 데이터 수정3
# cur.execute("UPDATE users SET username = '%s' WHERE id = '%d'" % ('Hong', 4))
# cur.execute(f"UPDATE users SET username = '{'Hong2'}' WHERE id = {4}")

# 데이터 삭제 1
# cur.execute("DELETE FROM users WHERE id= ?",(2,))

# 데이터 삭제 2
# cur.execute("DELETE FROM users WHERE id= :id", {'id':5})

# cur.execute("DELETE FROM users WHERE id='%s'" % 4)

# [문제1]데이터 확인하기
datas = cur.execute("SELECT * FROM users")

for data in datas:
    print(data)

# [문제2] 남은 데이터 모두 삭제하기 (삭제된 행의 수 출력)
print(cur.execute("DELETE FROM users").rowcount)


# 커밋
conn.commit()

conn.close()