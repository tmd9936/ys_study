import sys, cv2, numpy as np

cap = cv2.VideoCapture('./videos/clip.mp4')

if not cap.isOpened():
    print('video open failed!!')
    sys.exit()

ret, frame = cap.read()
print(frame.shape) # 720, 1280, 3

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')

out = cv2.VideoWriter('./videos/out_clip.mp4', fourcc, fps, (w,h))

# 당구대 부분만 자르기 
# 원+색으로 빨간색 흰색 검출
# 당구대 검출?
# 해당 턴의 당구공 색이 다른 당구공 맞고 벽에 3번 맞고 안맞은 다른색 공에 맞는지
# 맞으면 1점

ch_mode = 0
dst = None

while True:
    ret, frame = cap.read()

    if not ret:
        break

    dst = frame[110:550,240:1050]

    if ch_mode == 0:
        pass
    elif ch_mode == 1:
        gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(gray, method=cv2.HOUGH_GRADIENT, 
                    dp=1, minDist=100, param2=18, minRadius=3, maxRadius=12)
        if circles is not None:
            for circle in circles[0,:]:
                cx, cy, r = circle
                cv2.circle(dst, (cx,cy), r, (0,255,255), 2)
    
    cv2.imshow('dst', dst)

    key = cv2.waitKey(10)

    if key == 27:
        break
    if key == ord(' '):
        ch_mode += 1
        if ch_mode == 2:
            ch_mode == 0

cap.release()
cv2.destroyAllWindows()

    

