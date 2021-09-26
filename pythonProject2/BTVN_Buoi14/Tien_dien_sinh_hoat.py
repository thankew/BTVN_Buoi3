a = int(input("Nhập số tiền điện sinh hoạt: "))
tien_dien_chua_thue = 0
if a <= 50:
    tien_dien_chua_thue = 1678 * a
    print("Tiền điện sau thuế là: " + str(tien_dien_chua_thue*1.1))
elif a <= 100:
    tien_dien_chua_thue = 1734 * (a - 50) + 1678 * 50
    print("Tiền điện sau thuế là: " + str(tien_dien_chua_thue*1.1))
elif a <= 200:
    tien_dien_chua_thue = 2014 * (a - 100) + 1734 * 50 + 1678 * 50
    print("Tiền điện sau thuế là: " + str(tien_dien_chua_thue*1.1))
elif a <= 300:
    tien_dien_chua_thue = 2536 * (a - 200) + 2014 * 100 + 1734 * 50 + 1678 * 50
    print("Tiền điện sau thuế là: " + str(tien_dien_chua_thue*1.1))
elif a <= 400:
    tien_dien_chua_thue = 2834 * (a - 300) + 2536 * 100 + 2014 * 100 + 1734 * 50 + 1678 * 50
    print("Tiền điện sau thuế là: " + str(tien_dien_chua_thue*1.1))
else:
    tien_dien_chua_thue = 2927 * (a - 400) + 2834 * 100 + 2536 * 100 + 2014 * 100 + 1734 * 50 + 1678 * 50
    print("Tiền điện sau thuế là: " + str(tien_dien_chua_thue*1.1))
