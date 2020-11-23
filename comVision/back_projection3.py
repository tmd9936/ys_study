import sys, cv2, numpy as np

reference_img = cv2.imread('./images/son2.png')
mask = cv2.imread('./images/son2_mask.bmp', cv2.IMREAD_GRAYSCALE)

if reference_img is None or mask is None:
    print('image load failed!!')
    sys.exit()

def getHistDraw(hist):
    imgHist = np.full((100,128), 255, dtype=np.uint8)
    
    histMax = np.max(hist)

    for x in range(128):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        cv2.line(imgHist, pt1, pt2, 0)

    return imgHist

ref_ycrcb = cv2.cvtColor(reference_img, cv2.COLOR_BGR2YCrCb)

channels = [1, 2]
ranges = [0, 256, 0, 256]
# hist = cv2.calcHist([ref_ycrcb], channels, mask, [128, 128], ranges)
hist_cr = cv2.calcHist([ref_ycrcb], [1], mask, [128], [0, 256])
hist_cb = cv2.calcHist([ref_ycrcb], [2], mask, [128], [0, 256])

h_cr = getHistDraw(hist_cr)
h_cb = getHistDraw(hist_cb)

cv2.imshow('h_cr', h_cr)
cv2.imshow('h_cb', h_cb)

cv2.waitKey()
cv2.destroyAllWindows()
