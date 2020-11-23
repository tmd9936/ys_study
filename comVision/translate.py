import sys, cv2, numpy as np

src = cv2.imread('./images/img_1.png')

if src is None:
    print('Image load failed!!')
    sys.exit()

# 영상의 어파인 변환 함수
# cv2.warpAffine(src, M, dsize, dst, flags, boarderMode, boorerValue)
# src : 입력영상, M ; 2x3 어파인 변환 행렬, 실수형
# dsize : 결과영상 크기(w,h), (0,0)이면  입력영상과 같은 크기로 설정
# flags : 보간법(기본값은 cv2.INTER_LINEAR)을 설정하는 파라미터
# 보간법 : 결과영상의 퀄리티를 보정하는 방법(cv2.INTER_LINEAR)
# cv2.INTER_NEAREST
# cv2.INTER_LINEAR(효율성이 가장높다. 퀄리티 및 속도 빠름)
# cv2.CUBIC (LINEAR보다 퀄리티는 좋으나 속도 느림)
# cv2.INTER_LANCZOS4 (CUBIC보다 퀄리티는 좋으나 속도 느림)
# cv2.INTER_AREA( 영상 축소시 효과적으로 사용)

aff = np.array([[1,0,300], # 가로이동 크기
               [0,1,200]], dtype=np.float32) # 세로이동 크기


dst = cv2.warpAffine(src, aff, (0,0))


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()