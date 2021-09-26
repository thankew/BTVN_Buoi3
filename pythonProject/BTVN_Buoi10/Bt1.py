n = int(input("Nhap so nguyen duong n "))
if n <= 4096:
    print("4kb")
else:
    i = (n // 4096)*4
    if n % 4096 != 0:
        print(str(i+4) + "kb")
    else:
        print(str(i) + "kb")


# Cach 2:
n = int(input("Nhap so nguyen duong n "))
x = n // 4096
kb = x*4 if (n % 4096 ==0) else (x+1)*4
print("Dung luong cua file la: ", str(kb), "KB")


