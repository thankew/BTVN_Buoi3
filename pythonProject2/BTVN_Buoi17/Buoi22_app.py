import Buoi22_def_class as t

## Test
ms = input("Nhập mã Nhân viên: ")
name = input("Nhập tên Nhân viên: ")
last_name = input("Nhập họ Nhân viên: ")
salary = input("Nhập lương tháng Nhân viên: ")

nv1 = t.employee(ms,name,last_name,salary)

## User interface:
print('''
 Tính năng:
1. Hiện tên đầy đủ nhân viên
2. Hiện lương tháng nhân viên
3. Hiện lương năm của nhân viên
4. Tính tăng lương nhân viên
''')
choice = input("Chọn tính năng 1/2/3/4: ")
if choice == "1":
    t.employee.get_fullname(nv1)
elif choice == "2":
    t.employee.get_salary(nv1)
elif choice == "3":
    t.employee.get_annual_salary(nv1)
elif choice == "4":
    #input validation
    percent = -1
    while percent not in range(1,101):
        percent = int(input("Nhập % tăng lương nhân viên [0->100]: "))
        t.employee.raise_salary(nv1,percent)

