import sys
import numpy as np
import cv2


# 영상 불러오기
src1 = cv2.imread('./images/graf1.png', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('./images/graf3.png', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

# 특징점 알고리즘 객체 생성 (KAZE, AKAZE, ORB 등)
# feature = cv2.KAZE_create()
# feature = cv2.AKAZE_create()
feature = cv2.ORB_create()

# 특징점 검출 및 기술자 계산
kp1, desc1 = feature.detectAndCompute(src1, None)
kp2, desc2 = feature.detectAndCompute(src2, None)

# 특징점 매칭
# SIFT, SURF, KAZE 등의 실수 기술자는 L2 놈(L2 norm)방법을 써야됨
# matcher = cv2.BFMatcher_create()
# AKAZE, ORB, BRIEF 등의 이진 기술자는 아래의 NORM_HAMMING(해밍 거리) 방법을 써야됨
matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING)

# 디스크립트(매칭정보)를 이용하여 매칭을 함
matches = matcher.match(desc1, desc2)
good_matches = matches[:100]

print('# of kp1:', len(kp1))
print('# of kp2:', len(kp2))
print('# of matches:', len(matches))

# 특징점 매칭 결과 영상 생성
dst = cv2.drawMatches(src1, kp1, src2, kp2, good_matches, None)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()