"""
pip install youtube-dl
pip install pafy
"""

import pafy, cv2

def on_duration_change(param):
    print(param)

url = 'https://www.youtube.com/watch?v=uslB3C8QV4Q'
video = pafy.new(url)
print('title =', video.title)
print('rating =', video.rating)
# print('duration =', video.duration)

s_d = video.duration.split(':')
duration_sec = int(s_d[0])*3600 + int(s_d[1])*60 + int(s_d[2])
print('duration_sec =', duration_sec)

best = video.getbest(preftype='mp4')
print('best.resolution =', best.resolution)
print('best.url =',best.url)

cap = cv2.VideoCapture(best.url)
retval, frame = cap.read()

# cv2.imshow('frame', frame)

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
cv2.imshow('edges', edges )
    
cv2.createTrackbar('duration', 'edges', 0, duration_sec, on_duration_change)

while(True):
    retval, frame = cap.read()
    
    if not retval:
        break
    
    # cv2.imshow('frame', frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    cv2.imshow('edges', edges )
    
    key = cv2.waitKey(20)

    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()

