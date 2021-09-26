#Instruction
instruction = '''Phần mềm quản lý học viên:
1.Thêm thông tin học viên vào List
2.Hiển thị danh sách tất cả học viên trong List
3.Xóa thông tin của học viên (theo vị trí) khỏi List
'''
print(instruction)
choice = input("Nhập lựa chọn của bạn (1/2/3): ")
if choice == 1:
    add_student(split_student)
elif choice == 2:
    print(header)
    print(student)
elif choice == 3:
    remove_student(split_student)