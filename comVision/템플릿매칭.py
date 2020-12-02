import sys
import numpy as np
import cv2


# 입력 영상 & 템플릿 영상 불러오기
# 검색될 큰 이미지
src = cv2.imread('./images/mainboard1.bmp', cv2.IMREAD_GRAYSCALE)
# 매칭할 작은 이미지 템플릿
templ = cv2.imread('./images/mainboard_tem.bmp', cv2.IMREAD_GRAYSCALE)

if src is None or templ is None:
    print('Image load failed!')
    sys.exit()

noise = np.zeros(src.shape, np.int32)

# noise각 원소에 평균 50, 표준편차 10인 값들을 넣음
cv2.randn(noise, 50, 10)

# src에 노이즈 값을 더함
# CV_8UC3 : 부호 없는 8비트 정수화소, 3-채널 영상 
src = cv2.add(src, noise, dtype=cv2.CV_8UC3)

# 템플릿 매칭
# 출력값의 범위는 -1 ~ 1, 실수형 행렬로 결과가 나온다.
res = cv2.matchTemplate(src, templ, cv2.TM_CCOEFF_NORMED)

# 스케일링, 명암비 조절
res_norm = cv2.normalize(res, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# minimum value, maximum value, minimum location, maximum location 리턴
# 명암이 최대인 장소
_, maxv, _, maxloc = cv2.minMaxLoc(res)
print('maxv:', maxv)
print('maxloc:', maxloc)

# 매칭이 되는 부분은 하얗게 변함
th, tw = templ.shape[:2]
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
cv2.rectangle(dst, maxloc, (maxloc[0] + tw, maxloc[1] + th), (0, 0, 255), 2)

cv2.imshow('res_norm', res_norm)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()      

