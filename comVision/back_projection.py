# 히스토그램 역투영(back projection)
# 히스토그램 역투영 함수
# calcBackproject(images, channels, hist, ranges, scale, dst)

# 영역을 선택할 수 있도록 하는 함수
# cv2.selectROI(src)

import sys, cv2, numpy as np

src = cv2.imread('./images/grass_land.png')

if src is None:
    print("Image load failed!!")
    sys.exit()

# ROI selector 창 생성(영역을 선택할 수 있는 창 생성) 
x,y,w,h = cv2.selectROI(src)
# cv2.imshow('src', src)


scr_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
crop_zone = scr_ycrcb[y:y+h, x:x+w]

channels = [1,2]
# 막대갯수
histSize = [128, 128]
cr_range = [0, 256]
cb_range = [0, 256]
ranges = cr_range + cb_range

hist = cv2.calcHist([crop_zone], channels, None, histSize, ranges)
hist_norm = cv2.normalize(hist, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# 입력 영상 전체에 대한 히스토그램 역투영
backproj = cv2.calcBackProject([scr_ycrcb], channels, hist, ranges, 1)
dst = cv2.copyTo(src, backproj)

cv2.imshow('backproj', backproj)
cv2.imshow('hist_norm', hist_norm) # 초원의 히스토그램
cv2.imshow('dst', dst)
cv2.waitKey()




cv2.destroyAllWindows()