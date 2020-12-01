# 모폴로지 침식 연산 함수
# erode(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, berderValue=None)

# kernel : 구조 요소(structuring element), kernel 생성함수 : getStructuringElement()에 의해 생성
# anchor : 고정점 위치, 기본값(-1, -1)을 이용하면 자동으로 중앙점이 설정
# iteraion : 반복횟수, 기본값은 1 
# borderType : 가장자리 픽셀 확장방식, 기본값 cv2.BORDER_CONSTANT
# borderValue: cv2.BORDER_CONSTANT인 경우, 확장된 가장자리 픽셀을 채울 값

# 모폴로지 팽찰 연산 함수
# dilate(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, berderValue=None)
# -> retval 
# erode와 파라미터는 같다.

# 모폴로지 구조 요소(커널) 생성하는 함수
# getSturecturingElement(shape, ksize, anchor=None) -> retval
# shape : 커널의 모양을 표현하는 플래그(cv2.MORPH_RECT, cv2.MORPH_CROSS, cv2.MORPH_ELLIPSE)
# ksize : 커널의 크기(width, height)튜플로 표현, anchor : (-1, -1)
# retval : numpy.ndarray(0,과 1로 구성된 값, 1의 위치가 커널의 모양을 결정, 타입은 cv2.CV_8U) 


import sys, cv2, numpy as np

src = cv2.imread('./images/circuit.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('iamge open failed!!')
    sys.exit()

se = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 5))

dst1 = cv2.dilate(src, se)
dst2 = cv2.erode(dst1, (5,10))

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)


cv2.waitKey()
cv2.destroyAllWindows()
