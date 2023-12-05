"""
Đoạn code Python này sử dụng thư viện Colorama để in ra màu sắc trên terminal.

Cụ thể:

- Import thư viện Colorama
- Khởi tạo Colorama với tùy chọn autoreset=True. 
  Điều này có nghĩa là sau mỗi lần in ra màu, màu sẽ tự động đặt lại về mặc định thay vì giữ nguyên.
- Import ra 2 constant Fore và Back từ colorama dùng để set màu cho chữ và nền
- In ra dòng "Viet nam tuoi dep" với màu xanh lam (BLUE) cho chữ, màu vàng (YELLOW) cho nền
- In ra dòng "Thien nhien ky thu" với màu đen (BLACK) cho chữ, màu xanh lơ (CYAN) cho nền.

Như vậy, đoạn code trên đã sử dụng Colorama để làm cho terminal có thêm màu sắc, tô đậm các dòng text được in ra.
"""
import colorama
from colorama import Fore, Back

colorama.init(autoreset=True)

print(Fore.BLUE + Back.YELLOW + "Viet nam tuoi dep")
print(Back.CYAN + Fore.BLACK + "Thien nhien ky thu")
