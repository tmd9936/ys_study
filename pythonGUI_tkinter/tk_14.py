import tkinter as tk
from tkinter import ttk

# Menu 만들기
# 메뉴 이름 = tk.menu(윈도우창) : 해당 윈도우창에 메뉴를 사용
# 윈도우창.config(menu = 메뉴이름) : 해당 윈도우 창에 메뉴를 등록

win = tk.Tk()
win.geometry("640x400")
win.resizable(False, False)

menu_bar = tk.Menu(win)
win.config(menu = menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="서브메뉴1")
file_menu.add_command(label="서브메뉴2")
file_menu.add_separator() # 구분선
file_menu.add_command(label="종료", command=win.quit)

# 상위 메뉴와 하위메뉴 연결(label="하위메뉴이름", menu="연결할 하위메뉴")
menu_bar.add_cascade(label="File", menu=file_menu)

rad_menu = tk.Menu(menu_bar, tearoff=0)
rad_menu.add_radiobutton(label = "서브메뉴", state = "disable")
rad_menu.add_radiobutton(label = "서브메뉴2")
rad_menu.add_radiobutton(label = "서브메뉴3")
menu_bar.add_cascade(label="라디오메뉴", menu=rad_menu)

win.mainloop()