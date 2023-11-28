"""
Đây là một dòng code Python để nhập và xử lý email của người dùng.

input("Enter your email: ")
- Hàm input() dùng để nhập dữ liệu từ bàn phím của người dùng. Trong ngoặc kép là chuỗi ký tự "Enter your email:" - đây là lời nhắc sẽ hiển thị ra nhắc người dùng nhập email.

.strip()
-sau khi người dùng nhập xong, email được lưu trong biến email. .strip() là phương thức để xóa khoảng trắng thừa ở đầu và cuối chuỗi văn bản. Điều này đảm bảo rằng email sẽ không có khoảng trắng không mong muốn.

Như vậy, toàn bộ dòng code sẽ hiển thị lời nhắc "Enter your email: " để người dùng nhập, sau đó lưu giá trị đã nhập vào biến email và loại bỏ khoảng trắng thừa ở 2 đầu.
"""
email = input("Enter your email: ").strip()

"""
Đây là đoạn code Python để tìm vị trí ký tự @ trong chuỗi biến email và gán vị trí đó vào biến at_index.

Cụ thể:

email: biến chứa chuỗi email do người dùng nhập vào ở câu lệnh trước đó

.index('@'): phương thức index() dùng để tìm vị trí xuất hiện đầu tiên của một ký tự hoặc chuỗi con trong chuỗi. Ở đây tìm vị trí của ký tự @.

Nếu không tìm thấy @ trong email thì sẽ báo lỗi ValueError.

at_index: biến để lưu vị trí của ký tự @ được tìm thấy.

Như vậy, dòng code này sẽ tìm vị trí xuất hiện đầu tiên của ký tự @ trong chuỗi email, sau đó gán vị trí đó vào biến at_index. Biến này có thể được dùng để xử lý tiếp các logic liên quan tới email sau này.
"""
at_index = email.index('@')

"""
Đoạn code này dùng để tách tên người dùng và tên miền từ địa chỉ email:

email là biến chứa chuỗi email đã nhập
at_index là vị trí của ký tự @ trong email, được tìm ở câu lệnh trước

email[:at_index]: Cắt chuỗi email từ vị trí đầu cho tới vị trí trước ký tự @. Đây chính là tên người dùng.

email[at_index+1:]: Cắt chuỗi email từ vị trí sau ký tự @ cho tới hết. Đây chính là tên miền.

Sau đó gán 2 phần đã cắt này vào 2 biến tương ứng:
user_name: lưu phần tên người dùng
domain_name: lưu phần tên miền

Như vậy, chúng ta đã tách được tên người dùng và tên miền thành công từ địa chỉ email.

Các biến user_name và domain_name này có thể được xử lý tiếp ở các câu lệnh sau.
"""
user_name = email[:at_index]
domain_name = email[at_index+1:]

"""Demo
Enter your email: support@thecleverprogrammer.com
Your username is 'support', your domain name is 'thecleverprogrammer.com'
"""
"""
Đây là câu lệnh để in ra kết quả cuối cùng - tên người dùng và tên miền sau khi đã được tách từ email ở các dòng trước đó.

Cụ thể:

print(): in ra màn hình console

f"": dùng để format string. Trong ngoặc nháy đơn sẽ chèn các biến vào chuỗi.

{user_name}: chèn giá trị của biến user_name vào chuỗi

{domain_name}: chèn giá trị của biến domain_name vào chuỗi 

Như vậy, câu lệnh này sẽ in ra một thông báo với cú pháp: 

Your username is 'tên người dùng', your domain name is 'tên miền'

Điền vào 2 giá trị tương ứng của user_name và domain_name đã được xử lý.

Giúp người dùng biết được kết quả cuối cùng sau khi chạy chương trình.
"""
print(f"Your username is '{user_name}', your domain name is '{domain_name}'")
