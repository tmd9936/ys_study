# 특정 컬러 영역 추출하기

# 특정 영역안에 있는 컬러를 추출하는 함수
# cv2.inRange(src, lowerb, upperb, dst)

import sys, cv2, numpy as np

src = cv2.imread('./images/candies2.png')

if src is None:
    print('Image load failed!!')
    sys.exit()

hsv_src = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# RGB는 명암이 바뀌면 원하는 색상 영역을 못 가져올 경우가 있음
# 반면 HSV는 명암이 바뀌어도 크게 변함없이 원하는 색상 영역을 가져옴
dst1 = cv2.inRange(src, (0, 128, 0), (100, 235, 100))
dst2 = cv2.inRange(hsv_src, (50,150, 0), (80,255,255))

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()


