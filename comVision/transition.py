import sys
import numpy as np
import cv2


# 두 개의 동영상 불러오기
cap1 = cv2.VideoCapture('./videos/video1.mp4')
cap2 = cv2.VideoCapture('./videos/video2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('video open failed')
    sys.exit()

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = round(cap1.get(cv2.CAP_PROP_FPS))

trasition_frame = fps * 2

print('frame_cnt1 :', frame_cnt1)
print('frame_cnt2 :', frame_cnt2)
print('FPS : ', fps)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 출력 동영상 객체 생성
out = cv2.VideoWriter('./videos/output.avi', fourcc, fps, (w, h))

## 첫 번째 프레임
# while True:
#     ret1, frame1 = cap1.read()

#     if not ret1:
#         break

#     out.write(frame1)
#     cv2.imshow('frame', frame1)
#     cv2.waitKey(10)

##############################

## 첫 번째 프레임
for i in range(frame_cnt1 - trasition_frame):
    ret1, frame1 = cap1.read()

    if not ret1:
        break

    out.write(frame1)
    cv2.imshow('frame', frame1)
    cv2.waitKey(10)

## 합성
## 왼 -> 오
# for i in range(trasition_frame):
#     ret1, frame1 = cap1.read()
#     ret2, frame2 = cap2.read()
#     ##########################
#     # w/trasition_frame : 가로크기 / 48
#     dx = int(w * i/trasition_frame)
#     frame = np.zeros((h,w,3), dtype=np.uint8)
#     frame[:, 0:dx, :] = frame2[:, 0:dx, :]
#     frame[:, dx:w, :] = frame1[:, dx:w, :]
#     ##########################
    
#     out.write(frame)
#     cv2.imshow('frame', frame)
#     cv2.waitKey(10)

# 위 -> 아래
# for i in range(trasition_frame):
#     ret1, frame1 = cap1.read()
#     ret2, frame2 = cap2.read()
#     ##########################
#     # w/trasition_frame : 가로크기 / 48
#     dy = int(h * i/trasition_frame)
#     frame = np.zeros((h,w,3), dtype=np.uint8)
#     frame[0:dy, :, :] = frame2[0:dy, :, :]
#     frame[dy:h, :, :] = frame1[dy:h, :, :]
#     ##########################
    
#     out.write(frame)
#     cv2.imshow('frame', frame)
#     cv2.waitKey(10)

# 대각선
# for i in range(trasition_frame):
#     ret1, frame1 = cap1.read()
#     ret2, frame2 = cap2.read()
#     ##########################
#     # w/trasition_frame : 가로크기 / 48
#     dx = int(w * i/trasition_frame)
#     dy = int(h * i/trasition_frame)

#     frame = frame1
    
#     frame[0:dy, 0:dx, :] = frame2[0:dy, 0:dx, :]
#     frame[dy:h, dx:w, :] = frame1[dy:h, dx:w, :]  
    
#     ##########################
    
#     out.write(frame)
#     cv2.imshow('frame', frame)
#     cv2.waitKey(10)

# 페이드인아웃
for i in range(trasition_frame):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    ##########################
    # w/trasition_frame : 가로크기 / 48
    dx = int(w * i/trasition_frame)
    frame = np.zeros((h,w,3), dtype=np.uint8)

    alpha = 1.0 - i / trasition_frame
    frame = cv2.addWeighted(frame1, alpha, frame2, 1-alpha, 0) # 1 ~ 0 사이의 값이 나오도록 설정
    
    ##########################
    
    out.write(frame)
    cv2.imshow('frame', frame)
    cv2.waitKey(10)   
        


# 원형
# rx = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH)/2)
# ry = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)/2)
# for i in range(trasition_frame):
#     ret1, frame1 = cap1.read()
#     ret2, frame2 = cap2.read()

#     mask = np.zeros_like(frame1)
#     cv2.circle(mask, (rx, ry), int(w * i/trasition_frame), (255,255,255), -1)

#     masked = cv2.bitwise_and(frame2, mask)

#     masked[masked[:,:,:] == (0,0,0)] = frame1[masked[:,:,:] == (0,0,0)]

#     out.write(masked)
#     cv2.imshow('frame', masked)
#     cv2.waitKey(10)


## 두 번째 프레임
for i in range(trasition_frame, frame_cnt2):
    ret2, frame2 = cap2.read()

    if not ret2:
        break

    out.write(frame2)
    cv2.imshow('frame', frame2)
    cv2.waitKey(10)


cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()