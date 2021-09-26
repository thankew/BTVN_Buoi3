a = int(input('nhap vao so nam: '))
if a <= 0:
    print("Xin hay nhap lai nam")
elif a % 10 == 0:
    b = "Canh"
elif a % 10 == 1:
    b = "Tan"
elif a % 10 == 2:
    b = "Nham"
elif a % 10 == 3:
    b = "Quy"
elif a % 10 == 4:
    b = "Giap"
elif a % 10 == 5:
    b = "At"
elif a % 10 == 6:
    b = "Binh"
elif a % 10 == 7:
    b = "Dinh"
elif a % 10 == 8:
    b = "Mau"
elif a % 10 == 9:
    b = "Ky"
elif a % 12 == 0:
    print("Day la nam" + str(b) + "Ty")
elif a % 12 == 1:
    print("Day la nam" + str(b) + "Suu")
elif a % 12 == 2:
    print("Day la nam" + str(b) + "Dan")
elif a % 12 == 3:
    print("Day la nam" + str(b) + "Mao")
elif a % 12 == 4:
    print("Day la nam" + str(b) + "Thin")
elif a % 12 == 5:
    print("Day la nam" + str(b) + "Ti")
elif a % 12 == 6:
    print("Day la nam" + str(b) + "Ngo")
elif a % 12 == 7:
    print("Day la nam" + str(b) + "Mui")
elif a % 12 == 8:
    print("Day la nam" + str(b) + "Than")
elif a % 12 == 9:
    print("Day la nam" + str(b) + "Dau")
elif a % 12 == 10:
    print("Day la nam" + str(b) + "Tuat")
elif a % 12 == 11:
    print("Day la nam" + str(b) + "Hoi")
