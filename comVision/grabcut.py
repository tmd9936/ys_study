# 그랩컷 함수
# grabCut(img, mask, bgdModel, fgdModel, iterCount, mode=None) -> mask, bgdModel, fgdModel
# img : 입력영상 8비트 3채널
# mask : 입출력 마스크, cv2.GC_BGD(0), cv2.GC_FGD(1), cv2.BC_PR_BGD(2), cv2.BC_PR_FGD(3)
# 네개의 값으로 구성
# rect : ROI 영역, cv2.GC_INIT_WITH_RECT모드에서만 사용
# bgdModel : 임시 배경 모델 행렬
# fgdModel : 임시 전경 모델 행렬
# iterCount : 반복횟수
# mode : cv2.BC_INIT_WITH_RECT, cv2.GC_INIT_WITH_MASK

import sys, cv2, numpy as np

src = cv2.imread('./images/messi.jpg')

if src is None:
    print('Image load failed!!')
    sys.exit()


rc = cv2.selectROI(src)
mask = np.zeros(src.shape[:2], np.uint8)

cv2.grabCut(src, mask, rc, None, None, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')

dst = src * mask2[:, :, np.newaxis]

cv2.imshow('mask', mask2)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()