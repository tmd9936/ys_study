import sys
import numpy as np
import cv2

# 키보드 이벤트
# cv2.waitKey(delay) => retVal
# delay : 밀리초단위 대기시간, delay <= 0 : 무한정 대기, 기본값 0
# retVal: 눌린 키값(ASCII code), 키가 눌린지 않으면 -1
# 참고 : waitKey() 함수는 opencv창이 하나라도 있을 때 동작함.
# : 특정 키 입력을 확인하려면 ord()함수를 이용
# 주요 특수키 : ESC(27), ENTER(13), TAB(9)

img = cv2.imread('./dog_img.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed!!')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image',img)
revers = ~img

while True:

    retVal =  cv2.waitKey()
    
    if retVal == 27:
        break
    elif retVal == ord('i') or retVal == ord('I'):
        cv2.imshow('image', revers)
    elif retVal == ord('o') or retVal == ord('O'):
        cv2.imshow('image', img)



# https://angeloyeo.github.io/2020/01/16/time_frequency_uncertainty.html
cv2.destroyAllWindows()