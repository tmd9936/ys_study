import sys, cv2, numpy as np

src = cv2.imread('dog_img.bmp')

# dst = src.copy()

# for i in range(len(dst)):
#     for j in range(len(dst[i])):
#         dst[i,j,0] = np.clip(dst[i,j,0] + 100, 0, 255).astype(np.uint8)
#         dst[i,j,1] = np.clip(dst[i,j,1] + 100, 0, 255).astype(np.uint8)
#         dst[i,j,2] = np.clip(dst[i,j,2] + 100, 0, 255).astype(np.uint8)


# cv2.rectangle(src, (530,150), (620,210), (0,0,255), 1, cv2.LINE_AA)
# cv2.rectangle(src, (695,120), (790,200), (0,0,255), 1, cv2.LINE_AA)

# trn = np.array([[1, 0, 300], [0, 1, 200]], dtype=np.float32)
# dst = cv2.warpAffine(src, trn, (0, 0))

kernel = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]], dtype=np.float32)

dx_img = cv2.filter2D(src, 0, kernel)

cv2.imshow('src', src)
cv2.imshow('dx_img', dx_img)

cv2.waitKey()
cv2.destroyAllWindows()

