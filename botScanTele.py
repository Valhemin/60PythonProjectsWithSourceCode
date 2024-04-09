import qrcode 
import telebot
import cv2
import os
import numpy as np
try:
    import pyzbar.pyzbar as pyzbar
except:
    os.system("pip install pyzbar")    

bot = telebot.TeleBot("6790339105:AAHO2dZN-ZjKJ5Qt8IH8o-W50dV5HLQgbSk")

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "CHÀO MỪNG BẠN ĐẾN VỚI QR BOT TELEGRAM")
    
@bot.message_handler(commands=['tacgia'])
def tacgia(message):
    bot.reply_to(message, "NGUYỄN TRƯỜNG CHINH\n\n@Chinhcoder : ZALO : 0776186410") 

# Tiến hành xử lý các mã QR code được quét được tại đây      
@bot.message_handler(commands=['qrcode'])
def tao_qrcode(message):
    try:
        if len(message.text.split()) == 1: 
            bot.reply_to(message, "Không để trống nội dung")
        else:
            link = message.text.split()
            image = qrcode.make(link)
            image.save("qrcode.png")
            bot.send_photo(message.chat.id, open('qrcode.png', 'rb'))
    except :
        bot.reply_to(message, f"Không nhận diện được QRCode")   

@bot.message_handler(commands=['code'])
def tim_qrcode(message):
    bot.reply_to(message, "Hãy gửi một ảnh chứa mã QR code.")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        file_info = bot.get_file(message.photo[-1].file_id) 
        downloaded_file = bot.download_file(file_info.file_path)
        with open('qr_code.jpg', 'wb') as new_file:
            new_file.write(downloaded_file)
        
        if os.path.exists('qr_code.jpg'):
            qr_code_image = cv2.imread('qr_code.jpg')
            qr_code_detector = cv2.QRCodeDetector()
            decoded_data, points, _ = qr_code_detector.detectAndDecode(qr_code_image)
        
            if points is not None:
                decoded_text = decoded_data
                bot.reply_to(message, f"Nội dung của mã QR là: {decoded_text}")
            else:
                bot.reply_to(message, "Không tìm thấy mã QR trong ảnh.")
        else:
            bot.reply_to(message, "Không tìm thấy tệp ảnh.")
    except :
        bot.reply_to(message,"Không nhận diện được QRCode")


@bot.message_handler(func=lambda message: message.text == '1')
def option_1(message):
    bot.reply_to(message, "Nhập QR Code (/qrcode + nội dung)")

@bot.message_handler(func=lambda message: message.text == '2')
def option_2(message):
    bot.reply_to(message, "Gửi ảnh QR Code cần tìm kiếm ")

@bot.message_handler(func=lambda message: message.text not in ["/start", "/qrcode", "/tacgia", "/code"])
def option_menu(message):
    bot.reply_to(message, "Xin lỗi, tôi không hiểu ý bạn! Hãy chọn 1 trong những lựa chọn bên dưới 👇\n( 1 ) : Tạo QR Code\n( 2 ) : Tìm kiếm nội dung QR Code\n\n(/tacgia)")   
         
bot.polling()
