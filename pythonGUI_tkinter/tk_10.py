# Geometry Manager
# Tkinter 에서는 위젯들을 화면에 배치하는 방식으로 3가지 방식을 사용한다.

# Pack : 상하로 패킹(pack() 메소드)

# Grid : 위젯들을 격자(테이블)에 배치하는 방식(grid())

# Place(absolute) : 절대 좌표로 위젝을 정하여 배치, 윈도우 크기 변경에 따라 
# 위젯들이 변경되지 않는다. place() 메소드 사용, 많이 사용되지 않음.

import tkinter as tk

win = tk.Tk()
win.geometry("640x400")

win.resizable(False, False)

# side : top, left, right, bottmo으로 자동
# anchor : 특정 위치로 이동(현재 구역내에서)(동서남북 센터)
# fill : 할당된 공간에 맞게 크기가 변경
# expand : 미사용 공간을 모두 현재 위젯의 할당된 공간으로 변경
# justify : 정렬(좌, 우, 가운데)
frame1 = tk.Frame(win, bd=2, background="yellow")
frame1.pack(side = "top", fill="y", expand=True)

frame2 = tk.Frame(win, bd=2, background="blue")
frame2.pack(side="right", fill="both", expand=True)

btn1 = tk.Button(frame1, text="프레임1")
btn1.pack()

btn2 = tk.Button(frame2, text="프레임2")
btn2.pack()

win.mainloop()
