# 컴퓨터비전에서 연산 시간 체크의 필요성
# : 컴퓨터 비전은 대용량 데이터를 다루어서 의미있는
# : 최종 결과를 얻어내야 한다. 이를 위해서는 매여러 단계를
# : 거치게 되는데, 매 단계에서 병목(Bottleneck)현상이 있는지
# : 체크하는 것은 중요한 과정중 하나이다.
# : 단계별 연산 시간을 체크하기 위해 사용하는 함수 : TickMeter

import sys, cv2
import numpy as np

img = cv2.imread('./images/test_img.jpg')

if img is None:
    print("Image load failed!!")
    sys.exit()

# 특정 연산에 대한 시간 측정하기

tm = cv2.TickMeter()

tm.reset()
tm.start()

edge = cv2.Canny(img, 50, 150)

tm.stop()
print('Elapsed tme : {}ms.'.format(tm.getTimeMilli()))