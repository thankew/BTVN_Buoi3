import turtle
t = turtle.Turtle()
def rectangular(a,b,c):
    t.fillcolor(c)
    t.begin_fill()
    for i in range(2):
        t.forward(a)
        t.left(90)
        t.forward(b)
        t.left(90)
    t.end_fill()
    turtle.done()

rectangular(100,200,"blue")
