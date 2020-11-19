import cv2
import numpy as np
# ROI(Region of Interest) : 관심영역
# : 영상에서 어떤 특정한 연산을 수행하고자 할 때 사용하는 임의의 부분 영역

# 마스크 연산을 하기위한 함수
# cv2.copyTo(src, mask, dst)
# src : 입력영상
# mask : 마스크 영상 : 0과 255로 구분되어있는 영상 (255가 아니어도 됨)
# -> 0이 아닌 값(픽셀)에 대해서만 연산(복사)을 수행
# dst : 출력연산

src = cv2.imread('./images/airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('./images/airplane_mask.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('./images/field.bmp', cv2.IMREAD_COLOR)

# src와 dst는 타입이 같아야 함(grayscale, turecolor)
# cv2.copyTo(src, mask, dst)

# dst영상에 src마스크 영역을 할당해보세요
# 넘파이의 boolean 인덱싱을 이용하여 처리해보기
# dst[mask > 0] = src[mask > 0]

# cv2.imshow('src',src)
# cv2.imshow('mask',mask)
# cv2.imshow('dst',dst)

#################################################################

## 알파채널을 마스크 영상으로 활용하여 영상을 합성하기
dog = cv2.imread('./dog_img.bmp', cv2.IMREAD_COLOR)
logo = cv2.imread('./images/opencv.png', cv2.IMREAD_UNCHANGED)

mask = logo[:, :, 3] # mask는 알파채널로 만드는 역활을 하는 영상
logo = logo[:, :, :-1]

# dog[50:len(mask)+50, 50:len(mask[0])+50] = logo

h, w = mask.shape[:2]
# crop = dog[0:h, 0:w]

# crop은 src의 부분영역을 참조하고 있음. (즉, crop은 src의 부분영역임)
crop = dog[200:200+h, 200:200+w]


#cv2.copyTo(logo, mask, crop)
crop[mask > 0] = logo[mask > 0]

cv2.imshow('dog',dog)
cv2.imshow('logo', logo)
cv2.imshow('mask', mask)


cv2.waitKey()
cv2.destroyAllWindows()