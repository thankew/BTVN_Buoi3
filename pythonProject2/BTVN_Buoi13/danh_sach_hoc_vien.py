list_header = ("Danh sách học viên:\n"
        "Mã số\tHọ tên\t\tGiới tính\t Quê Quán\tĐiểm thi lý thuyết\tĐiểm thi thực hành\t Điểm Tổng Kết Đánh giá")
list_content = ("sv1\t\tNgô Thị F\t\tNữ\t\tLai Châu\t100\t\t\t\t\t44\t\t\t\t\t72\t\t\t\t\tKhông Đỗ\n"
    "sv2\t\tNguyễn Văn A\tNam\t\tKiên Giang\t100\t\t\t\t\t83\t\t\t\t\t91.5\t\t\t\t\tĐỗ\n"
    "sv3\t\tNguyễn Văn B\tNam\t\tVũng Tàu\t11\t\t\t\t\t45\t\t\t\t\t28\t\t\t\t\tKhông Đỗ\n"
    "sv4\t\tNguyễn Thị C\tNữ\t\tCần Thơ\t\t83\t\t\t\t\t68\t\t\t\t\t75.5\t\t\t\t\tĐỗ\n"
    "sv5\t\tNguyễn Văn D\tNam\t\tHải Phòng\t84\t\t\t\t\t84\t\t\t\t\t84\t\t\t\t\tĐỗ")
list_pass = ("sv2\t\tNguyễn Văn A\tNam\t\tKiên Giang\t100\t\t\t\t\t83\t\t\t\t\t91.5\t\t\t\t\tĐỗ\n"
    "sv4\t\tNguyễn Thị C\tNữ\t\tCần Thơ\t\t83\t\t\t\t\t68\t\t\t\t\t75.5\t\t\t\t\tĐỗ\n"
    "sv5\t\tNguyễn Văn D\tNam\t\tHải Phòng\t84\t\t\t\t\t84\t\t\t\t\t84\t\t\t\t\tĐỗ")
list_fail = ("sv1\t\tNgô Thị F\t\tNữ\t\tLai Châu\t100\t\t\t\t\t44\t\t\t\t\t72\t\t\t\t\tKhông Đỗ\n"
    "sv3\t\tNguyễn Văn B\tNam\t\tVũng Tàu\t11\t\t\t\t\t45\t\t\t\t\t28\t\t\t\t\tKhông Đỗ\n")


def intruction():
    intro = '''Quản lý thông tin học viên:
    1.Thêm thông tin học viên vào bộ nhớ
    2.Cập nhật thông tin học viên
    3.Hiển thị danh sách tất cả học viên
    4.Hiển thị danh sách học viên thi đỗ (Điểm trung bình >= 75)
    5.Hiển thị danh sách học viên thi trượt (Điểm trung bình < 75)
    6.Xóa thông tin của học viên
    7.Thoát chương trình'''
    print(intro)