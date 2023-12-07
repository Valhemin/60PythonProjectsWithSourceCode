"""
1. Import thư viện tkinter và messagebox để tạo giao diện người dùng.
2. Định nghĩa hàm convert để thực hiện chuyển đổi nhiệt độ và xử lý các trường hợp ngoại lệ.
3. Tạo cửa sổ giao diện chương trình và các thành phần giao diện như nhãn, ô nhập liệu, nút chuyển đổi và nút lựa chọn chuyển đổi.
4. Khi người dùng nhấn nút "Convert", hàm convert sẽ được gọi để thực hiện chuyển đổi và hiển thị kết quả trong một cửa sổ thông báo.
"""
import tkinter as tk
from tkinter import messagebox

"""
C = (F - 32) * 5/9
F = (9/5)*C + 32
"""
font_family = ("Arial", 14, "bold")


def convert():
    try:
        val = var.get()
        tmp = float(temp.get())

        """
        1: C -> F
        2: F -> C
        """
        if val == 1:
            f_temp = (9/5)*tmp + 32
            result = f"{tmp} C = {f_temp:.2f} F"
        elif val == 2:
            c_temp = (tmp - 32) * (5/9)
            result = f"{tmp} F = {c_temp:.2f} C"

        messagebox.showinfo("Result", result)
    except Exception as e:
        messagebox.showerror("Error", e)


root = tk.Tk()
root.title("Temperature convertor")
root.geometry("650x150")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Temperature", font=font_family).grid(row=0, column=0)
temp = tk.Entry(frame, width=30, font=font_family)
temp.grid(row=0, column=1, padx=20, pady=10)

tk.Button(frame, text="Convert", command=convert, font=font_family).grid(row=0, column=2)

var = tk.IntVar()
tk.Radiobutton(frame, text="C to F", variable=var,
                value=1, font=font_family).grid(row=1, column=1)
tk.Radiobutton(frame, text="F to C", variable=var,
                value=2, font=font_family).grid(row=2, column=1)

root.mainloop()
