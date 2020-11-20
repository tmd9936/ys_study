import sys, cv2, numpy as np
import matplotlib.pyplot as plt

# 그레이스케일 영상의 히스토그램 평활화

src = cv2.imread('./images/snow.png', cv2.IMREAD_GRAYSCALE)

dst = cv2.equalizeHist(src)

cv2.imshow('src', src)
cv2.imshow('dst', dst)

# 컬러영상 히스토그램 평활화
# BGR을 나눠서 각각 평활화를 -> 각각의 색상 성분이 바뀐상태에서 다시 합치면 전혀 다른 색상이 나올 수 있음
# YCrCb는 Y(밝기)만 평활화하면 색상성분은 그대로인 상태에서 밝기만 평활화된 이미지로 보임

src = cv2.imread('./images/snow.png')

# YCrCb로 변환
cvtsrc = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

# 성분 나누기
ycrcb = cv2.split(cvtsrc)

# 밝기 평활화
ycrcb[0] = cv2.equalizeHist(ycrcb[0])

# 합치기
msrc = cv2.merge(ycrcb)

# BGR로 변환
last = cv2.cvtColor(msrc, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('last', last)

############################################################

# candies = cv2.imread('./images/snow.png')

# s_candy = cv2.split(candies)

# for i in range(3):
#     s_candy[i] = cv2.equalizeHist(s_candy[i])

# m_candy = cv2.merge(s_candy)

# cv2.imshow('candies', candies)
# cv2.imshow('m_candy',m_candy)




cv2.waitKey()
cv2.destroyAllWindows()