import sys, cv2, numpy as np

# 영상의 회전 변환 행렬(2 x 3) 구하는 함수
# cv2.getRotationMatrix2S(center, angle, scale)
# center : 회전 중심 좌표
# angle : 회전각도(degree), 음수는 시계방향
# scale : 확대 비율

src = cv2.imread('./images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!!')
    sys.exit()

center_pt =(src.shape[1] / 2, src.shape[0]/2)

# rotation_arr = cv2.getRotationMatrix2D(center_pt, 45, 1)

# dst = cv2.warpAffine(src, rotation_arr, (0,0))

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()

i = 0
while True:
    rotation_arr = cv2.getRotationMatrix2D(center_pt, i, 1)
    # border_default : 원래이미지 이용해서 채우기
    dst = cv2.warpAffine(src, rotation_arr, (0,0), borderValue=255)
    
    cv2.imshow('dst', dst)

    if cv2.waitKey(3) == 27:
        break

    i += 1
    if i==361:
        i== 0

cv2.destroyAllWindows()