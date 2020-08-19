import random
import time
import winsound

import sqlite3

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

# # DB 기록하기
# cur.execute("INSERT INTO rec_tbl(\
#                 'cor_cnt',\
#                 'time_rec',\
#                 'reg_date' \
#                 ) VALUES(?,?,?)",())

conn.close()


