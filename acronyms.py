"""
- Chương trình tạo từ viết tắt với Python
- Từ viết tắt là dạng ngắn của một từ được tạo bởi các từ hoặc cụm từ dài 
như NLP để xử lý ngôn ngữ tự nhiên
"""
# Dòng này nhận vào input từ người dùng và lưu vào biến user_input.
# Hàm input() sẽ hiển thị "Enter a Pharse: " để nhắc người dùng nhập vào một cụm từ.
user_input = input("Enter a Pharse: ")

# Dòng này tách chuỗi user_input thành một danh sách các từ và lưu vào biến words.
# Hàm split() mặc định sẽ tách chuỗi input tại khoảng trắng.
words = user_input.split()

# Khởi tạo biến result là một chuỗi rỗng.
result = ''

# Vòng lặp for duyệt qua từng phần tử trong danh sách words. 
# Với mỗi từ, lấy ký tự đầu tiên của từ đó (word[0]) rồi viết hoa nó bằng hàm upper(), 
# cuối cùng nối vào biến result.
# Như vậy sau vòng lặp, biến result sẽ chứa ký tự đầu viết hoa của mỗi từ trong cụm từ người dùng nhập vào.
for word in words:
    result += word[0].upper()

""" Demo:
Enter a Pharse: Artificial Intelligence
AI
"""
# In ra kết quả đã tạo ở các bước trước.
print(result)
