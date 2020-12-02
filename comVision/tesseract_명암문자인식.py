# Tesseract
# 광학 문자 인식(OCR) 라이브러리
# 독일 만하임 대학교 사이트(https://github.com/UB-Mannheim/tesseract/wiki)
# Tesseract 설치 후
# pip install pytesseract 명령 실행

import sys
import random
import numpy as np
import cv2
import pytesseract

# 왼쪽위 꼭지점 부터 시계 방향으로 정렬
def reorderPts(pts):
    # 칼럼0 -> 칼럼1 순으로 정렬한 인덱스를 반환
    # 위에 있는 점인지 아래있는 점인지 정렬 
    idx = np.lexsort((pts[:, 1], pts[:, 0])) 
    print('인덱스 : ', idx)
    
    pts = pts[idx]      
    
    # 왼쪽에 있는 점인지 오른쪽에 있는 점인지 정렬
    # 반시계 방향으로 정렬된 좌표 pts 구하기
    if pts[0, 1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]]

    if pts[2, 1] < pts[3, 1]:
        pts[[2, 3]] = pts[[3, 2]]

    return pts 

# 영상 불러오기
filename = './images/namecard3.jpg'

if len(sys.argv) > 1:
    filename = sys.argv[1]

src = cv2.imread(filename)

if src is None:
    print('Image load failed!')
    sys.exit()

# 명함 크기
dw, dh = 720, 400

# 전체 이미지 좌표
srcCoord = np.array([[0, 0], [0, 0], [0, 0], [0, 0]], np.float32)
# 명암 그릴 창의 좌표
dstCoord = np.array([[0, 0], [0, dh], [dw, dh], [dw, 0]], np.float32)

# 결과이미지
dst = np.zeros((dh, dw), np.uint8)

# gray이미지오 변환
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 영상 OTSU로 자동 이진화
_, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# cv2.imshow('src_bin', src_bin)

# 외곽선 검출, 계층(hier)정보는 안 가져옴
# RETR_EXTERNAL : 포함된 외곽선은 검출 안함
contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cpy = src.copy()
for pts in contours:
    # 영역의 크기가 1000이하면 무시
    if cv2.contourArea(pts) < 1000:
        continue

    # approxPolyDP : 외곽선 근사화, 0.02는 근사치(마진)
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)
    # convex인지 검사, 꼭지점이 4개(사각형)가 아닌 경우 종료
    if not cv2.isContourConvex(approx) or len(approx) != 4:
        continue
    
    # 근사화된 좌표로 사각형객체 그리기
    cv2.polylines(cpy, [approx], True, (0, 255, 0), 2, cv2.LINE_AA)
    srcCoord = reorderPts(approx.reshape(4, 2).astype(np.float32))



# 투시변환을 이용해서 영상 펴기
pers = cv2.getPerspectiveTransform(srcCoord, dstCoord)
dst = cv2.warpPerspective(src, pers, (dw, dh))

dst_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
st = pytesseract.image_to_string(dst_gray, lang='Hangul+eng')

print(st)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()