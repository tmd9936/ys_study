# cv2.GaussianBlur(src, ksize, sigmaX, dst, sigmaY, borderType)
# src: 입력영상, 
# ksize: 가우시안 커널크기, (0,0)으로 지정하면 sigma값에 의해서 자동으로 값이 결정됨
# sigmaX: x방향의 표준편차
# sigmaY: y방향의 표준편차, 0이면 sigmaX와 동일하게 설정
# borderType : 가장자리 픽셀을 확장하는 방식

import sys, cv2, numpy as np

src = cv2.imread('./images/rose.png', cv2.IMREAD_GRAYSCALE)
if src is None:
    print('not load')
    sys.exit()

# blur를 더 주고자 할 때는 2,3으로 입력(값이 커질수록 연산량 증가)
# 시그마가 1일때는 unint8에서 mean(7,7)
dst = cv2.GaussianBlur(src, (0,0), 2) 
dst2 = cv2.blur(src, (7,7))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()