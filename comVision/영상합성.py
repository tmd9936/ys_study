import sys, cv2, numpy as np

src = cv2.imread('./images/bg2.jpg')

logo = cv2.imread('./images/cv_txt.png', cv2.IMREAD_UNCHANGED)

if src is None or logo is None:
    print("Image load failed!!")
    sys.exit()

mask = logo[:, :, 3]

# mask = cv2.Canny(mask, 100, 200)

logo = logo[:, :, :-1]

h, w = mask.shape[:2]

crop = src[350:350+h, 200:200+w]

crop[mask > 0] = logo[mask > 0]

cv2.imshow('src', src)
cv2.imshow('logo', logo)
cv2.imshow('mask', mask)

cv2.waitKey()
cv2.destroyAllWindows()