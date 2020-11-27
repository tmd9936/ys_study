import sys, pafy, cv2, numpy as np


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

for _ in range(1900):
    cap.read()

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray[:320,:] = 0

    blur = cv2.GaussianBlur(gray, (0,0), 1)

    edges = cv2.Canny(blur, 70, 140)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180.0, 110, minLineLength=80, maxLineGap=5)

    dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    

    if lines is not None:
        for i in range(lines.shape[0]):
            if lines[i][0][1] > 320 and lines[i][0][3] > 320:
                pt1 = (lines[i][0][0], lines[i][0][1])
                pt2 = (lines[i][0][2], lines[i][0][3])
                cv2.line(frame, pt1, pt2, (0,255,0), 1, cv2.LINE_AA)


    cv2.imshow('frame', frame)
    key = cv2.waitKey(5)

    if key == 27:
        break

cv2.destroyAllWindows()