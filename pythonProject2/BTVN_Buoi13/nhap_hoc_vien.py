print("Quản lý thông tin học viên")
a1 = input("Nhập Mã SV (sv..): ")
a2 = input("Nhập Họ tên: ")
a3 = input("Nhập Giới tính (M/F): ")
a4 = input("Nhập Quê quán: ")
a5 = 200
while not 0 <= a5 <= 100:
    a5 = float(input("Nhập Điểm thi Lý Thuyết: "))
a6 = 200
while not 0 <= a6 <= 100:
    a6 = float(input("Nhập Điểm thi Thực Hành: "))
a7 = (a5+a6)/2
a8 = 0
if a7 >= 75:
    a8 = "Đỗ"
else:
    a8 = "Trượt"



