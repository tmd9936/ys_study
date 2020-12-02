# Hu's seven invariant moments
# cv2.matchShapes(contour1, pts, cv2.CONTOURS_MATCH_I3, 0)
# 3차 이하의 정규화된 중심 모멘트를 조합하여 만든 7개의 모멘트 값
# 영상으 크기, 회전, 이동, 대칭 변환에 불변

import sys
import numpy as np
import cv2


# 영상 불러오기
obj = cv2.imread('./images/spad.png', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('./images/symbols2.bmp', cv2.IMREAD_GRAYSCALE)

if src is None or obj is None:
    print('Image load failed!')
    sys.exit()

# 외곽선 검출을 위한 이진화
_, obj_bin = cv2.threshold(obj, 128, 255, cv2.THRESH_BINARY_INV)
# 객체의 관계정보를 배제한 일반적인 외곽선 검출
obj_contours, _ = cv2.findContours(obj_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

contour1 = obj_contours[0]

# 입력 영상 분석
# 외곽선 검출을 위한 이진화
_, src_bin = cv2.threshold(src, 128, 255, cv2.THRESH_BINARY_INV)
# 객체의 관계정보를 배제한 일반적인 외곽선 검출
contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 결과 영상
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

# 입력 영상의 모든 객체 영역에 대해서
for pts in contours:
    if cv2.contourArea(pts) < 1000: # 노이즈 제거
        continue

    # 주어진 점을 가득채우는 최소단위 사각형
    rc = cv2.boundingRect(pts)
    cv2.rectangle(dst, rc, (255, 0, 0), 1)

    # 모양 비교
    # matchShapes(contour1, contour2, method, parameter)
    # contour1 메인 객체, contour2 : 비교될 객체
    # method : 수학적 모양 비교 함수
    dist = cv2.matchShapes(contour1, pts, cv2.CONTOURS_MATCH_I3, 0)

    cv2.putText(dst, str(round(dist, 4)), (rc[0], rc[1] - 3),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1, cv2.LINE_AA)




cv2.imshow('obj', obj)
cv2.imshow('dst', dst)
cv2.waitKey(0)