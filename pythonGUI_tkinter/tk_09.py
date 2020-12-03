# Geometry Manager
# Tkinter 에서는 위젯들을 화면에 배치하는 방식으로 3가지 방식을 사용한다.

# Pack : 상하로 패킹(pack() 메소드)

# Grid : 위젯들을 격자(테이블)에 배치하는 방식(grid())

# Place(absolute) : 절대 좌표로 위젝을 정하여 배치, 윈도우 크기 변경에 따라 
# 위젯들이 변경되지 않는다. place() 메소드 사용, 많이 사용되지 않음.


import tkinter as tk

# tkinter 패키지의 서브모듈 ttk를 가져옴
# ttk(themed tk를 의미)
from tkinter import ttk

win = tk.Tk()
win.geometry("400x400+1000+200")

# label = tk.Label(win, text="파이썬 파이썬")
label = tk.Label(win, text="파이썬 파이썬 \n파이썬",
                background = "yellow", width=20, height=10, 
                bd=5, relief="solid",
                anchor=tk.NE, justify=tk.RIGHT)
label.pack()

# label2 = tk.Label(label, text="파이썬 파이썬",
#                 background = "red", width=20, height=10)
# label2.grid(row=0, column=0)

# label3 = tk.Label(label, text="파이썬 파이썬",
#                 background = "blue", width=20, height=10)
# label3.grid(row=0, column=1)

win.mainloop()
