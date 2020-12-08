import tkinter as tk

# tkinter 패키지의 서브모듈 ttk를 가져옴
# ttk(themed tk를 의미)
from tkinter import ttk

win = tk.Tk()

win.title('파이썬 GUI 프로그래밍')

label1 = ttk.Label(win, text="과일명 입력:")
label1.grid(row = 0, column = 0)

fruitName = tk.StringVar()
fruitEntry = ttk.Entry(win, width=15, textvariable = fruitName)
fruitEntry.grid(row = 1, column = 0)

label2 = ttk.Label(win, text="수량 선택:")
label2.grid(row = 0, column = 1)

num = tk.StringVar()
numCombobox = ttk.Combobox(win, width=10, values=(5, 10, 20, 30), textvariable = num)
numCombobox.grid(row = 1, column = 1)

def select():
    label3.configure(text=""+ fruitName.get() +"를 "+num.get() +"개 선택했습니다.")

btn1 = ttk.Button(win, text="확인", command = select)
btn1.grid(row = 1, column = 2)

label3 = ttk.Label(win, text="")
label3.grid(row = 2, column = 0)



fruitEntry.focus()

win.mainloop()