# 영상의 속성

import cv2

# img1은 numpy.ndarray 타입이다.
# openCV는 영상데이터를 표현할 때 numpy.ndarray로 표현
img1 = cv2.imread('./dog_img.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('./dog_img.bmp', cv2.IMREAD_COLOR)

print(type(img1))
print(img1.shape)
print(img2.shape)
print(img2.dtype)

if len(img1.shape) == 2:
    print("img1은 그레이스케일")
elif len(img1.shape) == 3:
    print('img1은 트루컬러')

# img2의 이미지 사이즈 출력하기
h, w = img2.shape[:2]
print('img2 사이즈 : {} x {}'.format(w,h))

h, w = img1.shape
print('img2 사이즈 : {} x {}'.format(w,h))

## 영상의 픽셀값 참조
x = 20
y = 10
p1 = img1[y, x]
print(p1)

p2 = img2[y, x]
print(p2)

# 영상에 값을 넣어보기
img1[y,x] = 0
img2[y,x] = [50,50,250]

'''
for y in range(h):
    for x in range(w):
        img1[y, x] = 255
        img2[y, x] = (0,255,255)
'''

img1[:,:] = 255
img2[:,:] = (0, 0, 255)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.waitKey()

cv2.destroyAllWindows()

















