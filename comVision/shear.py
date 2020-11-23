import sys, cv2, numpy as np

src = cv2.imread('./images/img_1.png')

if src is None:
    print('Image load failed!!')
    sys.exit()

aff = np.array([[1, 0.5, 0],
               [0, 1, 0]], dtype=np.float32)

h, w = src.shape[:2]
print(src.shape)
# dst = cv2.warpAffine(src, aff, (0,0))

dst = cv2.warpAffine(src, aff, (w + int(w*0.5), h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()