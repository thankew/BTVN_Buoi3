class employee:
    code = 0
    first_name = ""
    last_name = ""
    salary = 0
    def __init__(self,code,first_name,last_name,salary):
        self.code = code
        self.first_name = first_name
        self.last_name = last_name
        self.salary  = float(salary)
    def get_fullname(self):
        print(f"Tên đầy đủ của nhân viên là: " + self.last_name + " " + self.first_name)
    def get_salary(self):
        print(f"Lương hàng tháng của nhân viên là: ", self.salary)
    def get_annual_salary(self):
        print(f"Lương hàng năm của nhân viên là: ",self.salary*12)
    def raise_salary(self,percent):
        raised_salary = self.salary*(1+percent/100)
        raised_annual_salary = raised_salary*12
        print(f"Lương tháng (sau khi tăng) là: ",raised_salary)
        print(f"Lương năm (sau khi tăng) là: ",raised_annual_salary)

