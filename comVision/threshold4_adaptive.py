# adaptiveThreshold 함수를 이용한 지역 이진화
# adaptiveThreshold(src, macValue, adaptiveMethod, thresholdType, blockSize, C, dst)
# src : 그레이스케일 영상(입력), maxValue: 255
# adaptiveMethod : 블록 평균 계산 방법 지정, cv2.ADAPTIVE_THRESH_MEAN_C(평균) 
#                  cv2.ADAPTIVE_THRESH_GAUSSIAN_C(가중치 평균)  
# thresholdType : BINARY, BINARY_INV
# blockSize : 보통 홀수로 지정(3이상 값)
# C : 보정 상수로서 adaptive에 계산된 값에서 양수면 빼주고 음수면 더해준다. 
# 픽셀단위(blockSize)마다 이진화 처리를 하는 방법이라서 수동보다 시간이 더 오래걸림

# cv2.ADAPTIVE_THRESH_MEAN_C: X, Y를 중심으로 block Size * block Size 안에 있는 픽셀 값의 평균에서 C를 뺸 값을 문턱값으로 함 
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C: X, Y를 중심으로 block Size * block Size 안에 있는 Gaussian 윈도우 기반 가중치들의 합에서 C를 뺀 값을 문턱값으로 한다. 

import sys, cv2, numpy as np

src = cv2.imread('./images/sudoku.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('iamge open failed!!')
    sys.exit()

def on_trackbar(pos):
    bsize = pos
    if bsize % 2 == 0:
        bsize = bsize - 1
    if bsize < 3:
        bsize = 3

    dst = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, bsize, 5) 

    cv2.imshow('dst', dst)

cv2.imshow('src', src)
cv2.namedWindow('dst')
cv2.createTrackbar('Block Size', 'dst', 0, 200, on_trackbar)
cv2.setTrackbarPos('Block Size', 'dst', 11)

cv2.waitKey()
cv2.destroyAllWindows()
