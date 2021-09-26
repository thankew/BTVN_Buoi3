students_list = ('''1221	Nguyễn Văn A	Nam	Kiên Giang	22	64
    1222	Nguyễn Văn B	Nam	Vũng Tàu	11	45
    1223	Nguyễn Văn C	Nam	Cần Thơ	83	68
    1224	Nguyễn Văn D	Nam	Hải Phòng	84	58
    1225	Nguyễn Thị E	Nữ	Cà Mau	6	34
    1226	Ngô Thị F	Nữ	Lai Châu	100	44
    1227	Đinh văn G	Nam	Cao Bằng	6	19
    1228	Phan thị H	Nữ	Hà Tĩnh 	44	26
    1229	Nguyễn thị I	Nữ	Quảng Ngãi	71	72
    1230	Nguyễn Thu K	Nữ	Thừa Thiên Huế	40	44
    1231	Phạm Văn J 	Nam	Hà Giang	69	40
    1232	Hoàng Văn M	Nam	Bến Tre	65	22''')

def list_std_header():
    print(f"{'Mã số':<10}{'Họ tên':^20}{'Giới tính':^10}{'  Tỉnh/Thành phố':<20}{'Điểm thi lý thuyết':>20}"
          f"{'Điểm thi thực hành':>20}")


def show_students():
    list_std_header()
    lst = students_list.split("\n")
    for std in lst:
        if std == "":
            continue
        info = std.split(",")
        code = info[0]
        name = info[1]
        gender = info[2]
        location = info[3]
        theory = info[4]
        practice = info[5]
        print(f"{code:<10}{name:^20}{gender:^10}{location:<20}{theory:>20}{practice:>20}")

show_students()
