"""
Đây là giải thích cho đoạn code Python trên:

Đầu tiên, import thư viện random để tạo các lựa chọn ngẫu nhiên:

```python
import random
```

Tiếp theo, khởi tạo các danh sách (list) chứa các từ khác nhau để xây dựng nên câu chuyện:

```python
when = ['Vài năm trước', 'Hôm qua', 'Tối qua', 'Lâu lắm rồi','Vào ngày 20 tháng 1']
who = ['một con thỏ', 'một con voi', 'một con chuột', 'một con rùa','một con mèo'] 
residence = ['Hà Nội', 'TP HCM', 'Đà Nẵng', 'Hải Phòng', 'Quảng Nam']
went = ['rạp chiếu phim', 'trường học', 'hội thảo', 'siêu thị', 'quán ăn']  
happened = ['kết bạn mới', 'ăn một chiếc bánh burger', 'tìm thấy một chiếc chìa khóa bí mật', 'giải một bí ẩn', 'viết một cuốn sách']
```

Sau đó, sử dụng hàm random.choice() để chọn ngẫu nhiên 1 phần tử từ mỗi danh sách và ghép chúng lại thành một câu: 

```python 
print(random.choice(when) + ', ' + random.choice(who) + ' sống ở ' + random.choice(residence) + ', đi đến ' + random.choice(went) + ' và ' + random.choice(happened))
```

Như vậy, mỗi lần chạy code sẽ in ra một câu chuyện ngẫu nhiên khác nhau từ các từ có sẵn trong các danh sách.

Bạn có thể thêm nhiều từ hơn vào các danh sách để tạo ra nhiều câu chuyện thú vị!
"""
import random

when = ['Vài năm trước', 'Hôm qua', 'Tối qua',
        'Lâu lắm rồi', 'Vào ngày 20 tháng 1']
who = ['một con thỏ', 'một con voi',
       'một con chuột', 'một con rùa', 'một con mèo']

residence = ['Hà Nội', 'TP HCM', 'Đà Nẵng', 'Hải Phòng', 'Quảng Nam']

went = ['rạp chiếu phim', 'trường học', 'hội thảo', 'siêu thị', 'quán ăn']
happened = ['kết bạn mới', 'ăn một chiếc bánh burger',
            'tìm thấy một chiếc chìa khóa bí mật', 'giải một bí ẩn', 'viết một cuốn sách']

# Hôm qua, một con rùa sống ở TP HCM, đi đến siêu thị và kết bạn mới
print(random.choice(when) + ', ' + random.choice(who) + ' sống ở ' + random.choice(
    residence) + ', đi đến ' + random.choice(went) + ' và ' + random.choice(happened))
