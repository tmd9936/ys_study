# 기본적인 2d 필터링

# cv2.filter2d(src, ddepth, kernerl, dst, anchor, delta, borderType)

# src : 입력영상
# ddepth : 출력영상 데이터타입(cv2.CV_8U, cv2.CV_32F, cv2.CV_64F)
# kernel : 필터 마스트 행렬(실수형)
# anchor : 고정점, (-1, -1)이면 중앙점을 anchor로 사용하겠다, 필터를 적용 할 픽셀
# delta : 추가적으로 결과에 더해줄 값
# borderType : 가장자리 픽셀을 확장하는 방식

import sys, cv2, numpy as np

src = cv2.imread('./images/rose.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('not load')
    sys.exit()

# 평균 필터
# kernel = np.array([[1/9,1/9,1/9]
#                  ,[1/9,1/9,1/9]
#                  ,[1/9,1/9,1/9]], dtype=np.float32)

kernel = np.ones((3,3), dtype=np.float64) / 9.

# dst = cv2.filter2D(src, -1, kernel) # -1은 입력영상과 동일한 타입으로 만들겠다는 의미

# cv2.blur(src, ksize) # ksize : 평균 크기(weight, height) 튜플 형태

# 내부적으로 kernel = np.ones((3,3), dtype=np.float64) / 9. 계산
# dst = cv2.blur(src, (3,3))

dst = cv2.blur(src, (3,3), kernel)

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()