# 컬러 space

# 색분리(채널 분리)
# cv2.split(m, mv) => dst
# m : 다채널 영상(BGR)으로 구성된 컬러 영상
# mv : 출력 영상
# dst : 출력영상 리스트

# 색결합(채널 결합)
# cv2.merge(mv, dst) = >dst
# mv : 출력 영상
# dst : 출력영상 리스트

## 영상처리에서는 특정 목적에 따라서 RGB 색공간(space)을 HSV, YCrCb
# Grayscale등의 색공간으로 전환해서 처리를 한다.

import sys, cv2, numpy as np

src = cv2.imread('./images/candies.png')

print('src.shape :', src.shape)
print('src.dtype :', src.dtype)

b_channel, g_channel, r_channel = cv2.split(src)

cv2.imshow('src', src)
cv2.imshow("b_channel", b_channel)
cv2.imshow("g_channel", g_channel)
cv2.imshow("r_channel", r_channel)

# cv2.waitKey()

## 색공간 변환 함수 : cv2.cvtColor(src, code, dst, dstCn) => dst
# src : 입력영상, code:색 변환코드, dstCn : 결과영상의 채널 수, dst : 출력영상
# hsv로 변환
# HSV 색공산
# Hue : 색의 종류(무지개색깔)
# Saturatin : 채도, 색이 탁한지 선명한지를 나타내는 정도
# Value : 명도, 빛의 밝기
# HSV 값의 범위
## 0 <= Hue <= 179, 0 <= S, V <= 255
  
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

channels = cv2.split(src_hsv)

cv2.imshow('src', src)
cv2.imshow('channels[0]', channels[0])
cv2.imshow('channels[1]', channels[1])
cv2.imshow('channels[2]', channels[2])
cv2.waitKey()

# YCrCb
# PAL, NTSC 등의 컬러비디오 표준에 사용되는 색공간
# Y : 밝기 정보(luma)
# Cr, Cb: 색차이(chroma)
# Cv2.CV_8U일때 YCrCb값의 범위 : 0 <= Y,Cr,Cb <= 255
