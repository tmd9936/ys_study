import matplotlib.pyplot as plt
import cv2

# 컬러영상 출력
# openCV는 BGR 순서
imgBGR = cv2.imread('./dog_img.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.axis('off')
# plt.imshow(imgBGR)
# plt.imshow(imgRGB)
# plt.show()

# 그레이 스케일 영상 출력하기
imgGray = cv2.imread('./dog_img.bmp', cv2.IMREAD_GRAYSCALE) 
# plt.imshow(imgGray, cmap='gray')
# plt.show()

# subplot을 이용한 영상 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()