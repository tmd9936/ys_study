import sys
import cv2

cap = cv2.VideoCapture('./videos/video1.mp4')

if not cap.isOpened():
    print("Video open failed")
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
print(fourcc)

# 비디오 출력 : VideoWriter(filename, forcc, fps, framesize, isColor)
# out = cv2.VideoWriter('./videos/outVideo.avi', fourcc, fps, (w,h))
out2 = cv2.VideoWriter('./videos/outVideo_edge.avi', fourcc, fps, (w,h))

if not out2.isOpened():
    print('File open fail!')
    cap.release()
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # inversed = ~frame
    edge = cv2.Canny(frame, 50, 150) # Canny의 리턴값은 grayScale
    edge_2 = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    # out.write(inversed)
    out2.write(edge_2)

    # cv2.imshow('inversed', inversed)
    # cv2.imshow('edge', edge)

    cv2.imshow('edge_2', edge_2)

    if cv2.waitKey(25) == 27:
        break



cap.release()
out2.release()
cv2.destroyAllWindows()





