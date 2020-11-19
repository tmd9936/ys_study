import numpy as np
import cv2

# 트랙바 (Trackbar)
# cv.creatTrackbar(trackbarName, windowName, value, count, onChange)
# trackbarName : 트랙바 이름
# windowName : 트랙바를 생성할 창이름.
# value : 트랙바의 위치 초기값
# count : 트랙바 최대값
# onChange : 트랙바의 위치가 변경될 때마다 호출되는 콜백 함수 이름
# onchang(pos)

def on_level_changed(pos):
    global img

    level = pos * 16

    # if level > 255:
    #     level = 255

    level = np.clip(level, 0, 255)

    img[:,:] = level
    cv2.imshow('image', img)

img = np.zeros((480, 640), np.uint8)

# cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.createTrackbar('level', 'image', 0, 16, on_level_changed)
cv2.waitKey()

cv2.destroyAllWindows()