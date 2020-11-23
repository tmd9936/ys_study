# 특정 컬러 영역 추출하기

# 특정 영역안에 있는 컬러를 추출하는 함수
# cv2.inRange(src, lowerb, upperb, dst)

import sys, cv2, numpy as np

lowerb = 0
upperb = 255
min_value = 0



def on_lowerb_change(pos):
    global lowerb
    lowerb = pos
    change_inRange()

def on_upperb_change(pos):
    global upperb
    upperb = pos
    change_inRange()

def on_value_change(pos):
    global min_value
    min_value = pos
    change_inRange()

def change_inRange():
    global lowerb, upperb, hsv_src, min_value
    
    dst = cv2.inRange(hsv_src, (lowerb, 150, min_value), (upperb, 255, 255))

    cv2.imshow('dst', dst)


src = cv2.imread('./images/candies2.png')

if src is None:
    print('Image load failed!!')
    sys.exit()

hsv_src = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

dst = cv2.inRange(hsv_src, (lowerb, 150, min_value), (upperb, 255, 255))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.namedWindow('dst')

cv2.createTrackbar('lowerb', 'dst', 0, 255, on_lowerb_change)
cv2.createTrackbar('upperb', 'dst', 0, 255, on_upperb_change)
cv2.createTrackbar('min_value', 'dst', 0, 254, on_value_change)

# cv2.getTrackbarPos('lowerb','dst')

cv2.waitKey()
cv2.destroyAllWindows()
