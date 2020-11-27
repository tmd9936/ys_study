import sys, cv2, numpy as np

ref = cv2.imread('./images/k1.png', cv2.IMREAD_COLOR)
mask = cv2.imread('./images/k1_mask.bmp', cv2.IMREAD_GRAYSCALE)

if ref is None or mask is None:
    print('image load failed!')
    sys.exit()

ref_ycrcb = cv2.cvtColor(ref, cv2.COLOR_BGR2YCrCb)
channels = [1, 2]
ranges = [0, 256, 0, 256]
hist = cv2.calcHist([ref_ycrcb], channels, mask, [128, 128], ranges)

hist_norm = cv2.normalize(hist, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# 역투영 적용 이미지
src = cv2.imread('./images/k2.png', cv2.IMREAD_COLOR)
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)

h, w = src.shape[:2]
dst = np.zeros((h, w, 3), np.uint8)
dst[backproj > 30] = src[backproj > 30]

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()