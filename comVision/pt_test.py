import sys
import cv2
import glob

imgs = glob.glob('./images/*.jpg')

# for f in imgs:
#     print(f)

# 전체화면으로 각 image를 띄우기
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# 전체화면으로 띄우기
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

#
cnt = len(imgs)
idx = 0

while True:
    img = cv2.imread(imgs[idx])

    if img is None:
        print('Image load failed!!')
        break
    
    cv2.imshow('image', img)
    # 모든 키값은 0보다 큼
    if cv2.waitKey(1000) >= 0:
        break
    idx += 1
    if idx >= cnt:
        idx = 0

cv2.destroyAllWindows()