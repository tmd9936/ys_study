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
# feature = cv2.KAZE_create() # (디스크립터로 계산을 안한 경우, 방향이 모두 0도로 나타남)
# feature = cv2.AKAZE_create() # 디스크립터로 방향까지 계산함 KAZE보다 속도가 빠름
feature = cv2.ORB_create(1000) # 속도는 빠르지만 정확도가 떨어짐, 파라미터는 검출할 keypoint의 개수


# 특징점 검출
kp1 = feature.detect(src1)
kp2 = feature.detect(src2)

print('# of kp1:', len(kp1))
print('# of kp2:', len(kp2))

# 검출된 특징점 출력 영상 생성
# 반지름은 벡터방향 원은 벡터 크기
dst1 = cv2.drawKeypoints(src1, kp1, None,
                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
dst2 = cv2.drawKeypoints(src2, kp2, None,
                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)



cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()