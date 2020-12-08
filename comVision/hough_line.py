import sys, cv2, numpy as np

# xcosθ(세타) + ysinθ(세타) = ρ(rho)
# 허프변환에 의한 직선 검출
# cv2.HoughLines(image, rho, theta, threshold, lines=None, srn=None, stn=None, min-theta=None, max-theta=None)
# image : 엣지 입력 영상(Canny 연산을 이용한 엣지 영상)
# rho : 축적배열에서 rho값의 간격
# theta : 축적배열에서의 theta값의 간격(np.pi/180)

# rho, theta값이 커지면 축적배열의 크기는 작아지고, 값이 작아지면 축적배열은 커진다.

# 축적배열이 커진다: 더 정밀한 직선을 표현, 연산량이 많아 더 오래걸림
# 축적배열이 작아진다: 정말한 직선을 표현할 수 없으나, 연산량이 적음

# threshold : 축적배열에서 직선으로 판단할 임계값, 직선의 개수와 반비례

# lines : rho와 theta값을 담고있는 3차원행렬(nd.array) 형태로 리턴된다.
# lines의 shape은 (N, 1, 2), N은 직선의 개수 가운데 1은 의미없는 차원, dtype = numpy.float32, ** shape 주의할 것

# 확률적 허프 변환 함수
# cv2.HoughLinesP(image, rho, theta, threshold, minLineLength=None, maxLineGap=None)
# image : 엣지 입력 영상(Canny 연산을 이용한 엣지 영상)
# rho : 축적배열에서 rho값의 간격
# theta : 축적배열에서의 theta값의 간격(np.pi/180)
# threshold : 축적배열에서 직선으로 판단할 임계값, 직선의 개수와 반비례
# lines : 선분의 시작과 끝 좌표(x1, y1, x2, y2)의 정보를 담고 있는 numpy.ndarray
# shape=(N, 1, 4), dtype=numpy.int32
# minLineLength : 검출하기위한 선분의 최소길이
# maxLineGap : 직선으로 간주하기 위한 최대 에지점 간격


src = cv2.imread('./images/bd1.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!!')
    sys.exit()

edges = cv2.Canny(src, 50, 150)

lines = cv2.HoughLinesP(edges, 1, np.pi / 180.0, 120, minLineLength=50, maxLineGap=5)

dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

print(lines)

if lines is not None:
    for i in range(lines.shape[0]):
        pt1 = (lines[i][0][0], lines[i][0][1]) # 시작점 좌표, 가운데 값을 무조건 0으로
        pt2 = (lines[i][0][2], lines[i][0][3]) # 끝점 좌표, 가운데 값을 무조건 0으로
        cv2.line(dst, pt1, pt2, (0,255,0), 1, cv2.LINE_AA)


cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()
