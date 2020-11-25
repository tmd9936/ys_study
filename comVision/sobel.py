import sys, cv2, numpy as np

src = cv2.imread('./images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!!')
    sys.exit()

# kernel = np.array([[-1, 0, 1],
#                    [-2, 0, 2],
#                    [-1, 0, 1]], dtype=np.float32)

# kernel2 = np.array([[-1, -2, 1],
#                    [0, 0, 0],
#                    [1, 2, 1]], dtype=np.float32)

# dx = cv2.filter2D(src, -1, kernel, delta=128)
# dy = cv2.filter2D(src, -1, kernel2, delta=128)

# 소벨 필터함수
# cv2.Sobel(src, ddepth, dx, dy, dst=None, ksize=None, scale=None, delta=None, borderType=None)
# src : 입력영상, depth: 출력영상 데이터차입, -1이면(=입력영상) cv2.CV_32F로 연산하는게 일반적임
# dx : x방향 미분지순, dy: y방량 미분지수(1차미분 또는 2차미분 지정)
# dx=1, dy=0으로 dx=0, dy=1로 설정하는것이 일반적인 방법
# ksize는 보통 3으로 지정, scale : 연산결과에 추가적으로 곱할 값(기본값:1)
# delta : 연산결과에 추가적으로 더할 값(기본값: 0)
# borderType : 가장자리 픽셀 확장 방식, 기본값은 cv2.BORDER_DEFAULT

# 샤르 필터(파라미터는 소벨과 동일)
# cv2.Scharr(src, ddepth, dx, dy, dst=None, ksize=None, scale=None, delta=None, borderType=None)

dx = cv2.Sobel(src, -1, 1, 0, delta=128)
dy = cv2.Sobel(src, -1, 0, 1, delta=128)

cv2.imshow('src', src)
cv2.imshow('dx', dx)
cv2.imshow('dy', dy)

cv2.waitKey()

cv2.destroyAllWindows()