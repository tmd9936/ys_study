import sys, cv2, numpy as np

cap = cv2.VideoCapture('./videos/traffic_clip.mp4')


# 시간 뛰어 넘기
for _ in range(200):
    cap.read()

while True:
    ret, frame = cap.read()

    gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray1, cv2.HOUGH_GRADIENT, 1, 120, None, param2=22, minRadius=10, maxRadius=20)
    if circles is not None:
        for circle in circles[0,:]:
            cx, cy, r = circle
            cv2.circle(frame, (cx,cy), r, (125,125,155), 3)
            # 원안에 사각형 만들기, 왼쪽 위 죄표
            x, y = (cx-r),(cy-r)
            # 히스토그램 값

         

    cv2.imshow('frame', frame)

    if cv2.waitKey(20) == 27:
        break

cap.release()
cv2.destroyAllWindows()