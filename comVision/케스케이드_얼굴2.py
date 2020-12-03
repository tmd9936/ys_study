# https://github.com/opencv/opencv/tree/master/data/haarcascades
# 정면얼굴 데이터 : haarcascade_frontalface_alt2.xml

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


cap = cv2.VideoCapture('./videos/blue_src.mp4')
sunglass = cv2.imread('./images/sunglass.png', cv2.IMREAD_UNCHANGED)


if cap.isOpened() is None:
    print('video load failed!')
    sys.exit()

# 학습된 데이터 불러오기
faceClassifier = cv2.CascadeClassifier('./studydata/haarcascade_frontalface_alt2.xml') # 정면
eyeClassifier = cv2.CascadeClassifier('./studydata/haarcascade_eye.xml') # 눈


if faceClassifier.empty() or eyeClassifier.empty():
    print('XML load failed!')
    sys.exit()

while True:
    ret, frame = cap.read()

    if frame is None:
        break

    # 기본값은 1.1
    faces = faceClassifier.detectMultiScale(frame, scaleFactor=1.3, minSize=(100,100), maxSize=(300,300))

    for (x, y, w, h) in faces: 
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)

        # 검출된 얼굴에서 눈 디텍팅
        # eyes = eyeClassifier.detectMultiScale(frame[y:y+h, x:x+w])
        eyes = eyeClassifier.detectMultiScale(frame[y:y+h, x:x+w], scaleFactor=1.1, minSize=(15,15), maxSize=(23,23))
        
        # for (x2, y2, w2, h2) in eyes:
        #     cv2.rectangle(frame, (x+x2, y+y2), (x+x2+w2, y+y2+h2), (0,0,255), 2, cv2.LINE_AA)

        if len(eyes) == 2:
            (x1, y1, w1, h1) = eyes[0]
            (x2, y2, w2, h2) = eyes[1]
            
            if x1 > x2:
                bigx = x1
                smallx = x2
                bigw = w1
                smallw = w2
            else:
                bigx = x2
                smallx = x1
                bigw = w2
                smallw = w1
            
            if y1 > y2:
                bigy = y1
                smally = y2
                bigh = h1
                samllh = h2
            else:
                bigy = y2
                smally = y1
                bigh = h2
                samllh = h1
            
            rSunglass = cv2.resize(sunglass, (w, h // 2))

            mask = rSunglass[:, :, 3]
            sg = rSunglass[:, :, :-1]

            mh, mw = mask.shape[:2]

            crop = frame[samllh+y:samllh+mh+y, x:mw+x]

            crop[mask > 0] = sg[mask > 0]

    cv2.imshow('frame', frame)

    if cv2.waitKey(10) == 27:
        break


cv2.destroyAllWindows()