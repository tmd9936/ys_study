import sys, cv2, numpy as np

src = cv2.imread('./images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!!')
    sys.exit()


# cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)
# Parameters:	
# d – filtering시 고려할 주변 pixel 지름
# sigmaColor – Color를 고려할 공간. 숫자가 크면 멀리 있는 색도 고려함.
# sigmaSpace – 숫자가 크면 멀리 있는 pixel도 고려함.

dst = cv2.bilateralFilter(src, 9, 50, 50)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()