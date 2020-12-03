import tkinter as tk
from tkinter import scrolledtext

# tkinter 패키지의 서브모듈 ttk를 가져옴
# ttk(themed tk를 의미)
from tkinter import ttk

win = tk.Tk()

win.title('파이썬 GUI 프로그래밍')

colors = ["Blue", "Yellow", "Red", "Green"]

def selColor():
    radVal = radColor.get()
    win.configure(background = colors[int(radVal)])


radColor = tk.IntVar()


for i, color in enumerate(colors):
    rad = tk.Radiobutton(win, text=color, value=i, variable = radColor, command=selColor)
    rad.grid(row=0, column=i+1, sticky="w")

txtComments = tk.Text(win)
txtComments.grid(row = 0, column = 0)

txtComments = scrolledtext.ScrolledText(win, width=50, height=3, wrap='word')
txtComments.grid(column=0, columnspan = 3)

win.mainloop()