import sys
import numpy as np
import cv2

src = cv2.imread('./images/word.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)

src_bin = cv2.morphologyEx(src_bin, cv2.MORPH_OPEN, None)

src_bin = cv2.morphologyEx(src_bin, cv2.MORPH_DILATE, None)

# 전체 객체 개수 + 1, stats 행렬 (객체의 바운딩 박스 정보)
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)

# 컬러 변환
dst = cv2.cvtColor(src_bin, cv2.COLOR_GRAY2BGR)


# 배경을 제외하기 위해서 1부터 시작
for i in range(1, cnt): 
    # x, y, width, height, area(픽셀개수)
    (x, y, w, h, area) = stats[i] 

    cv2.rectangle(dst, (x, y, w, h), (255, 0, 255), 2) 

cv2.imshow('src', src)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

