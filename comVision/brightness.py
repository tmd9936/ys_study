# 영상 화소 처리(Pint processing)
# : 특정 좌표의 픽셀 값을 변경하여 출력영상의 해당 좌표 픽셀값으로 설정

# 밝기 조절 : cv2.add(src1, src2, dst, mask, dtype)
# src1 : 첫번째 영상 또는 스칼라값(입력)
# src2 : 두번째 영상 또는 스칼라값(입력)
# dst : 덧셈 연산 결과 영상(출력)
# mask : 마스크 영상
# dtype : 출력 영상 타입

import numpy as np
import cv2
import sys

# src = cv2.imread('./images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

# if src is None:
#     print('Image load failed!!')
#     sys.exit()

# dst = cv2.add(src, 100)

# cv2.imshow('src',src)
# cv2.imshow('dst',dst)
# cv2.waitKey()

## 컬러영상
src = cv2.imread('./images/lenna.bmp')
if src is None:
    print('Image load failed!!')
    sys.exit()

# dst = cv2.add(src,100) # 파란색 톤만 밝아짐
dst = cv2.add(src, (100,100,100,0))

# 밝기 조절 수식 : dst(x, y) = saturate(src(x, y) + n)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()


cv2.destroyAllWindows()




