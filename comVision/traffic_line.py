import sys, pafy, cv2, numpy as np


def setLabel(img, pts, label):
    # boundingRect : 주어진 점들을 감싸는 최소크기 사각형
    (x, y, w, h) = cv2.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x + w, y + h)

    # 각 객체 따로 보기
    # temp_img = img[y:y+h, x:x+w]
    # cv2.imshow('poly', temp_img)
    # cv2.waitKey()

    cv2.rectangle(img, pt1, pt2, (0, 0, 255), 1)
    cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))

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



for _ in range(5000):
    cap.read()

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray[:180, :] = 0

    blur = cv2.blur(gray, (10,10))

    # blur = cv2.morphologyEx(blur, cv2.MORPH_OPEN, None)

    # edges = cv2.Canny(blur, 70, 140)
    dstX = cv2.Sobel(blur, -1, 1, 0, ksize=3, scale=0.5, delta=127)

    _, dstX = cv2.threshold(dstX, 145, 255, cv2.THRESH_BINARY)

    lines = cv2.HoughLinesP(dstX, 1, np.pi / 180.0, 110, minLineLength=80, maxLineGap=5)

    # dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    # 큰 물체 판별
    _, img_bin = cv2.threshold(blur, 145, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    for pts in contours[1:]:
        size = cv2.contourArea(pts)
        if size < 3000 or size > 20000:
            continue
        setLabel(frame, pts, 'Big thing')            
        print(size)


    if lines is not None:
        for i in range(lines.shape[0]):
            if lines[i][0][1] > 320 and lines[i][0][3] > 320:
                pt1 = (lines[i][0][0], lines[i][0][1])
                pt2 = (lines[i][0][2], lines[i][0][3])
                cv2.line(frame, pt1, pt2, (0,255,0), 1, cv2.LINE_AA)


    cv2.imshow('frame', frame)
    # cv2.imshow('img_bin', img_bin)
    key = cv2.waitKey(5)

    if key == 27:
        break

cv2.destroyAllWindows()