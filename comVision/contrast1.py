import sys, cv2, numpy as np

src = cv2.imread('./images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed !!')
    sys.exit()

# 명암비를 조절하는 수식
# dst(x, y) = np.clip((1+alpha)*src - 128*alpha, 0, 255)

alpha = 2.0
dst = np.clip((1+alpha)*src - 128*alpha, 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()








