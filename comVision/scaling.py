import sys, cv2, numpy as np

src = cv2.imread('./images/rose2.bmp')

if src is None:
    print('Image load failed!!')
    sys.exit()

# cv2.resize(src, dsize, dst, fx, fy, interpolation)
# src: 입력영상, dize: 출력영상 크기(w,h), (0,0,)이면 fx,fy값을 이용해서 결정
# fx, fy : x와 y의 스케일 비율(scale factor)
# interpolation : 보간법

dst = cv2.resize(src, (0,0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)

dst2 = cv2.resize(src, (1920,1280))
dst3 = cv2.resize(src, (1920,1280), interpolation=cv2.INTER_CUBIC)
dst4 = cv2.resize(src, (1920,1280), interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('src', src)
cv2.imshow('dst', dst[500:800, 400:800])
cv2.imshow('dst2', dst2[500:800, 400:800])
cv2.imshow('dst3', dst3[500:800, 400:800])
cv2.imshow('dst4', dst4[500:800, 400:800])
cv2.waitKey()
cv2.destroyAllWindows()