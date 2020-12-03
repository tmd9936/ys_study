import tkinter as tk

# tkinter 패키지의 서브모듈 ttk를 가져옴
# ttk(themed tk를 의미)
from tkinter import ttk

win = tk.Tk()

win.title('파이썬 GUI 프로그래밍')


color1 = "Blue"
color2 = "Yellow"
color3 = "Red"

def sel_rbtn():
    radVal = radColor.get()
    if radVal == 1: win.configure(background = color1)
    elif radVal == 2: win.configure(background = color2)
    elif radVal == 3: win.configure(background = color3)

radColor = tk.IntVar()
radio1 = tk.Radiobutton(win, text=color1, value=1, variable = radColor, command=sel_rbtn)
radio1.grid(row=0, column=0, sticky="w")

radio2 = tk.Radiobutton(win, text=color2, value=2, variable = radColor, command=sel_rbtn)
radio2.grid(row=0, column=1, sticky="w")

radio3 = tk.Radiobutton(win, text=color3, value=3, variable = radColor, command=sel_rbtn)
radio3.grid(row=0, column=2, sticky="w")


win.mainloop()