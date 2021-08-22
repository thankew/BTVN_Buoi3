primecount = int(input("Hay nhap vao 1 so luong so nguyen to muon hien thi "))
count = 0
n = 1
while count < primecount:
    n +=1
    for a in range(2, n // 2 + 1):
        if n % a == 0:
            break
    else:
        print(n)
        count +=1



