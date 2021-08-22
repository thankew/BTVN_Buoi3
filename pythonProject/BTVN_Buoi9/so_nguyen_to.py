i = 0
while i <= 1:
    i = int(input("Hay nhap vao 1 so nguyen duong "))
    for a in range(2, i // 2 + 1):
        if i % a != 0:
            print("So " + str(i) + " la so nguyen to")
        else:
            print("So " + str(i) + " KHONG PHAI la so nguyen to")

