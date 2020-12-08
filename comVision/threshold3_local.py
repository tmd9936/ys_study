# threshold (임계값 함수)
# cv2.threshold(src, thresh, maxval, type, dst) -> retval, dst
# src : 입력영상, thresh : 사용자가 지정한 임계치
# maxval : 무조건 255
# type : cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV 이 두가지 타입이 대부분 사용됨.
# retval : 사용자가 지정한 임계값
# dst : 출력영상

import sys, cv2, numpy as np

# src = cv2.imread('./images/sudoku.jpg', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('./images/rice.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('iamge open failed!!')
    sys.exit()

# 오츠에 의한 전역 이진화
th, dst1 = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY| cv2.THRESH_OTSU)

# 각 지역을 이진화 후 덮어쓸 공간 생성
dst2 = np.zeros(src.shape, np.uint8)

# 4등분
bw = src.shape[1] // 4
bh = src.shape[0] // 4

# src의 지역(src_)을 참조한 다음 threshold로 이진화를 한 후에 참조한 dst지역(dst_)에 덮어씀
for y in range(4):
    for x in range(4):
        src_ = src[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
        dst_ = dst2[y*bh:(y+1)*bh, x*bw:(x+1)*bw]

        # dst_를 파라미터로 사용하면 입력과 동시에 출력으로 사용할 수 있다.
        cv2.threshold(src_, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU, dst_)


cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()
