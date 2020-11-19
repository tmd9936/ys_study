import sys
import cv2
import numpy as np

# setMouseCallback(windowname, onMouse, param)
# windowName : 마우스 이벤트 처리를 수행할 창이름
# onMouse : 마우스 이벤트 처리를 위한 콜백함수 이름
# param : 콜백함수에 전달 할 데이터

# onMouse(event, x, y, flags, param) : 이벤트 처리 함수
# event : 마우스 이벤트 종류(클릭, 드레그, 이동...), cv2.EVENT_로 시작하는 상수
# x, y : 이벤트 발생 좌표
# flags : 마우스 이벤트가 발생했을 때의 상태
# param : setMouseCallback

# flags
# cv2.EVENT_FLAG_LBUTTON  : 1 (마우스 왼쪽 버튼이 눌렸을 때)
# cv2.EVENT_FLAG_RBUTTON  : 2 (마우스 오른쪽 버튼이 눌렸을 때)
# cv2.EVENT_FLAG_MBUTTON  : 4 (마우스 가운데 버튼이 눌렸을 때)
# cv2.EVENT_FLAG_CTRLKEY  : 8 (컨트롤 키가 눌렸을 때)
# cv2.EVENT_FLAG_SHIFTKEY : 16 (쉬프트 키가 눌렸을 때)
# cv2.EVENT_FLAG_ALTKEY   : 32 (알트 키가 눌렸을 때)



img = np.ones((480, 640, 3), dtype=np.uint8) * 255
px = 0
py = 0

def on_mouse(event, x, y, flags, param):
    global img, px, py
    if event == cv2.EVENT_LBUTTONDOWN:
        print('EVENET_LBUTTONDOWN: {}, {}'.format(x, y))
        px, py = x, y
        # cv2.rectangle(img, (50, 200, 150, 150), (153,223,54), 10)

    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENET_LBUTTONUP: {}, {}'.format(x, y))        

    elif event == cv2.EVENT_MOUSEMOVE:
        # 비트 연산자 
        if flags & cv2.EVENT_LBUTTONDOWN:
            # print('EVENET_MOUSEMOVE: {}, {}'.format(x, y))
            # cv2.circle(img, (x, y), 5, (0,0,255), -1)
            cv2.line(img, (px,py), (x,y), (55,100,100), 5, cv2.LINE_AA)
            px, py = x, y
            cv2.imshow("image", img)

cv2.namedWindow("image")
cv2.setMouseCallback("image", on_mouse)

cv2.imshow("image", img)
cv2.waitKey()

cv2.destroyAllWindows()

