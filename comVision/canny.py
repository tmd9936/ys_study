import sys, cv2, numpy as np

# Canny edge 검출함수
# cv2.Canny(image, threshold1, threshold2, edge=None, apertureSize=None, L2gradient=None)
# image : 입력영상
# threshold1 : low 임계값, threshold2 : high 임계값 => 비율 1:2 또는 1:3을 많이 사용
# edge : 결과벡터
# apertureSize : 소벨연산용 커널, 기본값은 3
# L2gradient : True이면 L2 norm, False이면 L1 norm, 기본값은 False 

#src = cv2.imread('./images/lenna.bmp', cv2.IMREAD_GRAYSCALE)
# src = cv2.imread('./images/bd1.png', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('./images/bd2.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!!')
    sys.exit()

dst = cv2.Canny(src, 100, 200)

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()

cv2.destroyAllWindows()