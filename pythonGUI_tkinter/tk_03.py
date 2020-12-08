import tkinter as tk

# tkinter 패키지의 서브모듈 ttk를 가져옴
# ttk(themed tk를 의미)
from tkinter import ttk

win = tk.Tk()

win.title('파이썬')

label = ttk.Label(win, text="라벨")
label.grid(column = 0, row = 0)
# label.pack()


def clickMe():
    label.configure(text = "버튼이 클릭되었습니다!!")
    btn1.configure(text="****")
    label.configure(foreground= "blue", background="yellow")

btn1 = ttk.Button(win, text="클릭", command = clickMe)
btn1.grid(column = 1, row = 0)
# btn1.pack()

win.mainloop()