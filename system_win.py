import tkinter as tk
import platform

font = ("Segoe UI", 14)

root = tk.Tk()

tk.Label(root, text=platform.system(), font=font).pack()
tk.Label(root, text=platform.version(), font=font).pack()
tk.Label(root, text=platform.machine(), font=font).pack()
tk.Label(root, text=platform.uname(), font=font).pack()
tk.Label(root, text=platform.processor(), font=font).pack()

root.mainloop()
