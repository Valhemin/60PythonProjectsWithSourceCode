"""
Được, đây là giải thích bằng tiếng Việt cho đoạn code trên:

Đầu tiên, import thư viện random để sử dụng hàm ngẫu nhiên:

```python
import random
```

Tiếp theo, khởi tạo giá trị nhỏ nhất (min_val) và lớn nhất (max_val) khi tung xúc xắc:

```python
min_val = 1
max_val = 6 
```

Sau đó, sử dụng vòng lặp while True để cho phép lặp đi lặp lại việc tung xúc xắc: 

Trong vòng lặp, hỏi người dùng có muốn tung xúc xắc hay không thông qua câu lệnh:

```python
roll_again = input("Muốn tung xúc xắc không ? (yes/no): ")
```

Kiểm tra giá trị trả về:
- Nếu khác yes/no: Báo lỗi yêu cầu nhập lại 
- Nếu bằng no: Thoát vòng lặp
- Nếu bằng yes: In ra đang tung xúc xắc, và random 2 số từ 1 đến 6

Như vậy, đoạn code cho phép người dùng tung xúc xắc liên tục, cho đến khi họ nhập "no" thì thoát chương trình.

Mong rằng giải thích này giúp ích! Hãy cho mình biết nếu bạn có thắc mắc gì nhé.
"""
import random

min_val = 1
max_val = 6

"""
Muốn tung xúc xắc không ? (yes/no): yes
Đang Tung Xúc Xắc ...
Những giá trị là:
5
2
Muốn tung xúc xắc không ? (yes/no): yes
Đang Tung Xúc Xắc ...
Những giá trị là:
5
2
Muốn tung xúc xắc không ? (yes/no): no
"""
while True:
    roll_again = input("Muốn tung xúc xắc không ? (yes/no): ").lower()

    if roll_again not in ("yes", "no"):
        print("Chọn lại đi bạn :(")
    elif roll_again in "no":
        break
    else:
        print("Đang Tung Xúc Xắc ...")
        print("Những giá trị là:")

        print(random.randint(min_val, max_val))
        print(random.randint(min_val, max_val))
