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

# 히스토그램 스트레칠(Histogram stretching)
# 영상의 히스토그램이 그레이스케일 전체에 걸쳐 나타나도록 변경하는 선형 변환 기법
# : 영상의 명암비를 자동으로 조절하는 기법
# 정규화 함수 : cv2.normalize(src, dst, alpha, beta, norm_type, dtype, mask)

# 히스토그램 평활화(histogram equalization)
# : 히스토그램 평탄화, 전체 그레이스케일 구간에 히스토그램이 분포되도록 하는 명암비 향상 비법
# 함수 : cv2.equalizeHist(src, dst) => dst
# src : 입력영상, 그레이스케일 영상

import sys, cv2, numpy as np
import matplotlib.pyplot as plt

def getHistDraw(hist):
    imgHist = np.full((100,256), 255, dtype=np.uint8)

    histMax = np.max(hist)
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        cv2.line(imgHist, pt1, pt2, 0)

    return imgHist

src = cv2.imread('./images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!!')
    sys.exit()

hist = cv2.calcHist([src], [0], None, [256], [0, 256])
print(hist)

hc = getHistDraw(hist)

cv2.imshow('src', src)
cv2.imshow('hc', hc)

plt.plot(hist)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()