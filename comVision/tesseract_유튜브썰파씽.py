# Tesseract
# 광학 문자 인식(OCR) 라이브러리
# 독일 만하임 대학교 사이트(https://github.com/UB-Mannheim/tesseract/wiki)
# Tesseract 설치 후
# pip install pytesseract 명령 실행

import sys
import random
import numpy as np
import cv2, pafy
import pytesseract

url = 'https://www.youtube.com/watch?v=tyMj0r8MfNw'
video = pafy.new(url)
print('title =', video.title)
print('rating =', video.rating)
# print('duration =', video.duration)

s_d = video.duration.split(':')
duration_sec = int(s_d[0])*3600 + int(s_d[1])*60 + int(s_d[2])
print('duration_sec =', duration_sec)

best = video.getbest(preftype='mp4')
print('best.resolution =', best.resolution)
print('best.url =',best.url)

cap = cv2.VideoCapture(best.url)


for _ in range(2000):
    cap.read()

oldst = ""
while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    st = pytesseract.image_to_string(gray, lang='Hangul')
    st = st.strip()

    if st is None or st == "" or oldst == st:
        continue
    
    print(st)
    oldst = st

    cv2.imshow('frame', frame)
    # cv2.imshow('img_bin', img_bin)
    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.waitKey()
cv2.destroyAllWindows()