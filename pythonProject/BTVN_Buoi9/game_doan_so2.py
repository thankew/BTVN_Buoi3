
import random
randomNumber = random.randint(1,10)
for i in range(3):
    so_chon = int(input("Hay nhap vao so nguyen tu 1 toi 10: "))
    if so_chon == randomNumber:
        print(randomNumber)
        print("Xin chuc mung ban ^^!~. So ban chon la so ngau nhien")
        break
    elif so_chon < randomNumber:
        print("So ban chon nho hon so ngau nhien")
    else:
        print("So ban chon lon hon so ngau nhien")
    print("Ban con " + str(2-i) + " luot")
else:
    print("Xin loi! Chuc may man lan sau")
    print("So ngau nhien la " + str(randomNumber))
