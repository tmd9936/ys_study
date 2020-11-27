import math, sys, cv2, numpy as np


# 입력 영상 불러오기
src = cv2.imread('./images/coin3.jpg')

if src is None:
    print('iamge open failed!!')
    sys.exit()

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (0,0), 1)

# 허프변환 원 검출 함수 사용
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 30, 
    param1=150, param2=40, minRadius=60, maxRadius=120)

sum_of_money = 0
dst = src.copy()
# 원 검출 결과 및 동전 금액 출력
for circle in circles[0,:]:
    cx, cy, radius = circle
    cv2.circle(dst, (cx,cy), radius, (0,0,255), 2, cv2.LINE_AA)

    # 동전 영역 분분 영상 추출
    x1 = int(cx - radius)
    y1 = int(cy - radius)
    x2 = int(cx + radius)
    y2 = int(cy + radius)
    radius = int(radius)

    print(radius)

    crop = dst[y1:y2, x1:x2, :]
    ch, cw = crop.shape[:2]

    # 동전 영역에 대한 ROI 마스크 영상 생성
    mask = np.zeros((ch, cw), np.uint8)
    cv2.circle(mask, (cw//2, ch//2), radius, 255, -1)

    # hue 계산
    hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
    hue, _, _ = cv2.split(hsv)
    # hue에 shit를 줘서 양극단에 있던 빨간값을 왼쪽으로 몰리게 함
    hist_shift = (hue + 50) % 180
    mean_of_hue = cv2.mean(hist_shift, mask)[0]
    
    # cv2.imshow('crop', crop)
    # cv2.imshow('mask', mask)
    # cv2.waitKey()

    # Hue 평균이 90보다 작으면 10원, 90보다 크면 100원으로 간주
    won = 100
    if mean_of_hue < 70:
        won = 10
    else:
        if radius > 90:
            won = 500


    
    sum_of_money += won

    cv2.putText(dst, str(won), (int(cx-10), int(cy)), cv2.FONT_HERSHEY_SIMPLEX,
        0.75, (255,0,0), 2, cv2.LINE_AA)
    

cv2.putText(dst, str(sum_of_money) +' won', (40, 80), cv2.FONT_HERSHEY_SIMPLEX,
    2, (255,0,0), 2, cv2.LINE_AA)

# cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()