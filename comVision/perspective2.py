import math, sys, cv2, numpy as np

src = cv2.imread('./images/perspective_test.jpg')

if src is None:
    print('Image load failed!!')
    sys.exit()

h, w = src.shape[:2]

src_copy = src.copy()
pts = np.array([[50,50], [w-100,50], [w-100,h-100], [50,h-100]])
radius = 20

def on_mouse(event, x, y, flags, param):
    global ptOld
    mv_point = -1
    is_move = False

    if event == cv2.EVENT_LBUTTONDOWN:
        ptOld = (x, y)

    if event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_LBUTTONDOWN:
            for i in range(0, len(pts)):
                # if (x > pts[i][0] - radius and x < pts[i][0] + radius) and (y > pts[i][1] - radius and y < pts[i][1] + radius):
                if cv2.norm(pts[i] - (x, y)) < radius: # 거리계산
                    mv_point = i
                    is_move = True
                    break
            
            if is_move:
                src = src_copy.copy()
                dx = x - ptOld[0]
                dy = y - ptOld[1]
                pts[mv_point] += (dx, dy)

                ptOld = (x,y)

                for pt in pts:
                    cv2.circle(src, (pt[0], pt[1]), radius, (255,200,200), -1)
                
                src = cv2.addWeighted(src, 0.3, src_copy, 0.7, 0)
                
                cv2.polylines(src, [pts], isClosed = True, color=(0, 0, 255))
                cv2.imshow('image', src)

    if event == cv2.EVENT_LBUTTONUP:
        is_move = False


cv2.namedWindow("image")
cv2.setMouseCallback("image", on_mouse)

for pt in pts:
    pp = cv2.circle(src, (pt[0], pt[1]), radius, (255,200,200), -1)

src = cv2.addWeighted(src, 0.3, src_copy, 0.7, 0)

cv2.polylines(src, [pts], isClosed = True, color=(0, 0, 255))
cv2.imshow('image', src)
while True:

    key = cv2.waitKey()
    if key == ord(' '):
        w = int(math.sqrt( (pts[1,0]-pts[0,0])**2 + (pts[1,1]-pts[0,1])**2 ) )
        h = int(math.sqrt( (pts[3,0]-pts[0,0])**2 + (pts[3,1]-pts[0,1])**2 ) )

        src_Coord = pts.astype(np.float32)
        dst_Coord = np.array([[0,0], [w-1, 0], [w-1, h-1], [0,h-1]], np.float32)

        per_matrix = cv2.getPerspectiveTransform(src_Coord, dst_Coord)
        dst = cv2.warpPerspective(src_copy, per_matrix, (w,h))

        cv2.imshow('dst', dst)

        
    elif key == 27:
        break

cv2.destroyAllWindows()