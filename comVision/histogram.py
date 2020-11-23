# 히스토그램
# 영상의 픽셀값 분포를 그래프 형태로 표현한 것
# 히스토그램 구하는 함수
# cv2.calcHist(images, channels, mask, histSize, ranges, hist=None, accumulate)
# images : 입력영상 리스트, channels: 히스토그램을 얻기위한 채널리스트
# mask : 마스크영상, hitSize : 막대(bin)의 개수를 나타내는 리스트 
# ranges: 히스토그램 각 차원의 최소, 최대값으로 구성된 리스트
# hist : 계산된 히스토그램
# accumulate: 기존의 hist 히스토그램에 누적여부(True/False)

# 명암비(Contrast): 어두운곳과 밝은곳의 밝기 차이

# 히스토그램 스트레칭(Histogram stretching)
# 영상의 히스토그램이 그레이스케일 전체에 겊쳐 나타나도록 변경하는 선형 변환 기법
# : 영상의 명암비를 자동으로 조절하는 기법
# 정규화 함수 : cv2.normalize(src, dst, alpha, beta, norm_type, dtype, mask)

# 히스토그램 평활화(histogram equalization)
# : 히스토그램 평탄화, 전체 그레이스케일 구간에 히스토그램이 분포되도록 하는 명암비 향상 비법
# 함수 : cv2.equalizeHist(src, dst) => dst
# src : 입력영상, 그레이스케일 영상

import sys, cv2, numpy as np
import matplotlib.pyplot as plt

# 흑백 영상 히스토 그램
src = cv2.imread('./images/lenna.bmp', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([src], [0], None, [256], [0,256])

# cv2.imshow('src', src)

# plt.plot(hist)
# plt.show()

# 컬러 영상 히스토그램
src = cv2.imread('./images/lenna.bmp')

colors = ['b', 'g', 'r']
bgr_channels = cv2.split(src)

for (channel, c) in zip(bgr_channels, colors):
    hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
    plt.plot(hist, color = c)

cv2.imshow('src', src)
cv2.waitKey(1)

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()