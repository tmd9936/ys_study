import tkinter as tk

win = tk.Tk()
win.geometry("640x400")

win.resizable(False, False)

# place
btn1 = tk.Button(win, text="btn1")
btn1.place(x=100, y=100)

btn2 = tk.Button(win, text="btn2")
btn2.place(x=100, y=200, width=150, height=150)

# rely = 0.2 -> y축 20프로지점
btn3 = tk.Button(win, text="btn3")
btn3.place(x=0, relx=0.5, rely=0.3) # relx,rely : x,y좌표 배치비율(0~1)

btn4 = tk.Button(win, text="btn4")
# relwidth, relheight : x,y 좌표 위젯의 너비와 높이 비율(0~1)
btn4.place(x=0, y=200, relwidth=1)


win.mainloop()