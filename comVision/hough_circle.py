import sys, cv2, numpy as np

src = cv2.imread('./images/old_tel.png')

if src is None:
    print('Image load failed!!')
    sys.exit()

# 블러처리 해서노이즈 제거하면 성능이 좋아짐
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (0,0), 1.0)

# 허프변환을 이용한 원 검출 함수
# cv2.HoughCircles(image, method, dp, minDist, circles=None, param1=None, param2=None, minRadius=None, maxRadius=None)
# image : 일반 영상(에지 영상 아님), 에지영상에서는 방향성분을 알수없음
# method : OpenCV 4.2 이하에서는 cv2.HOUGH_GRADIENT를 지정해야 함.
# dp : 축적배열의 크기 비율 기본값 : 1을 넣어주면 됨
# minDist : 검출된 원의 중심점들의 최소거리
# circles : (cx, cy, r) 정보를 갖고있는 np.ndarray, shape=(1, N, 3), dtype=np.float32
# param1 : Canny 에지 검출기의 높은 임계값, param2 : 축적배열에서 원 검출을 하기위한 임계값
## param1 값이 결정되면 낮은 임계값은 param1의 1/2값으로 결정됨-
## param2 값에 따라 많은 원이 검출될 수 있고 원이 검출 안될 수 있음.

def on_level_changed(pos):
    rmin = cv2.getTrackbarPos('minRadius', 'img')
    rmax = cv2.getTrackbarPos('maxRadius', 'img')
    th = cv2.getTrackbarPos('threshold', 'img')
    param1 = cv2.getTrackbarPos('param1', 'img')

    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 20,
            param1=param1, param2=th, minRadius=rmin, maxRadius=rmax)

    dst = src.copy()
    if circles is not None:
        for circle in circles[0,:]:
            cx, cy, r = circle
            cv2.circle(dst, (cx,cy), r, (0,0,255), 2, cv2.LINE_AA)
    
    cv2.imshow('img', dst)
# old_tel1.png는 mindist=20, rmin=5, rmax=60, th=36 일 경우 깨끗하게 구해짐


cv2.imshow('img', src)

cv2.createTrackbar('minRadius', 'img', 0, 100, on_level_changed)
cv2.createTrackbar('maxRadius', 'img', 0, 150, on_level_changed)
cv2.createTrackbar('threshold', 'img', 0, 100, on_level_changed)
cv2.createTrackbar('param1', 'img', 0, 255, on_level_changed)
cv2.setTrackbarPos('minRadius', 'img', 10)
cv2.setTrackbarPos('maxRadius', 'img', 80)
cv2.setTrackbarPos('threshold', 'img', 40)
cv2.setTrackbarPos('param1', 'img', 125)

cv2.waitKey()
cv2.destroyAllWindows()
