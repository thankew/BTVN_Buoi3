
#Định nghĩa lớp (define class)
class Car:
    name = ""
    model = ""
    year = 0
    color = ""
    def __init__(self,name,model,year,color):
        self.name = name
        self.model = model
        self.year = year
        self.color = color

#Khởi tạo, xây dựng đối tượng (create new objects):

ford = Car("Ford","Ranger",2020,"red")
mazda = Car("Mazda","C",2021,"white" )

