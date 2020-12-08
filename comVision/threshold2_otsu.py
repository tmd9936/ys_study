# threshold (임계값 함수)
# cv2.threshold(src, thresh, maxval, type, dst) -> retval, dst
# src : 입력영상, thresh : 사용자가 지정한 임계치
# maxval : 무조건 255
# type : cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV 이 두가지 타입이 대부분 사용됨.
# retval : 사용자가 지정한 임계값
# dst : 출력영상

import sys, cv2, numpy as np

# src = cv2.imread('./images/cell3.jpg', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('./images/rice.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('iamge open failed!!')
    sys.exit()

# 오츠 알고리즘을 사용하는 경우 지정한 thresh을 무시하고 otsu가 알아서 내부적으로 계산
# th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU) 와 cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) 는 같음
th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

print("오츠의 임계치 :", th)

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()
