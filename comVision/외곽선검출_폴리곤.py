import math
import cv2

def setLabel(img, pts, label):
    # boundingRect : 주어진 점들을 감싸는 최소크기 사각형
    (x, y, w, h) = cv2.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x + w, y + h)

    # 각 객체 따로 보기
    # temp_img = img[y:y+h, x:x+w]
    # cv2.imshow('poly', temp_img)
    # cv2.waitKey()

    cv2.rectangle(img, pt1, pt2, (0, 0, 255), 1)
    cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))

def main():
    img = cv2.imread('./images/convex.jpg', cv2.IMREAD_COLOR)    

    if img is None:
        print('Image load failed!')
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    _, img_bin = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cv2.imshow('img_bin', img_bin)
    cv2.imshow('gray', gray)

    for pts in contours:
        if cv2.contourArea(pts) < 300:
            continue
        
        # approxPolyDP : 외곽선 단순화 
        # 0.02는 선분의 마진(마진 구간안에 다른 점(좌표)이 있는 경우 그 점을 삭제)
        approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)

        vtc = len(approx)

        # print(vtc)
        # setLabel(img, pts, '?')

        if vtc == 3:
            setLabel(img, pts, 'TRI')
        elif vtc == 4:
            setLabel(img, pts, 'RECT')
        elif vtc == 10:
            setLabel(img, pts, 'STAR')
        else:
            length = cv2.arcLength(pts, True)
            area = cv2.contourArea(pts)
            ratio = 4. * math.pi * area / (length * length)
            
            if ratio > 0.85:
                setLabel(img, pts, 'CIR')
            
    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()