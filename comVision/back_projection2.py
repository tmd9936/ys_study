import sys, cv2, numpy as np

# 역투영
# CrCb의 살색 히스트그램을 얻어오기

referenc_img = cv2.imread('./images/son2.png')
mask = cv2.imread('./images/son2_mask.bmp', cv2.IMREAD_GRAYSCALE)

ref_ycrcb = cv2.cvtColor(referenc_img, cv2.COLOR_BGR2YCrCb)

# CrCb 채널 가져옴
channels = [1,2]
ranges = [0, 256, 0, 256]
hist = cv2.calcHist([ref_ycrcb], channels, mask, [128, 128], ranges)

hist_norm = cv2.normalize(hist, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

##
src = cv2.imread('./images/ki.png')
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)


cv2.imshow('src', src)
cv2.imshow('hist_norm', hist_norm)

cv2.imshow('backproj', backproj)

cv2.waitKey()
cv2.destroyAllWindows()