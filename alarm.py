from datetime import datetime  # import thư viện datetime để làm việc với ngày giờ
from playsound import playsound  # import thư viện playsound để phát audio

# nhận input từ người dùng cho thời gian báo thức mong muốn
alarm_time = input("Thời gian báo thức (HH:MM:SS sa/ch): ")

# tìm chỉ số của khoảng trắng giữa thời gian và SA/CH
space_idx = alarm_time.find(' ')

# cắt chuỗi để lấy phần SA hoặc CH
alarm_perd = alarm_time[space_idx+1:]

# cắt chuỗi để lấy phần thời gian báo thức (HH:MM:SS)
alarm_main = alarm_time[:space_idx]

# tách thời gian báo thức thành các thành phần: giờ, phút, giây
alarm_hour, alarm_min, alarm_sec = alarm_main.split(':')

"""Ví dụ 
Thời gian báo thức (HH:MM:SS sa/ch): 11:36:00 PM
Dậy đi!"""
while True:
    # lấy ngày giờ hiện tại
    today = datetime.now()

    # lấy giờ hiện tại theo định dạng 12 giờ
    cur_hour = today.strftime("%I")

    # lấy phút hiện tại
    cur_min = today.strftime("%M")

    # lấy giây hiện tại
    cur_sec = today.strftime("%S")

    # lấy SA/CH hiện tại
    cur_perd = today.strftime("%p")

    # kiểm tra SA/CH hiện tại có khớp đặt báo thức không
    if alarm_perd == cur_perd:
        # kiểm tra giờ hiện tại có khớp giờ báo đặt không
        if alarm_hour == cur_hour:
            # kiểm tra phút hiện tại có khớp phút báo đặt không
            if alarm_min == cur_min:
                # kiểm tra giây hiện tại có khớp giây báo đặt không
                if alarm_sec == cur_sec:
                    print("Dậy đi!")
                    # phát âm báo thức
                    playsound("resources/music/alarm.wav")
                    break
