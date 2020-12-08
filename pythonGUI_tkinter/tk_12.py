import tkinter as tk

win = tk.Tk()
win.geometry("640x400")

win.resizable(False, False)

# grid
btn1 = tk.Button(win, text="btn1")
btn2 = tk.Button(win, text="btn2", width = 30)
btn3 = tk.Button(win, text="btn3")

btn4 = tk.Button(win, text="btn4")
btn5 = tk.Button(win, text="btn5")
btn6 = tk.Button(win, text="btn6")

# btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2, padx=20)

btn4.grid(row=1, column=0, rowspan=1)
btn5.grid(row=1, column=1, ipadx = 30, ipady = 30, pady = 20)
btn6.grid(row=1, column=3)

win.mainloop()