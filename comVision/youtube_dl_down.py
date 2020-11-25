import pafy, cv2

def on_duration_change(param):
    print(param)

url = 'https://www.youtube.com/watch?v=BWTJ2Acw6Sk'
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

best.download('./videos/')


"""
비디오 길이 변환
ffmpeg -i ..\..\traffic.mp4 -ss 117 -t 17 -vcodec copy -acodec copy traffic_clip.mp4
"""