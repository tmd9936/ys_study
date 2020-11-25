# 2D 벡터 크기 구하는 함수
# cv2.magnitude(x, y, magnitude=None)
# x : 2D벡터의 x좌표 행렬(실수형), x의 편미분
# y : 2D벡터릐 y좌표 행렬, x와 같은 크기(실수형), y의 편미분
# 그라디언트 : 기울기, 경사
# 매그니튜드 : 그라디언트의 크기, 큰값을 갖는 곳이 엣지부분


import math, sys, cv2, numpy as np

src = cv2.imread('./images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!!')
    sys.exit()

# 결과벡터는 float32값으로 변형되어서 나옴
dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

mag = cv2.magnitude(dx, dy)

# 0보다 작은 수는 0 , 255보다 큰 수는 255로 변환
dst = np.clip(mag, 0, 255).astype(np.uint8)

edge = np.zeros(dst.shape[:2], np.uint8)

edge[dst > 120] = 255

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('edge', edge)
cv2.waitKey()

cv2.destroyAllWindows()