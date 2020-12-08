# 파이썬 GUI 프레임워크(Toolkit)

# Tkinter(Tk interface) : 파이썬에서 기본적으로 제공되는 표준 라이브러리

# PyQt

import tkinter as tk



# TK클래스를 이용해서 윈도우 창을 만든다
win = tk.Tk()

# 파이썬 tkinter 위젯 클래스 중에 Label, Button
label = tk.Label(win, text = "Welcome to PYTHON")
button = tk.Button(win, text="클릭!!")

# 이벤트 루프 생성
win.mainloop()
