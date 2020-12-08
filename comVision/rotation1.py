import math, sys, cv2, numpy as np


src = cv2.imread('./images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!!')
    sys.exit()

# degree를 radian 단위로 수정
for i in range(0, 360):
    
    rad = 2 * math.pi * i / 360 # 반시계 방향

    aff = np.array([[math.cos(rad), math.sin(rad), 0],
                    [-math.sin(rad), math.cos(rad), 0]], dtype=np.float32)

    dst = cv2.warpAffine(src, aff, (0,0))


    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    if cv2.waitKey(1) == 27:
        break


cv2.destroyAllWindows()