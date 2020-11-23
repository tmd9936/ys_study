import sys, cv2, numpy as np

src = cv2.imread('./images/rose.png')

if src is None:
    print('not load')
    sys.exit()

ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

# split을 이용하지 않고  y채널 가져오기
# float32로 conversion을 하는이유 : 중간과정에서 미세한 계산치가 사라지지 않도록 하기 위함
# 내부 연산을 한 후에 최종격과를 확인할 떄 unit8로 형변환 하는것이 좋다.
src_y = ycrcb[:,:,0].astype(np.float32)

blur = cv2.GaussianBlur(src_y, (0,0), 5.0)
ycrcb[:, :, 0] = np.clip(2.*src_y - blur, 0, 255).astype(np.uint8)

dst = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()