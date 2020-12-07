# Spinbox 위젯

import tkinter as tk
from tkinter import ttk, scrolledtext

win = tk.Tk()
win.title('파이썬 GUI - Spinbox')
win.geometry("640x480")
win.resizable(0,0)

def _spin():
    val = spin.get()
    scrol.insert(tk.INSERT, val + '\n')

def _spin2():
    val = spin2.get()
    scrol.insert(tk.INSERT, val + '\n')


spin = tk.Spinbox(win, width=5, from_ = 0, to = 10, command=_spin)
spin.grid(row=0, column=0, padx=20, pady=20)

spin2 = tk.Spinbox(win, width=5, values=(10, 20, 40, 100), command=_spin2)
spin2.grid(row=0, column=1, padx=20, pady=20)

scrol = scrolledtext.ScrolledText(win, width=30, height=3, wrap=tk.WORD)
scrol.grid(row=1, columnspan=2, padx = 20, pady = 10)



win.mainloop()
