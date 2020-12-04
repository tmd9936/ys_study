import sys
import numpy as np
import cv2

def overlay(img, glasses, pos):
    # 실제 합성을 수행할 부분 영상 좌표 계산
    # sx, sy : 시작좌표 
    # ex, ey : 길이
    sx = pos[0]
    ex = pos[0] + glasses.shape[1]
    sy = pos[1]
    ey = pos[1] + glasses.shape[0]

    # 합성할 영역이 입력 영상 크기를 벗어나면 무시(합성 안함)
    if sx < 0 or sy < 0 or ex > img.shape[1] or ey > img.shape[0]:
        return

    # frame에서 합성할 부분 crop
    img1 = img[sy:ey, sx:ex]   # shape=(h, w, 3)
    
    # 알파채널을 뺀 안경의 bgr값 추출
    img2 = glasses[:, :, 0:3]  # shape=(h, w, 3)

    #  알파채널로 각 원소의 가중치 정하기
    alpha = 1. - (glasses[:, :, 3] / 255.)  # shape=(h, w)

    # BGR 채널별로 두 부분 영상의 가중합
    # img1[..., 0] -> 앞에꺼 다 건너뛰고 마지막 차원의 0번째 값들
    # img1[:,:, 0] = (img1[:,:, 0] * alpha + img2[:,:, 0] * (1. - alpha)).astype(np.uint8)
    # img1[:,:, 1] = (img1[:,:, 1] * alpha + img2[:,:, 1] * (1. - alpha)).astype(np.uint8)
    # img1[:,:, 2] = (img1[:,:, 2] * alpha + img2[:,:, 2] * (1. - alpha)).astype(np.uint8)

    img1[..., 0] = (img1[..., 0] * alpha + img2[..., 0] * (1. - alpha)).astype(np.uint8)
    img1[..., 1] = (img1[..., 1] * alpha + img2[..., 1] * (1. - alpha)).astype(np.uint8)
    img1[..., 2] = (img1[..., 2] * alpha + img2[..., 2] * (1. - alpha)).astype(np.uint8)


cap = cv2.VideoCapture('./videos/blue_src.mp4')

if not cap.isOpened():
    print('Camera open failed!')
    sys.exit()

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 비디오 저장을 위한 코덱 설정&객체
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# out = cv2.VideoWriter('./output_f.avi', fourcc, 30, (w, h))

# Haar-like XML 파일 열기
face_classifier = cv2.CascadeClassifier('./studydata/haarcascade_frontalface_alt2.xml')
eye_classifier = cv2.CascadeClassifier('./studydata/haarcascade_eye.xml')

if face_classifier.empty() or eye_classifier.empty():
    print('XML load failed!')
    sys.exit()

# 안경 PNG 파일 열기 (Image from http://www.pngall.com/)
# IMREAD_UNCHANGED -> 알파채널이 있는 경우 원본이미지를 사용해야됨
glasses = cv2.imread('./images/glasses.png', cv2.IMREAD_UNCHANGED)

if glasses is None:
    print('PNG image open failed!')
    sys.exit()

# 합성할 안경영상의 계산된 눈의 좌표 위치
ew, eh = glasses.shape[:2]  
# 안경영상의 크기에 맞춘 임의의 눈의 좌표 ? 
ex1, ey1 = 240, 300  
ex2, ey2 = 660, 300  

# 프레임별 안경 합성
while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    # 얼굴 검출
    faces = face_classifier.detectMultiScale(frame, scaleFactor=1.2,
                                             minSize=(100, 100), maxSize=(400, 400))

    for (x, y, w, h) in faces:
        # 눈 검출
        # 얼굴 반쪽 위 부분
        faceROI = frame[y:y + h // 2, x:x + w]
        eyes = eye_classifier.detectMultiScale(faceROI)

        # 눈 2개가 검출이 안되면 빠져나옴
        if len(eyes) != 2:
            continue
        
        x1 = x + eyes[0][0] + (eyes[0][2] // 2) 
        y1 = y + eyes[0][1] + (eyes[0][3] // 2)
        x2 = x + eyes[1][0] + (eyes[1][2] // 2) 
        y2 = y + eyes[1][1] + (eyes[1][3] // 2) 

        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        fx = (x2 - x1) / (ex2 - ex1)
        # 위에서 구한 fx비율에 맞춰 안경영상의 크기를 변경
        glasses2 = cv2.resize(glasses, (0, 0), fx=fx, fy=fx, interpolation=cv2.INTER_AREA)

        # 크기 조절된 안경 영상을 합성할 위치 계산 (좌상단 좌표)
        pos = (x1 - int(ex1 * fx), y1 - int(ey1 * fx))

        # pos 위치에 합성을 해주는 함수
        overlay(frame, glasses2, pos)

    # 프레임 저장 및 화면 출력
    # out.write(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()