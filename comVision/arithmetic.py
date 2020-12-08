# 산술 연산
# cv2.add, cv2.subtract, cv2.addWeighted, cv2.absdiff

import sys, cv2, numpy as np

src1 = cv2.imread('./images/lenna256.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('./images/square.bmp', cv2.IMREAD_GRAYSCALE)
src3 = cv2.imread('./images/blight.bmp', cv2.IMREAD_GRAYSCALE)

dst1 = cv2.add(src1,src2, dtype=cv2.CV_8U)
# cv2.addWeighted(src1, alpha, src2, beta, gammma, dst, dtype)
# src1 : 첫번쨰영상 scr2 : 두번째영상
# alpha : 첫번째 영상의 가중치
# beta : 두번째 영상의 가중치
# gamma : 결과 영상에 추가적으로 더해줄 값
# dtype : 출력(dst) 타입
dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)
dst3 = cv2.subtract(src1, src2)

# cv2.absdiff(src1, src2, dst) : src1 
# : 두 영상의 같은 위치에 존재하는 픽셀값에 대하여 뺄셈 연산을 수행한 후,
# : 그 절대값을 결과영상에 의해 픽셀값으로 설정
dst4 = cv2.absdiff(src1, src2)
dst5 = cv2.add(src1, src3)
dst6 = cv2.subtract(src1, src3)

cv2.imshow('src3', src3)

cv2.imshow('dst1',dst1)
#cv2.imshow('dst2',dst2)
#cv2.imshow('dst3',dst3)
cv2.imshow('dst4',dst4)
cv2.imshow('dst5',dst5)
cv2.imshow('dst6',dst6)

cv2.waitKey()
cv2.destroyAllWindows()