#List contacts:
contacts = [
    {
        "Name": "Hải",
        "Phone": ["123","456","789"],
        "Email": ["haihai_@yahoo.com","nguyenduyhai@hotmail.com"],
        "Address": "Hà Nam",
        "Tags": ["friend","work"]
        },
    {
        "Name": "Thái",
        "Phone": ["344","222","235"],
        "Email": ["ggoaa_@yahoo.com","thaiii23@hotmail.com"],
        "Address": "Quảng Nam",
        "Tags": ["work"]
    },
    {
        "Name": "Duy",
        "Phone": ["512233","44123","3333"],
        "Email": ["vmgkkk_@yahoo.com","duyyy2@hotmail.com"],
        "Address": "Yên Bái",
        "Tags": ["friend"]
    }
]

#Hiển thị danh bạ:
def show_contact(contacts):
    for ppl in contacts:
        ppl2 = iter(ppl)
        while True:
            try:
                key = next(ppl2)
                # meaning = en_dict.get(key)
                meaning = ppl[key]
                print(f'{key:<10}:{meaning}')
            except StopIteration:
                break
        print("-"*30)

#Tìm kiếm danh bạ
def look_up(contacts):
    look_up = input("Nhập tên cần tra: ").lower().capitalize()
    for ppl in contacts:
        if look_up == ppl["Name"]:
            for ppl2 in ppl.keys():
                print(f'{ppl2}: {ppl[ppl2]}')
            print("Kết thúc")
            break
        else:
            print("Không tìm thấy")

#Xóa danh bạ
def remove_contact(contacts):
    remove = input("Nhập tên cần xóa: ").lower().capitalize()
    for ppl in contacts:
        if remove == ppl["Name"]:
            contacts.remove(ppl)
            break
        else:
            print("Không tìm thấy")
    show_contact(contacts)

#Thay đổi danh bạ
def edit_contact(contacts):
    edit = input("Nhập tên cần thay đổi: ").lower().capitalize()
    for ppl in contacts:
        if edit == ppl["Name"]:
            for ppl2 in ppl.keys():
                print(f'{ppl2}: {ppl[ppl2]}')
            edit_choice = input("Bạn muốn thay đổi (N/P/E/A): ")
            if edit_choice == "N":
                edit_name = input("Thay đổi thành: ")
                ppl["Name"] = edit_name
                for ppl2 in ppl.keys():
                    print(f'{ppl2}: {ppl[ppl2]}')
            elif edit_choice =="A":
                edit_adress = input("Thay đổi thành: ")
                ppl["Address"] = edit_adress
                for ppl2 in ppl.keys():
                    print(f'{ppl2}: {ppl[ppl2]}')
        elif edit != ppl["Name"]:
            print("Không tìm thấy")

#User_interface:
guide = '''
    Quản lý danh bạ:
    1. Hiển thị tất cả danh bạ
    2. Tìm kiếm danh bạ
    3. Xóa danh bạ
    4. Thay đổi danh bạ
'''
def user_guide(contacts):
    print(guide)
    choice = input("Bạn muốn (1/2/3/4): ")
    if choice == "1":
        show_contact(contacts)
    elif choice == "2":
        look_up(contacts)
    elif choice == "3":
        remove_contact(contacts)
    elif choice == "4":
        edit_contact(contacts)
    else:
        print("Chức năng này ko biết làm :D ")

user_guide(contacts)
