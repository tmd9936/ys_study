# 모폴로지 연산 함수
# morphologyEx(src, op, kernel, dst=Noen, anchor=None, iterations, borderType, borderValue)

# op : 모폴로지 연산 플래그 설정(침식, 팽창, 열기, 닫기)
#      cv2.MORPH_ERODE  : 침식 
#      cv2.MORPH_DILATE : 팽창
#      cv2.MORPH_OPEN   : 열기
#      cv2.MORPH_CLOSS  : 닫기   
#      cv2.MORPH_GRADIENT : 팽창 - 침식

import sys, cv2, numpy as np

src = cv2.imread('./images/rice.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('iamge open failed!!')
    sys.exit()

# 지역 이진화 수행
dst1 = np.zeros(src.shape, np.uint8)

bw = src.shape[1] // 4
bh = src.shape[0] // 4

for y in range(4):
    for x in range(4):
        src_ = src[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
        dst_ = dst1[y*bh:(y+1)*bh, x*bw:(x+1)*bw]

        cv2.threshold(src_, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU, dst_)

# 객체(흰색 덩이리)의 개수를 리턴
cnt1, _ = cv2.connectedComponents(dst1)
print('cnt1 :', cnt1)

# cv2.erode(dst1, None, dst1)
# cv2.dilate(dst1, None, dst1)
# 열기 연산은 노이즈 제거를 함
cv2.morphologyEx(dst1, cv2.MORPH_OPEN, None, dst1)

cnt2, _ = cv2.connectedComponents(dst1)
print('cnt2 :', cnt2)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)

cv2.waitKey()
cv2.destroyAllWindows()