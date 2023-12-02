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
