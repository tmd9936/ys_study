import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk

def info():
    msg.showinfo("정보", '정보버튼을 클릭!')

def colorChg():
    result = msg.askyesnocancel("색 변경", "색을 바꾸시겠습니까?")

    if result:
        if colorValue.get() == 1:
            btn1["background"] = "yellow"
        elif colorValue.get() == 2:
            btn1["background"] = "blue"
        

def ask_quit():
    result = msg.askyesno("종료", "종료 하시겠습니까?")

    if result:
        win.quit()

win = tk.Tk()
win.geometry("640x400")
win.resizable(False, False)

menu_bar = tk.Menu(win)
win.config(menu=menu_bar)

menu1 = tk.Menu(win, tearoff=0)
menu1.add_command(label="정보", command = info)

colorValue = tk.IntVar()
submenu = tk.Menu(win, tearoff=0)
submenu.add_radiobutton(label="Red", value=1, variable=colorValue, command=colorChg)
submenu.add_radiobutton(label="Blue", value=2, variable=colorValue, command=colorChg)

menu_bar.add_cascade(label="Menu1", menu=menu1)
menu1.add_cascade(label="radio", menu=submenu)

menu1.add_command(label="종료", command=ask_quit)

def hello():
    # msg.showinfo("파이썬 GUI 정보", "파이썬 정보")
    # msg.showwarning("파이썬 GUI 경고", "파이썬 경고")
    # msg.showerror("파이썬 GUI 에러", "파이썬 에러")
    # msg.askokcancel("파이썬 멀티 선택", "파이썬 강좌 재밌나요?")
    result = msg.askyesnocancel("파이썬 예스노캔슬", "파이썬 강좌 재밌어요?")

btn1 = tk.Button(win, text = "Hello world!!", command = hello)
btn1.pack()



win.mainloop()