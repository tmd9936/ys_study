import numpy as np
import cv2


# 영상 생성하기
# img1 = np.empty((240,320), dtype=np.uint8) # grayscale
# img2 = np.zeros((240,320, 3), dtype=np.uint8) # color image
# img3 = np.ones((240,320), dtype=np.uint8)
# img4 = np.full((240,320,3), (0,255,0), dtype=np.uint8)

# cv2.imshow("img1", img1)
# cv2.imshow("img2", img2)
# cv2.imshow("img3", img3)
# cv2.imshow("img4", img4)
# cv2.waitKey()

# cv2.destroyAllWindows()

# 복사하기
# img1 = cv2.imread('./images/cat_test.jpg')

# img2 = img1 # 참조이미지, 얕은 복사
# img3 = img1.copy() # 메모리에새로 할당한 복사본, 깊은 복사

# img1 [:,:] = (0,255,0)


# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.imshow('img3', img3)
# cv2.waitKey()

# 부분적 영상 추출
img1 = cv2.imread('./dog_img.bmp')

img2 = img1[40:120, 10:150] # numpy.ndarray라서 슬라이싱 가능
img3 = img2.copy() 

# img1[:,:] = (0,255,255)
# img2.fill(0) # 잘라온 영상에 값을 채웠을 때 원본에도 값이 채워진다.

cv2.circle(img2, (20,20), 10, (0,0,255), 2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()












