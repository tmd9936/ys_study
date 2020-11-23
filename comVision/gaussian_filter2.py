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

cv2.imshow('src', src)

for sigma in range(1,6):
    dst = cv2.GaussianBlur(src, (0,0), sigma)
    
    desc = 'sigma {}'.format(sigma)
    cv2.putText(dst, desc , (10, 30), cv2.FONT_HERSHEY_TRIPLEX, 1.0, 255, 1, cv2.LINE_AA)
    
    cv2.imshow('dst', dst)
    cv2.waitKey()


cv2.destroyAllWindows()