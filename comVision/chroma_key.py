import sys, cv2, numpy as np

#cap1 = cv2.VideoCapture('./videos/blue_src.mp4')
cap1 = cv2.VideoCapture('./videos/green_src.mp4')
if not cap1.isOpened():
    print('video1 open failed!!!')
    sys.exit() 

cap2 = cv2.VideoCapture('./videos/monkey2.avi')
if not cap2.isOpened():
    print('video2 open failed!!!')
    sys.exit() 

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

print('frame_cnt1 : ', frame_cnt1)
print('frame_cnt2 : ', frame_cnt2)

fps = cap1.get(cv2.CAP_PROP_FPS)

# 두 프레임 사이의 간격
delay = int(1000 / fps)

# 합성플레그
composit_flag = False

#
while True:
    ret1, frame1 = cap1.read()

    if not ret1:
        break

    if composit_flag:
        ret2, frame2 = cap2.read()
    
        if not ret2:
            break
        
        # frmae1 크기로 사이즈 조정
        frame2 = cv2.resize(frame2, (w,h))
        
        # 배경 영역을 검출하여 합성
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)

        # mask = cv2.inRange(hsv, (100,150,0), (125,255,255))
        mask = cv2.inRange(hsv, (40,150,0), (60,255,255))

        cv2.copyTo(frame2, mask, frame1)

    cv2.imshow('frame', frame1)
    key = cv2.waitKey(delay)

    # spacebar를 이용해서 플래그 toggle
    if key == ord(' '):
        composit_flag = not composit_flag
    elif key == 27:
        break


cap1.release()
cap2.release()
cv2.destroyAllWindows()





