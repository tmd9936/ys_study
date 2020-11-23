import os
import cv2
import numpy as np
import pyautogui


src_path = os.path.join('dino','back.png')
tpl_path = os.path.join('dino','dino.png')

src = cv2.imread(src_path, cv2.IMREAD_GRAYSCALE)
tpl = cv2.imread(tpl_path, cv2.IMREAD_GRAYSCALE)

res = cv2.matchTemplate(src, tpl, cv2.TM_CCOEFF_NORMED)

minva, maxval, minloc, maxloc = cv2.minMaxLoc(res)

h, w = tpl.shape[:2]

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
cv2.rectangle(dst, maxloc, (maxloc[0] + w, maxloc[1] + h), (0, 255, 0), 3)

tpl = cv2.resize(tpl, None, fx=2, fy=2)
cv2.imshow('tpl', dst)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()
