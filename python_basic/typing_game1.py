import random
import time
import winsound

import datetime
import sqlite3

words = []
n = 1 # 게임 횟수
correct_cnt = 0 # 정답의 개수

with open('./resource/word.txt', 'r') as f:
    for word in f:
        words.append(word.strip())

input('엔터키를 누르세요!! 게임 시작됩니다!!')

start = time.time()

while n <= 5:
    random.shuffle(words)
    question = random.choice(words) # 랜덤으로 하나를 추출
    
    print()
    print('********* Question ***********')
    print(question) # 문제 출력
    
    answer = input() # 사용자 입력값
    print()
    
    if str(question).strip() == str(answer).strip():
        print('정답!!')
        # 정답 사운드
        winsound.PlaySound('./resource/good.wav', winsound.SND_FILENAME)
        correct_cnt += 1
    else:
        print('땡!!')
        winsound.PlaySound('./resource/bad.wav', winsound.SND_FILENAME)
    n += 1

end = time.time()

game_time = end - start # 게임시간

game_time = format(game_time, '.2f') # 소수점 두 째자리 출력

if correct_cnt >= 3:
    print('합격')
else:
    print('불합격')
    
print(f'게임시간 : {game_time}초, 정답수 : {correct_cnt}')

# db 연결
conn = sqlite3.connect('./resource/record.db', isolation_level= None)

# Cursor 연결
cur = conn.cursor()

# 테이블 생성
cur.execute("CREATE TABLE IF NOT EXISTS rec_tbl( \
                id INTEGER PRIMARY KEY AUTOINCREMENT,\
                cor_cnt INTEGER, \
                time_rec TEXT,\
                reg_date TEXT)")

# DB 기록하기
cur.execute("INSERT INTO rec_tbl(\
                'cor_cnt',\
                'time_rec',\
                'reg_date' \
                ) VALUES(?,?,?)",(correct_cnt, game_time, 
                    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))



conn.close()