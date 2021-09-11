#Hiển thị học sinh
header = ("Mã số\tHọ tên\t\tGiới tính\t Quê Quán\tĐiểm thi lý thuyết\tĐiểm thi thực hành\t Điểm Tổng Kết Đánh giá")

student = '''1221 Thắng Nam Kiên Giang 22 64
1222 Chiến Nam Vũng Tàu 11 45
1223 Duy Nam Cần Thơ 83 68
1224 Kiên Nam Hải Phòng 84 58
1225 Thảo Nữ Cà Mau 6 34
1226 Ngọc Nữ Lai Châu 100 44
1227 Bảo Nam Cao Bằng 6 19
1228 Trân Nữ Hà Tĩnh  44 26
'''
split_student = student.split("\n")

#Thêm thông tin học sinh
def add_student(split_student):
    print("Thêm thông tin học viên")
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
    split_student.append(f"{a1} {a2} {a2} {a4} {a5} {a6}")
    print(header)
    print(split_student)

#Xóa thông tin học viên
def remove_student(split_student):
    print("Xóa thông tin học viên")
    remove_id = input("Hãy nhập vào mã số của học viên muốn xóa khỏi bộ nhớ: ")
    new_students_list = ""
    for std in split_student:
        info = std.split(" ")
        id = info[0]
        if id != remove_id:
            new_students_list += std + "\n"
    print(new_students_list)

#Instruction
instruction = '''Phần mềm quản lý học viên:
1.Thêm thông tin học viên vào List
2.Hiển thị danh sách tất cả học viên trong List
3.Xóa thông tin của học viên (theo vị trí) khỏi List
'''
print(instruction)
choice = input("Nhập lựa chọn của bạn (1/2/3): ")
if choice == "1":
    add_student(split_student)
elif choice == "2":
    print("Hiển thị thông tin học viên")
    print(header)
    print(student)
elif choice == "3":
    remove_student(split_student)
print("Kết thúc chương trình")