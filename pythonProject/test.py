a = int(input('nhap vao chieu dai canh thu nhat: '))
b = int(input('nhap vao chieu dai canh thu hai: '))
c = int(input('nhap vao chieu dai canh thu ba: '))
if a <= 0 or b <= 0 or c <= 0:
    print("Error: Xin nhap lai thong so canh tam giac")
elif a+b>c and a+c>b and b+c>a:
    print("Day la 1 tam giac")
    if a == b == c:
        print("Day la 1 tam giac deu")
    elif a == b or b == c or a == c:
        print("Day la 1 tam giac can")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == a**2:
        print("Day la 1 tam giac vuong")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == a**2 and a == b or b == c or a == c:
        print("Day la 1 tam giac vuong can")
    elif a**2 + b**2 < c**2 or b**2 + c**2 < a**2 or a**2 + c**2 < a**2:
        print("Day la 1 tam giac tu")
    else:
        print("Day la 1 tam giac thuong")
else:
    print("Day khong phai 1 tam giac")
