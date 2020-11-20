import sys, cv2, numpy as np
import matplotlib.pyplot as plt

# 히스토그램 스트레칭(Histogram stretching)
# 영상의 히스토그램이 그레이스케일 전체에 겊쳐 나타나도록 변경하는 선형 변환 기법
# : 영상의 명암비를 자동으로 조절하는 기법
# 정규화 함수 : cv2.normalize(src, dst, alpha, beta, norm_type, dtype, mask)

# 히스토그램 평활화(histogram equalization)
# : 히스토그램 평탄화, 전체 그레이스케일 구간에 히스토그램이 분포되도록 하는 명암비 향상 비법
# 함수 : cv2.equalizeHist(src, dst) => dst
# src : 입력영상, 그레이스케일 영상
def getHistDraw(hist):
    imgHist = np.full((100,256), 255, dtype=np.uint8)

    histMax = np.max(hist)
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        cv2.line(imgHist, pt1, pt2, 0)

    return imgHist

src = cv2.imread('./images/snow.png', cv2.IMREAD_GRAYSCALE)
src_hist = cv2.calcHist([src], [0], None, [256], [0, 256])
src_hd = getHistDraw(src_hist)

if src is None:
    print('Image load failed !!')
    sys.exit()

dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
dst_hist = cv2.calcHist([dst], [0], None, [256], [0,256])
dst_hd = getHistDraw(dst_hist)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('src_hd', src_hd)
cv2.imshow('dst_hd', dst_hd)

cv2.waitKey()
cv2.destroyAllWindows()