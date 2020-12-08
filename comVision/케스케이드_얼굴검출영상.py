# https://github.com/opencv/opencv/tree/master/data/haarcascades
# 정면얼굴 데이터 : haarcascade_frontalface_alt2.xml

# 얼굴영상 :https://www.pexels.com/search/videos/face

# cv2.CascadeClassifier.detectMultiScale(image, scaleFactor=None, minNeighbors=None, flags=None, minSize=None, maxSize=None, /) 
# image : 입력 영상
# scaleFactor: 기본값 1.1(영상 축소 비율), 기본값은 사각형의 크기를 1.1배로 점점 키우면서 검출
# ex) 1.2는 1.2배씩 키워가면서 검출
# minneighbors : 최종 검출 영역으로 설정하기 위한 사각형의 개수 지정, 기본값 3
# flags : 사용하지 않음
# minSize, maxSize : 보통 (24, 24)부터 시작,
# minSize를 지정해서 속도를 빠르게 할 수 있다.

import sys
import numpy as np
import cv2


cap = cv2.VideoCapture('./videos/face01.mp4')


if cap.isOpened() is None:
    print('video load failed!')
    sys.exit()

# 학습된 데이터 불러오기
classifier = cv2.CascadeClassifier('./studydata/haarcascade_frontalface_alt2.xml') # 정면


if classifier.empty():
    print('XML load failed!')
    sys.exit()

while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, (800,700))

    if frame is None:
        break

    # 기본값은 1.1
    faces = classifier.detectMultiScale(frame, scaleFactor=1.2)


    for (x, y, w, h) in faces: 
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(5) == 27:
        break

cv2.waitKey()
cv2.destroyAllWindows()
