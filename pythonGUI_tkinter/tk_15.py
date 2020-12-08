import tkinter as tk
from tkinter import ttk

# Menu 만들기
# 메뉴 이름 = tk.menu(윈도우창) : 해당 윈도우창에 메뉴를 사용
# 윈도우창.config(menu = 메뉴이름) : 해당 윈도우 창에 메뉴를 등록

win = tk.Tk()
win.geometry("640x400")
win.resizable(False, False)

menu_bar = tk.Menu(win)
win.config(menu=menu_bar)

menu1 = tk.Menu(win, tearoff=0)
menu1.add_command(label="file")
submenu = tk.Menu(win, tearoff=0)
submenu.add_radiobutton(label="Option1")
submenu.add_radiobutton(label="Option2")

menu_bar.add_cascade(label="Menu1", menu=menu1)
menu1.add_cascade(label="Submenu", menu=submenu)

menu1.add_command(label="종료", command=win.quit)


win.mainloop()