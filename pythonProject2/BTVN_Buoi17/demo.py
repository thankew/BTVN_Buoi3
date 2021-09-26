# list= ["Nguyen","Tra","Mai"]
# my_inter = iter(list)
# while True:
#     try:
#         print(next(my_inter))
#     except StopIteration:
#         break


en_dict = {
    "Laptop": "Máy tính xách tay",
    "Vietnamese": "Người Việt, tiếng Việt",
    "Snake": "Con rắn",
    "Happy": "Hạnh phúc",
    "Sad": "Buồn bã"
}
#def show_dict(en_dict):
#    en_dict1 = iter(en_dict)
#    while True:
#        try:
#            print(next(en_dict1))
#        except StopIteration:
#            break
def show_dict(en_dict):
    en_dict1 = iter(en_dict)
    #show_all = ""
    while True:
        try:
            key = next(en_dict1)
            # meaning = en_dict.get(key)
            meaning = en_dict[key]
            print(f'{key:<10}:{meaning}')
        except StopIteration:
            break
    #print(show_all)

def lookup_dict(en_dict):
    key = input("Nhập từ cần tra: ").lower().capitalize()

    if key in en_dict.keys():
        print(en_dict[key])
    else:
        print("Không có trong từ điển")


# User interface
guide = '''
    Ứng dụng tra từ điển Anh - Việt
    1. Hiển thị list các từ
    2. Tra từ cụ thể
    3. Kết thúc
'''
while True:
    print(guide)
    choice = input("Bạn muốn (1/2/3): ")
    if choice == "1":
        show_dict(en_dict)
    elif choice == "2":
        lookup_dict(en_dict)
    elif choice == "3":
        print("Kết thúc chương trình")
        break
    else:
        print("Xin nhập lại: ")
