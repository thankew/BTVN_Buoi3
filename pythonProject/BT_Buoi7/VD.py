# a = int(input('nhap so a: '))
# b = int(input('nhap so b: '))
# m = 0
# for i in range(a,b+1):
#     m += i
# print(m)

# a = int(input('nhap so a: '))
# b = int(input('nhap so b: '))
# for i in range(a,b+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("So " + str(i) + " nen la FizzBuzz")
#     elif i % 3 == 0:
#         print("So " + str(i) + " nen la Fizz")
#     elif i % 5 == 0:
#         print("So 4" + str(i) + " nen la Buzz")

for i in range(5,0,-1):
    print(i*" " + "*"*(6-i))

