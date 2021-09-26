kg = float(input('nhap so can nang: '))
m = float(input('nhap so chieu cao: '))
bmi = kg / ( m ** 2 )
if bmi < 16:
    print('gay cap do 3')
elif bmi >= 16 and bmi < 40:
    if bmi < 17:
        print('gay cap do 2')
    elif bmi < 18.5 and bmi >= 17:
        print('gay cap do 1')
    elif bmi < 25 and bmi > 18.5:
        print('binh thuong')
    elif bmi > 25 and bmi < 30:
        print('thua can')
    elif bmi > 30 and bmi < 35:
        print('beo phi cap do 1')
    else:
        print('beo phi cap do 2')
else:
    print('sap chet')