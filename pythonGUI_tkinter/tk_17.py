import tkinter as tk
from tkinter import ttk

# 탭 컨트롤(위젯)을 생성하는 클래스 Notebook()

win = tk.Tk()
win.geometry("640x400")
win.resizable(False, False)

tabControl = ttk.Notebook(win)

# 첫 번째 탭
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text = "Tab 1")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text = "Tab 2")

# -after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
tabControl.pack(fill = "both", expand=True, padx=10, pady=10)

ttk.Label(tab1, text = "tab1의 라벨입니다..").grid(row=0, column=0)

ttk.Label(tab2, text = "tab2의 라벨입니다..").grid(row=0, column=0)

win.mainloop()