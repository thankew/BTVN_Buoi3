year = int(input("Nhap so nam: "))
if year > 0 and year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(str(year) + " la nam nhuan")
else:
    print(str(year) + " khong phai la nam nhuan")


