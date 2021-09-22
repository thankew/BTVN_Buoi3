class people:
    full_name = ""
    phone = []
    email = []
    address = ""
    note = ""
    tags = []
    def __init__(self,full_name,phone,email,address,note,tags):
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.address = address
        self.note = note
        self.tags = tags

thanh = people("Thành","Thành Nguyễn",["0123","4533"],["thanhhh@gmail.com","thzzzz@yahoo.com"],"Hà Nội",["friend","work"])

#Show information:
def show_info(thanh):
    print(thanh.full_name,thanh.phone,thanh.email,thanh.address,thanh.note,thanh.tags)


edit = '''
    Thông tin có thể thay đổi
    1. Tên
    2. SĐT
    3. Email
    4. Địa chỉ
   
'''
def edit_name(thanh):
    print("Bạn muốn đổi tên. Tên hiện tại là: " + str(thanh.full_name))
    change = input("Nhập tên muốn đổi: ")
    thanh = people(change, change, ["0123", "4533"], ["thanhhh@gmail.com", "thzzzz@yahoo.com"], "Hà Nội",
                   ["friend", "work"])
    print("Thông tin được cập nhật. Danh bạ mới là:")
    show_info(thanh)

def edit_phone(thanh):
    print("Bạn muốn đổi SĐT. SĐT hiện tại là: " + str(thanh.phone))
    change = input("Nhập SĐT muốn đổi: ")
    thanh = people("Thành","Thành Nguyễn",[change],["thanhhh@gmail.com","thzzzz@yahoo.com"],"Hà Nội",["friend","work"])
    print("Thông tin được cập nhật. Danh bạ mới là:")
    show_info(thanh)

def edit_email(thanh):
    print("Bạn muốn đổi email. Email hiện tại là: " + str(thanh.email))
    change = input("Nhập SĐT muốn đổi: ")
    thanh = people("Thành","Thành Nguyễn",["0123","4533"],[change],"Hà Nội",["friend","work"])
    print("Thông tin được cập nhật. Danh bạ mới là:")
    show_info(thanh)

def edit_adress(thanh):
    print("Bạn muốn đổi địa chỉ. Địa chỉ hiện tại là: " + str(thanh.address))
    change = input("Nhập địa chỉ muốn đổi: ")
    thanh = people("Thành","Thành Nguyễn",["0123","4533"],["thanhhh@gmail.com","thzzzz@yahoo.com"],change,["friend","work"])
    print("Thông tin được cập nhật. Danh bạ mới là:")
    show_info(thanh)

def edit_info(thanh):
    print(edit)
    choice = input("Nhập thông tin bạn muốn thay đổi 1/2/3/4/5/6: ")
    if choice == "1":
        edit_name(thanh)
    elif choice == "2":
        edit_phone(thanh)
    elif choice == "3":
        edit_email(thanh)
    elif choice == "4":
        edit_adress(thanh)

def check_tag(thanh):
    tag = input("Nhập vào tag cần kiểm tra: ").lower()
    for tag1 in thanh.tags:
        if tag1 == tag:
            print(True)
        else:
            print(False)

#User_guide:
guide = '''
    Quản lý danh bạ
    1. Sửa danh bạ
    2. Hiển thị danh bạ
    3. Kiểm tra tag
'''

print(guide)
user_input = input("Nhập chức năng muốn thực hiện 1/2/3: ")
if user_input == "1":
    edit_info(thanh)
elif user_input == "2":
    show_info(thanh)
elif user_input == "3":
    check_tag(thanh)