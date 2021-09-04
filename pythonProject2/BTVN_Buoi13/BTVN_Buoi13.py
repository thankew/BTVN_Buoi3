
import danh_sach_hoc_vien as ds
instruction =("Quản lý thông tin học viên:\n"
"1.Cập nhật thông tin học viên\n"
"2.Hiển thị danh sách tất cả học viên\n"
"3.Hiển thị danh sách học viên thi đỗ (Điểm trung bình >= 75)\n"
"4.Hiển thị danh sách học viên thi trượt (Điểm trung bình < 75)\n"
"5.Xóa thông tin của học viên")
print(instruction)
option = 7
while not option in range(1, 6):
    option = int(input("Nhập chức năng bạn muốn (1/2/3/4/5): "))

if option == 2:
    print(ds.list_header)
    print(ds.list_content)

elif option == 1:
    import nhap_hoc_vien as nh
    print(ds.list_header)
    print(ds.list_content)
    print(str(nh.a1) + "\t\t" + str(nh.a2) + "\t" + str(nh.a3) + "\t\t" + str(nh.a4) + "\t" + str(nh.a5)
          + "\t\t\t\t\t" + str(nh.a6) + "\t\t\t\t\t" + str(nh.a7) + "\t\t\t\t\t" + str(nh.a8) + "\n")

elif option == 3:
    print(ds.list_pass)
elif option == 4:
    print(ds.list_fail)
else:
    print("Chức năng này ko bít làm :)")