"""
Đây là một game đơn giản cho trò chơi "Kéo, búa, bao" (rock-paper-scissors) bằng Python.

Các điểm chính:

- cpu_score và player_score: các biến toàn cục để lưu trữ điểm số của máy và người chơi

- beats: một dictionary định nghĩa mối quan hệ giữa kéo, búa, bao. Ví dụ "Kéo" thắng "Bao".

- hàm rps: nhận vào lựa chọn của máy và người chơi, so sánh chúng dựa trên beats dictionary, 
cộng điểm cho bên thắng và trả về kết quả

- choices: các lựa chọn hợp lệ 

- Vòng lặp while True: lặp liên tục để chơi nhiều ván
- Máy chọn ngẫu nhiên một lựa chọn
- Nhận input từ người dùng 
- Kiểm tra các điều kiện để kết thúc, lựa chọn không hợp lệ
- Gọi hàm rps để xác định và cộng điểm
- Sau khi kết thúc in ra điểm số của máy và người chơi

Như vậy đây là một game đơn giản sử dụng các khái niệm cơ bản trong python như vòng lặp, dictionary, hàm, biến toàn cục.
"""
import random

cpu_score = player_score = 0


beats = {
    "Kéo": "Bao",
    "Bao": "Búa",
    "Búa": "Kéo"
}


def rps(computer, player):
    global cpu_score, player_score
    if beats[computer] == player:
        cpu_score += 1
        return "Máy Thắng"

    if beats[player] == computer:
        player_score += 1
        return "Bạn Thắng"

    return "Hòa"


choices = ("Kéo", "Búa", "Bao")

"""Demo
Kéo, Búa hay Bao: k
Lựa chọn không hợp lệ
Kéo, Búa hay Bao: Bao
Hòa
Kéo, Búa hay Bao: Búa
Máy Thắng
Kéo, Búa hay Bao: Kéo
Hòa
Kéo, Búa hay Bao: Bao
Bạn Thắng
Kéo, Búa hay Bao: Búa
Bạn Thắng
Kéo, Búa hay Bao: End
Điểm cuối cùng
Điểm của máy    : 1
Điểm của người  : 2
"""
while True:
    computer = random.choice(choices)
    player = input("Kéo, Búa hay Bao: ").capitalize()

    if player == "End":
        print("Điểm cuối cùng")
        print(f"Điểm của máy\t: {cpu_score}")
        print(f"Điểm của người\t: {player_score}")
        break
    elif player not in choices:
        print("Lựa chọn không hợp lệ")
    else:
        print(rps(computer, player))
