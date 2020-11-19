import numpy as np
import cv2

# 직선 그리기
# cv2.line(img, pt1, pt2, color, thickness, lineType, shift)
# img : 그릴 영상(도화지)
# pt1, pt2 : 선의 시작과 끝점(튜플)
# color : 색상, thickness : 두깨(기본값 1)
# lineType : 선타입(cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA)
# LINE_AA : Anti_alias, 주변에 다른색을 추가해서 곡선을 좀 더 부드럽게 보여줌
# shift : 좌표값의 축소 비율 , 기본값=0

# fill_value값을 이미지에 채움
img = np.full((800,800,3),(255,255,255), np.uint8)

# cv2.line(img, (100,100), (400,100), (255, 0, 0), 50)
# cv2.line(img, (140,140), (400,400), (0, 0, 255), 25)

# cv2. rectangle(img, pt1, pt2, color, thickness, lineType, shift)
# cv2. rectangle(img, rec, color, thickness, lineType, shift)

# (x,y,w,h) w:폭, h:높이
cv2.rectangle(img, (50, 200, 150, 150), (153,223,54), 10)
cv2.rectangle(img, (70, 220), (180, 280), (26,100,204), -1) # -1은 채우기

# cv2.circle(img, center, radius, color, thickness, lineType, shift)
cv2.circle(img, (300, 300), 100, (255,155,100), -1, lineType=cv2.LINE_AA)

# 타원
# cv2.ellipse(img, center, size(가로세로사이즈), 앵글, 시작각도, 끝각도, color, thickness, lineType, shift)

cv2.ellipse(img, (400,500), (200, 150), 0, 180, 360, (0,0,255), -1)
cv2.ellipse(img, (400,500), (200, 150), 45, 0, 360, (255,0,0), 5)
cv2.ellipse(img, (400,500), (200, 150), 0, 0, 360, (0,255,0), 5)

# 다각형
# cv2.plolylines(img, pts, isClose, color, thickness, lineType, shift)
pts = np.array([
            [399,200], [300, 150], [350, 300], [250, 300]
        ])
cv2.polylines(img, [pts], True, (255, 0 ,255), 2)

# cv.putText(img, text, org, fontFace, fontScale, color, thick, bottomLeftOrigin)
text = "My Picture"
cv2.putText(img, text, (200, 600), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,244), lineType=cv2.LINE_AA)

############################



cv2.imshow('img', img)
cv2.waitKey()

cv2.destroyAllWindows()





















