class people:
    full_name = ""
    phone = []
    email = []
    address = ""
    note = ""
    tags = []

    def __init__(self, full_name, phone, email, address, note, tags):
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.address = address
        self.note = note
        self.tags = tags

    def set_name(self,full_name):
        self.full_name = full_name
    def set_phone(self,phone):
        self.phone = phone
    def set_email(self,email):
        self.email = email
    def set_address(self,address):
        self.address = address
    def set_note(self,note):
        self.note = note
    def set_tags(self,tags):
        self.tags = tags

    def show(self):
        return f"""
            * {"Name:":10}{self.full_name}
            * {"Phone:":10}{self.phone}
            * {"Email:":10}{self.email}
            * {"Address:":10}{self.address}
            * {"Note:":10}{self.note}
            * {"Tag":10}{self.tags}
"""

    def check_tag(self,tag):
        return tag in self.tags


thanh = people("Thành","Thành Nguyễn",["0123","4533"],["thanhhh@gmail.com","thzzzz@yahoo.com"],"Hà Nội",["friend","work"])

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
    print("""
    1. Name
    2. Phone
    3. Email
    4. Address
    5. Note
    6. Tags
    """)
    choice = input("Nhập thông tin muốn sửa 1/2/3/4/5/6: ").lower()
    if choice == "1":
        print(thanh.full_name)
        new_choice = input("Giá trị sửa thành là: ")
        print(thanh.set_name(new_choice))
    elif choice ==
elif user_input == "2":
    print(thanh.show())
elif user_input == "3":
    input_tags = input("Nhập tag muốn check: ")
    thanh.check_tag(input_tags)

