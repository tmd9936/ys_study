import tkinter as tk

# tkinter 패키지의 서브모듈 ttk를 가져옴
# ttk(themed tk를 의미)
from tkinter import ttk

win = tk.Tk()

win.title('파이썬 GUI')

label = ttk.Label(win, text="아이디")
label.grid(row = 0, column = 0)

id = tk.StringVar()
entry1 = ttk.Entry(win, textvariable = id)
entry1.grid(row = 0, column = 1)

def clickMe():
    label2.configure(text="하이!!" + id.get())
    id.set("stop")

btn1 = ttk.Button(win, text="클릭", command=clickMe)
btn1.grid(row = 0, column = 2)

label2 = ttk.Label(win, text="")
label2.grid(row = 1, column = 1)

entry1.focus()
btn1.focus()

win.mainloop()