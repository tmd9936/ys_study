# Fourcc(4-문자코드, four charater code)
# 동영상 파일의 코덱, 압축방식, 색상, 픽셀 등을 정의하는 정수값

# *'DIVX' : DIVX MPEG-4 코덱,
# *'XVID' : XVID MPEG-4 코덱, 
# *'FMP4' : FFMPEG MPEG-4 코덱, 
# *'X264' : H.264/AVC 코덱,
# *'MJPG' : Motion JPEG-4 코덱

import sys
import cv2

# 비디오/카메라 파일 열기 : cv2.VideoCapture 클래스
cap = cv2.VideoCapture('./videos/video1.mp4')

if not cap.isOpened():
    print("Video open failed")
    sys.exit()

# 비디오 프레임 크기, 전체 프레임수, FPS
print('Frame Width :',cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('Frame Height :',cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('Frame Count :',cap.get(cv2.CAP_PROP_FRAME_COUNT))

fps = cap.get(cv2.CAP_PROP_FPS)
print("FPS :",fps)

# 비디오 각 프레임 처리
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # inversed = ~frame # 색상반전
    edge = cv2.Canny(frame, 50, 150)
    
    cv2.imshow('frame', frame)
    # cv2.imshow('inversed', inversed)
    cv2.imshow('edge', edge)

    if cv2.waitKey(20) == 27:
        break


cap.release()
cv2.destroyAllWindows()

