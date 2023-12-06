"""
Code bên dưới là một chương trình tính chỉ số BMI (Body Mass Index) của một người. Chỉ số BMI là một chỉ số thể trạng được tính dựa trên cân nặng và chiều cao của một người. Chỉ số BMI được sử dụng để đánh giá tình trạng cân nặng của một người, bao gồm thiếu cân, thừa cân, béo phì,...

Code được viết bằng ngôn ngữ Python. Các biến được sử dụng trong chương trình như sau:

* `height`: Chiều cao của người được tính BMI, đơn vị là cm.
* `weight`: Cân nặng của người được tính BMI, đơn vị là kg.
* `bmi`: Chỉ số BMI của người được tính.

Chương trình hoạt động như sau:

1. Đầu tiên, chương trình yêu cầu người dùng nhập chiều cao và cân nặng của họ.
2. Sau đó, chương trình kiểm tra xem chiều cao và cân nặng có âm hay không. Nếu có, chương trình sẽ in thông báo lỗi và yêu cầu người dùng nhập lại.
3. Nếu chiều cao và cân nặng là số dương, chương trình sẽ tiếp tục.
4. Chương trình sẽ chuyển đổi chiều cao từ cm sang m bằng cách chia chiều cao cho 100.
5. Chương trình sẽ tính chỉ số BMI bằng cách chia cân nặng cho chiều cao bình phương.
6. Cuối cùng, chương trình sẽ in thông báo về tình trạng cân nặng của người được tính.

Ví dụ, nếu người dùng nhập chiều cao là 176 cm và cân nặng là 65 kg, chương trình sẽ in thông báo sau:

```
Nhập chiều cao của bạn theo cm  : 176
Nhập cân nặng của bạn theo kg   : 65
Bạn khỏe mạnh
```

Giải thích chi tiết từng dòng code:

```python
height = float(input("Nhập chiều cao của bạn theo cm\t: "))
```

Dòng code này sẽ yêu cầu người dùng nhập chiều cao của họ và lưu giá trị nhập vào biến `height`. Dòng code này sử dụng hàm `input()` để lấy dữ liệu đầu vào từ người dùng. Hàm `input()` sẽ trả về một giá trị là một chuỗi ký tự. Để chuyển chuỗi ký tự thành số, chúng ta cần sử dụng hàm `float()`.

```python
weight = float(input("Nhập cân nặng của bạn theo kg\t: "))
```

Dòng code này hoạt động tương tự như dòng code trên, chỉ khác là nó lấy dữ liệu đầu vào là cân nặng.

```python
while height < 0 or weight < 0:
  print("\n* Sai rồi, nhập lại bạn ơi *\n")
  height = float(input("Nhập chiều cao của bạn theo cm\t: "))
  weight = float(input("Nhập cân nặng của bạn theo kg\t: "))
```
Dòng code này tạo một vòng lặp `while`. Vòng lặp sẽ chạy liên tục cho đến khi chiều cao và cân nặng đều là số dương. Nếu chiều cao hoặc cân nặng là âm, vòng lặp sẽ in thông báo lỗi và yêu cầu người dùng nhập lại.

```python
height /= 100
```

Dòng code này sẽ chuyển đổi chiều cao từ cm sang m bằng cách chia chiều cao cho 100.

```python
bmi = weight / height**2
```

Dòng code này sẽ tính chỉ số BMI bằng cách chia cân nặng cho chiều cao bình phương.

```python
if bmi <= 16:
  print("Bạn đang thiếu cân nghiêm trọng!")
elif bmi <= 18.5:
  print("Bạn đang thiếu cân")
elif bmi <= 25:
  print("Bạn khỏe mạnh")
elif bmi <= 30:
  print("Bạn đang thừa cân")
else:
  print("Bạn đang thừa cân nghiêm trọng!")
```

Dòng code này sẽ kiểm tra chỉ số BMI và in thông báo về tình trạng cân nặng của người được tính.
"""
height = float(input("Nhập chiều cao của bạn theo cm\t: "))
weight = float(input("Nhập cân nặng của bạn theo kg\t: "))

while height < 0 or weight < 0:
    print("\n* Sai rồi, nhập lại bạn ơi *\n")
    height = float(input("Nhập chiều cao của bạn theo cm\t: "))
    weight = float(input("Nhập cân nặng của bạn theo kg\t: "))

height /= 100

bmi = weight / height**2

"""Demo
Nhập chiều cao của bạn theo cm  : 176
Nhập cân nặng của bạn theo kg   : 65
Bạn khỏe mạnh
"""
if bmi <= 16:
    print("Bạn đang thiếu cân nghiêm trọng!")
elif bmi <= 18.5:
    print("Bạn đang thiếu cân")
elif bmi <= 25:
    print("Bạn khỏe mạnh")
elif bmi <= 30:
    print("Bạn đang thừa cân")
else:
    print("Bạn đang thừa cân nghiêm trọng!")
