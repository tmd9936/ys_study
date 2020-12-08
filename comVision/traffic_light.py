import sys, pafy, cv2, numpy as np

# cap = cv2.VideoCapture('./videos/traffic_clip.mp4')

url = 'https://www.youtube.com/watch?v=fEkeyes0jSc'
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

# 빨강 평균 50
# 파랑 평균 112
# 노랑 평균 66

# 시간 뛰어 넘기
for _ in range(2800):
    cap.read()

move_state = "GO"
old_move_state = "GO"

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (0,0), 1)
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 200, None, param1=150, 
            param2=15, minRadius=2, maxRadius=7)
    
    if circles is not None:
        for circle in circles[0,:]:
            cx, cy, r = circle
            cv2.circle(frame, (cx,cy), r, (125,125,155), 3, cv2.LINE_AA)
            # 원안에 사각형 만들기, 왼쪽 위 죄표
            x1 = int(cx - r)
            y1 = int(cy - r)
            x2 = int(cx + r)
            y2 = int(cy + r)
            r = int(r)

            # 히스토그램 값
            # HSV 로 변환해서 
            crop = frame[y1:y2, x1:x2, :]
            
            ch, cw = crop.shape[:2]

            if ch < 1 or cw < 1:
                continue

            mask = np.zeros((ch, cw), np.uint8)
            # 마스크에 ROI부분의 값음 채움
            cv2.circle(mask, (cw//2, ch//2), r, 255, -1)
            
            # hue 계산
            hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
            hue, _, _ = cv2.split(hsv)
            # hue에 shit를 줘서 양극단에 있던 빨간값을 왼쪽으로 몰리게 함
            hist_shift = (hue + 50) % 180
            maen_of_hue = cv2.mean(hist_shift, mask)[0]


            # print(maen_of_hue)
            # cv2.imshow('crop', crop)
            # cv2.imshow('mask', mask)
            # cv2.waitKey()
            
            if maen_of_hue > 48 and maen_of_hue < 53:
                move_state = "STOP"
                old_move_state = move_state
            elif maen_of_hue > 64 and maen_of_hue < 69:
                move_state = "READY"
                old_move_state = move_state
            elif maen_of_hue > 109 and maen_of_hue < 114:
                move_state = "GO"
                old_move_state = move_state
    else:
        move_state = "GO"        
    
    cv2.putText(frame, move_state, (40, 80), cv2.FONT_HERSHEY_SIMPLEX,
        2, (255,0,0), 2, cv2.LINE_AA)

         

    cv2.imshow('frame', frame)

    if cv2.waitKey(20) == 27:
        break

cap.release()
cv2.destroyAllWindows()