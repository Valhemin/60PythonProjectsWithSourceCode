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
