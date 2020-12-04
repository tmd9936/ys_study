import cv2
import numpy as np
from tkinter import *
from PIL import Image # pip install pillow
from PIL import ImageTk
from tkinter import filedialog

file_name = './images/soccer_01.jpg'
title_name = 'Haar cascade 얼굴 검출'
frame_width = 500

def selectFile():
    # 파일 다이얼로그 띄우기, initialdir: 초기 위치, title : 다이얼로그 이름, filetypes : fillting 할 파일 종류
    file_name =  filedialog.askopenfilename(initialdir = "./images/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print('File name : ', file_name)

    if file_name is None or file_name == "":
        return

    # 이미지를 비율에 맞게 사이즈를 조정
    read_image = cv2.imread(file_name)
    (height, width) = read_image.shape[:2]
    frameSize = int(sizeSpin.get())
    ratio = frameSize / width
    dimension = (frameSize, int(height * ratio))
    
    read_image = cv2.resize(read_image, dimension, interpolation = cv2.INTER_AREA)

    # tkinter와 호환되는 이미지로 변환
    # image = cv2.cvtColor(read_image, cv2.COLOR_BGR2RGB)
    # image = Image.fromarray(image)
    # imgtk = ImageTk.PhotoImage(image=image)
    detectAndDisplay(read_image)

# 얼굴, 눈 검출
def detectAndDisplay(frame):
    # gray타입으로 변환
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 색상을 늘어트림
    frame_gray = cv2.equalizeHist(frame_gray)

    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        
        center = (x + w//2, y + h//2)
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4)
        faceROI = frame_gray[y:y+h,x:x+w]

        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv2.circle(frame, eye_center, radius, (255, 0, 0 ), 4)

    # cv2.imshow('Capture - Face detection', frame)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image) 

    # 객체로 변환하기
    imgtk = ImageTk.PhotoImage(image=image) 

    # 라벨에 이미지 띄우기
    detection.config(image=imgtk)
    detection.image = imgtk
    
# tkinter GUI main
main = Tk()
main.title(title_name)
main.geometry()

read_image = cv2.imread("images/soccer_01.jpg")
(height, width) = read_image.shape[:2]
# 가로 비율
ratio = frame_width / width
# 가로비율에 맞춰서 세로 비율 구하기
dimension = (frame_width, int(height * ratio))
# 창크기에 맞춰서 이미지의 사이즈 조절
read_image = cv2.resize(read_image, dimension, interpolation = cv2.INTER_AREA)

image = cv2.cvtColor(read_image, cv2.COLOR_BGR2RGB)
# PIL 라이브러리를 이용해서 ndarray를 이미지로 변환
image = Image.fromarray(image)
# tkinter와 호환되는 이미지로 변경
imgtk = ImageTk.PhotoImage(image=image)

# 얼굴검출 객체
face_cascade = cv2.CascadeClassifier()
# 눈 검출 객체
eyes_cascade = cv2.CascadeClassifier()

#-- 1. Load the cascades
if not face_cascade.load('./studydata/haarcascade_frontalface_alt2.xml'):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load('./studydata/haarcascade_eye.xml'):
    print('--(!)Error loading eyes cascade')
    exit(0)

label=Label(main, text=title_name)
# 폰트변경
label.config(font=("Courier", 18))
label.grid(row=0,column=0,columnspan=4)
# 사이즈 크기 조정용 레이블
sizeLabel=Label(main, text='Frame Width : ')                
sizeLabel.grid(row=1,column=0)

# 초기값 설정
sizeVal = IntVar(value=frame_width)
# 스핀박스 생성 값은 sizeVal변수와 동기롸, 0부터 2000의 값을 100씩 증가
sizeSpin = Spinbox(main, textvariable=sizeVal,from_=0, to=2000, increment=100, justify=RIGHT)
sizeSpin.grid(row=1, column=1)

# 파일 다이알로그를 띄우는 버튼 객체 생성
Button(main,text="File Select", height=2, command=lambda:selectFile()).grid(row=1, column=2, columnspan=2, sticky=(W, E))
# PIL로 만든 tkinter와 호환되는 이미지버퍼를 불러옴
detection = Label(main, image=imgtk)
detection.grid(row=2,column=0,columnspan=4)
detectAndDisplay(read_image)

main.mainloop()