import tkinter as tk
from tkinter import ttk, scrolledtext

def fruit_event():
    txt = fname.get() + " " + amount.get() + "개를 선택하셨습니다.\n"
    txtComments.insert(tk.INSERT, txt)

def colorChg():
    sublbFrame1["text"] = colors[radioVar.get()]

win = tk.Tk()
win.geometry("640x400")
win.resizable(False, False)

# 탭 관리자 생성
tabControl = ttk.Notebook(win)

# 첫 번째 탭
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text = "Tab 1")

lbFrame1 = ttk.LabelFrame(tab1, text="파이썬 GUI 1")
lbFrame1.grid(row=0, column=0, padx=5, pady=5)

lb1 = ttk.Label(lbFrame1, text="과일명 입력")
lb1.grid(row=0, column=0, sticky=tk.W, padx=5)
fname = tk.StringVar()
fentry = ttk.Entry(lbFrame1, width=12, textvariable=fname)
fentry.grid(row=1, column = 0, padx=5, sticky="w")

lb2 = ttk.Label(lbFrame1, text="수량").grid(row=0, column=1)
amount = tk.StringVar()
fcombo = ttk.Combobox(lbFrame1, width=12, textvariable=amount, value=(5,10,20,30))
fcombo.grid(row=1, column = 1, padx = 5, sticky="w")

btn1 = ttk.Button(lbFrame1, text="확인", command=fruit_event)
btn1.grid(row=1, column=2, padx = 5, sticky="w")

txtComments = scrolledtext.ScrolledText(lbFrame1, width=50, height=3, wrap='word')
txtComments.grid(row=2, column=0, columnspan = 3, padx=5)
# 첫 번째 탭 끝

# 두 번째 탭
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text = "Tab 2")

lbFrame2 = ttk.LabelFrame(tab2, text="파이썬 GUI 2")
lbFrame2.grid(row=0, column=0, padx=5, pady=5)

chkvar1 = tk.IntVar()
chk1 = ttk.Checkbutton(lbFrame2, text="체크1", variable=chkvar1)
chk1.grid(row=0, column=0, padx=5, pady=5)

chkvar2 = tk.IntVar()
chk2 = ttk.Checkbutton(lbFrame2, text="체크2", variable=chkvar2)
chk2.grid(row=0, column=1, padx=5, pady=5)

chkvar3 = tk.IntVar()
chk3 = ttk.Checkbutton(lbFrame2, text="체크3", variable=chkvar3)
chk3.grid(row=0, column=2, padx=5, pady=5)

radioVar = tk.IntVar()
colors = ["Red", "Yellow", "Blue"]
for i in range(len(colors)):
    radio = ttk.Radiobutton(lbFrame2, value=i, text=colors[i], variable=radioVar, command=colorChg)
    radio.grid(row=1, column=i, sticky="w")

sublbFrame1 = ttk.LabelFrame(lbFrame2, text="Red")
sublbFrame1.grid(row=2, columnspan=3)

for i in range(3):
    ttk.Label(sublbFrame1, text="Label" + str(i+1)).grid(row=i, column=0)


# 두 번째 탭 끝
tabControl.pack(fill = "both", expand=True, padx=10, pady=10)

win.mainloop()