# 영상 다운 샘플링
# cv2.pyrDown(src, dst, dstsize, borderType)
# src : 입력영상, dst:출력영상
# dstsize: 출력영상크기, 따로 설정하지 않는 경우 입력영상의 가로, 세로 1/2크기로 설정(원이미지의 1/4크기)

import sys, cv2, numpy as np
import math

src = cv2.imread('./images/puppy.png')

if src is None:
    print('Image load failed!!')
    sys.exit()

cv2.imshow("src_origin", src)


for i in range(1,4):
    src = cv2.pyrDown(src)
    cpy = src.copy()
    cv2.imshow('src', cpy)
    cv2.waitKey()
    cv2.destroyWindow('src')

cv2.destroyAllWindows()