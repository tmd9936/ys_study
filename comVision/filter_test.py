import sys, cv2, numpy as np

cap = cv2.VideoCapture('./videos/video1.mp4')

if not cap.isOpened():
    print('video open failed!!')
    sys.exit()

# def filter_1(img):
#     h, w = img.shape[:2]

#     s_img = cv2.resize(img, (int(w//2), int(h//2)))

#     blur = cv2.bilateralFilter(s_img, -1, 20, 8)
#     edge = 255 - cv2.Canny(s_img, 80, 130)
#     edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

#     dst = cv2.bitwise_and(blur, edge)

#     dst = cv2.resize(dst, (w,h), interpolation=cv2.INTER_NEAREST)

#     return dst

def filter_2(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 가우시안 표준편차 3
    blur = cv2.GaussianBlur(gray, (0,0), 3)

    # gray를 blur로 나눠주고 255곱해줌
    dst = cv2.divide(gray, blur, scale=255)

    

    return dst


while True:
    ret, frame = cap.read()

    if not ret:
        break

    # frame = filter_1(frame)
    frame = filter_2(frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
