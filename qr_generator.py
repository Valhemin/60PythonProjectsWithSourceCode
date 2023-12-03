"""
Đây là cách bạn có thể tạo mã QR cho chuỗi "hello world" và lưu nó dưới dạng ảnh PNG:

```python
import segno

s = "hello world" 

qr = segno.make_qr(s)
qr.save("result.png", scale=10, light="lightblue")
```

Hãy phân tích từng bước:

- Import thư viện `segno` để tạo mã QR  
- Tạo chuỗi `s` với nội dung bạn muốn mã hóa
- Gọi `segno.make_qr(s)` để tạo đối tượng mã QR với nội dung này
- Gọi phương thức `save()` trên đối tượng mã QR để lưu ảnh
- Chỉ định tên file cho ảnh PNG đầu ra (ở đây là `result.png`)
- Tùy chọn tùy biến giao diện bằng cách đặt:
  - `scale` để điều khiển kích thước 
  - `light` cho màu module/quiet zone

Điều chính là gọi `segno.make_qr()` để tạo mã QR ban đầu,
sau đó tùy biến việc lưu với các thông số như scale và màu sắc.

Hãy cho tôi biết nếu bạn có bất kỳ câu hỏi nào khác!
"""
# Các bạn nhớ pip install segno để cài đặt thư viện nhé
import segno

s = "hello world"

resp = segno.make_qr(s)
resp.save(
    "result.png",
    scale=10,
    light="lightblue"
)
