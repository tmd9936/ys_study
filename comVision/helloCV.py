import cv2
import sys

print('hello opencv', cv2.__version__)

# 영상파일 불러오기
# cv2.IMREAD_COLOR : 컬러, defalut값
# cv2.IMREAD_GRAYSCALE : 흑백
# cv2.IMREAD_UNCHANGED : 투명 PNG파일
img = cv2.imread('./dog_img.bmp', cv2.IMREAD_COLOR) 

if img is Nonw:
    print('Image load failed!!')
    sys.exit()

# image라는 창을 생성
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
# cv2.namedWindow('image', cv2.WINDOW_NORMAL) # 사이즈 조절 가능

# imshow에서 이미지가 보이는게 아니라 waitKey가 되는 순간 이미지가 보임
# imshow에 의해서 생성된 image는 이미지의 크기대로만 생성
cv2.imshow('image', img)
cv2.waitKey()
# key = cv2.waitKey(2000) # 2초간 딜레이를 줌
# print(key)

# 특정키로만 종료하기
# while True:
#     # if cv2.waitKey() == 27:
#     if cv2.waitKey() == ord('q'):
#         break


cv2.destroyAllWindows()
# cv2.destroyWindow('image')
