import cv2, numpy as np

X = np.array([[0,   0,  0,      100,    100,    150,    -100,   -150],
              [0,   50, -50,    0,      30,     100,    -20,    -100]], dtype = np.float64)

# 전치행렬 X.T로도 구해짐
X = X.transpose() # X = X.T

# 각 행(cv2.COVAR_ROWS)에서 (x,y) 좌표의 평균 mean, 공분산 행렬 cov를 계산한다.
# 평균은 1x2 열벡터이고, 공분산 행렬 cov는 2x2행렬이다. 
# 만약 데이터가 행렬의 열에 있으면 flags에 cv2.COVAR_COLS를 사용한다.
cov, mean = cv2.calcCovarMatrix(X ,mean = None, flags = cv2.COVAR_NORMAL + cv2.COVAR_ROWS)

print("mean=", mean)
print("cov=", cov)

# 공분산의 역행렬의 구한다.
ret, icov = cv2.invert(cov)
print('icov=', icov)

v1 = np.array([[0], [0]], dtype= np.float64)
v2 = np.array([[0], [50]], dtype= np.float64)

dist = cv2.Mahalanobis(v1, v2, icov)
print('dist=', dist)


