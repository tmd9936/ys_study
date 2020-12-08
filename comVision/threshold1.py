# threshold (임계값 함수)
# cv2.threshold(src, thresh, maxval, type, dst) -> retval, dst
# src : 입력영상, thresh : 사용자가 지정한 임계치
# maxval : 무조건 255
# type : cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV 이 두가지 타입이 대부분 사용됨.
# retval : 사용자가 지정한 임계값
# dst : 출력영상

import sys, cv2, numpy as np


src = cv2.imread('./images/cell1.jpg', cv2.IMREAD_GRAYSCALE)


def on_change_threshold(pos):
    thr = cv2.getTrackbarPos('threshold', 'dst')
    
    _, dst = cv2.threshold(src, thr, 255, cv2.THRESH_BINARY)

    cv2.imshow('dst', dst)

if src is None:
    print('iamge open failed!!')
    sys.exit()

# _, dst = cv2.threshold(src, 150, 255, cv2.THRESH_BINARY) # retval값을 받지 않는 것으로 처리
_, dst = cv2.threshold(src, 200, 255, cv2.THRESH_BINARY)


# cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.createTrackbar('threshold', 'dst', 0, 255, on_change_threshold)
cv2.setTrackbarPos('threshold', 'dst', 128)

cv2.waitKey()
cv2.destroyAllWindows()
