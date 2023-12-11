import tkinter as tk
from tkinter import ttk
from plyer import notification

root = tk.Tk()
root.title("Notification app")

fr1 = tk.Frame(root)
tk.Label(fr1, text='ỨNG DỤNG THÔNG BÁO TRÊN WINDOWS').pack()

fr1.pack(pady=(20, 0))

fr2 = tk.Frame(root)
tk.Label(fr2, text='Tiêu đề thông báo:').grid(row=3, column=0, sticky='W')
tk.Label(fr2, text='Nội dung thông báo:').grid(row=4, column=0, sticky='W')
tk.Label(fr2, text='Bao nhiêu giây nó xuất hiện:'). grid(row=5, column=0, sticky='W')

t1 = tk.Entry(fr2)
t1.grid(row=3, column=1)

m = tk.Entry(fr2)
m.grid(row=4, column=1)

tm = tk.Entry(fr2)
tm.grid(row=5, column=1)

fr2.pack(padx=20, pady=10)

def start():
    a = int(tm.get())
    notification.notify(
        title=t1.get(),
        message=m.get(),
        timeout=a
    )


ttk.Button(root, text='Chạy', command=start).pack(pady=(0, 20))

root.mainloop()
