import tkinter as tk

# tkinter 패키지의 서브모듈 ttk를 가져옴
# ttk(themed tk를 의미)
from tkinter import ttk

win = tk.Tk()

win.title('파이썬 GUI 프로그래밍')

ent1 = tk.Entry(win)
ent1.grid(row = 0, column = 0)

ent1 = tk.Entry(win)
ent1.grid(row = 0, column = 1)

chk1 = tk.Checkbutton(win, text = "독서", state = 'disable')
# 동서남북으로 계산, 대각선도 가능
#    n
# w     e
#    s
chk1.grid(row = 1, column = 0, sticky='w')

chk2 = tk.Checkbutton(win, text = "운동")
chk2.grid(row = 1, column = 1, stick=tk.E)
chk2.select()

chk3 = tk.Checkbutton(win, text = "영화감상")
chk3.grid(row = 1, column = 2)



win.mainloop()