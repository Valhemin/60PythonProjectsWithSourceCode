def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0

    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Đúng rồi <3")
            score += 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sai rồi, thử lại!\n")
            attempt += 1

    if attempt == 3:
        print("Câu trả lời đúng là:", answer)


score = 0

"""
1+2=?
1
Sai rồi, thử lại!
1
Sai rồi, thử lại!
1
Câu trả lời đúng là: 3
Điểm: 0
"""

guess = input("1+2=?\n")
check_guess(guess, '3')

print("Điểm:", score)
