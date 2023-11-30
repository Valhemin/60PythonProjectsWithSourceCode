"""
Đoạn code Python này dùng để tạo mật khẩu ngẫu nhiên. Hãy cùng tìm hiểu từng dòng:

```python
import random
import string
```

Nhập các thư viện random và string để sử dụng các hàm liên quan đến ngẫu nhiên và chuỗi.

```python 
chars = string.printable.strip()
```

Tạo biến chars bằng cách gọi hàm string.printable để lấy tất cả các ký tự có thể in được, 
sau đó dùng hàm strip() để loại bỏ ký tự khoảng trắng ở đầu và cuối.

```python
pass_len = int(input("Enter the password length: "))
```

Nhập độ dài mật khẩu từ người dùng và chuyển nó về kiểu số nguyên.

```python
password = ''.join(random.sample(chars, k=pass_len))
```

Tạo mật khẩu bằng cách:
- Sử dụng hàm random.sample để lấy một mẫu ngẫu nhiên ký tự từ biến chars với độ dài bằng pass_len
- Nối chuỗi các ký tự lại với nhau thành một chuỗi duy nhất thông qua hàm join.

```python
print(password)
```

In mật khẩu ngẫu nhiên vừa tạo ra.

Như vậy, đoạn code trên cho phép người dùng nhập vào độ dài mật khẩu mong muốn, 
sau đó tự động tạo ra một mật khẩu ngẫu nhiên với độ dài đó.
"""
import random
import string

chars = string.printable.strip()
pass_len = int(input("Enter the password length: "))

"""Demo
Enter the password length: 10
EGCk]Os8ja
"""
password = ''.join(random.sample(chars, k=pass_len))
print(password)
