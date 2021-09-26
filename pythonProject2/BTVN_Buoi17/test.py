
class rectangular:
    width = 0
    length = 0

    def __init__(self, width,length):
        self.width = width
        self.length = length

    def rec_area(self):
        return self.width* self.length
    def rec_peri(self):
        return (self.width+self.length)*2
    def rec_draw(self):
        import turtle as t
        for i in range(2):
            t.forward(self.width)
            t.left(90)
            t.forward(self.length)
            t.left(90)

a1 = rectangular(100,200)
print(rectangular.rec_area(a1))
print(rectangular.rec_draw(a1))

