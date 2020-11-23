import sys, cv2, numpy as np

src = cv2.imread('./images/noise.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!!')
    sys.exit()

# cv2.medianBlur(src, ksize, dst)

# 이미지가 뭉치는 현상이 발생함(그림처럼 보임)
dst = cv2.medianBlur(src, 3)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()