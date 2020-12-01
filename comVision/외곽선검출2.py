import sys
import random
import numpy as np
import cv2


src = cv2.imread('./images/milkwave.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, hier = cv2.findContours(src_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

h, w = src_bin.shape[:2]
dst = np.zeros((h,w,3), dtype=np.uint8)

# hierachy를 이용한 반복문
# idx = 0 
# while idx >= 0:
    
#     c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     cv2.drawContours(dst, contours, idx, c, 1, cv2.LINE_8, hier) 

#     idx = hier[0, idx, 0]

# N개의 contours만큼 반복
for i in range(len(contours)):
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst, contours, i, c, 1, cv2.LINE_8)

# cv2.imshow('src', src)
cv2.imshow('src', src_bin)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()