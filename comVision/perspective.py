# 어파인 변환 행렬 구하기
# cv2.getAffineTransform(src, dst)  리턴값 2 X 3 행렬  

# 투시변환 행렬 구하기
# cv2.getPerspectiveTransform(src, dst) 리턴값 3 X 3 행렬

# 어파인 변환함수
# cv2.warfAffine(src, M, dsize, dst, flag, borderMode, borderValue)

# 투시변환 함수
# cv2.warfPerspective(src, M, dsize, dst, flag, borderMode, borderValue)

import math, sys, cv2, numpy as np

src = cv2.imread('./images/name_card_3.jpg')

if src is None:
    print('Image load failed!!')
    sys.exit()

# 일반 명함카드 비율 (9:5)
w, h = 720, 400

# 소스의 좌표
src_Coord = np.array([[228,116],[797, 224], [744,566], [81,381]], np.float32)

# 출력 좌표
dst_Coord = np.array([[0,0], [w-1, 0], [w-1, h-1], [0,h-1]], np.float32)

per_matrix = cv2.getPerspectiveTransform(src_Coord, dst_Coord)
dst = cv2.warpPerspective(src, per_matrix, (w,h))

##############################################################################

src = cv2.imread('./images/name_card_2.jpg')

if src is None:
    print('Image load failed!!')
    sys.exit()

w, h = int(math.sqrt((173**2)+(139**2))), int(math.sqrt((434**2)+(259**2)))

# 소스의 좌표
src_Coord = np.array([[143,275],[316, 145], [697,334], [574,536]], np.float32)

# 출력 좌표
dst_Coord = np.array([[0,0], [w-1, 0], [w-1, h-1], [0,h-1]], np.float32)

per_matrix = cv2.getPerspectiveTransform(src_Coord, dst_Coord)
dst2 = cv2.warpPerspective(src, per_matrix, (w,h))

##############################################################################

src = cv2.imread('./images/name_card_2.jpg')

if src is None:
    print('Image load failed!!')
    sys.exit()

w, h = int(math.sqrt((173**2)+(139**2))), int(math.sqrt((434**2)+(259**2)))

# 소스의 좌표
src_Coord = np.array([[143,275],[316, 145], [697,334], [574,536]], np.float32)

# 출력 좌표
dst_Coord = np.array([[0,0], [w-1, 0], [w-1, h-1], [0,h-1]], np.float32)

per_matrix = cv2.getPerspectiveTransform(src_Coord, dst_Coord)
dst2 = cv2.warpPerspective(src, per_matrix, (w,h))

##############################################################################

src = cv2.imread('./images/name_card_1.jpg')

if src is None:
    print('Image load failed!!')
    sys.exit()

h, w = int(math.sqrt((173**2)+(139**2))), int(math.sqrt((434**2)+(259**2)))

# 소스의 좌표
src_Coord = np.array([[429,628], [348,225], [556,105], [732,508]], np.float32)

# 출력 좌표
dst_Coord = np.array([[0,0], [w-1, 0], [w-1, h-1], [0,h-1]], np.float32)

per_matrix = cv2.getPerspectiveTransform(src_Coord, dst_Coord)
dst3 = cv2.warpPerspective(src, per_matrix, (w,h))

## 샤프닝 작업
ycrcb = cv2.cvtColor(dst3, cv2.COLOR_BGR2YCrCb)
src_y = ycrcb[:,:,0].astype(np.float32)
blur = cv2.GaussianBlur(src_y, (0,0), 5.0)
ycrcb[:, :, 0] = np.clip(2.*src_y - blur, 0, 255).astype(np.uint8)
##

dst3 = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)


#cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.waitKey()
cv2.destroyAllWindows()