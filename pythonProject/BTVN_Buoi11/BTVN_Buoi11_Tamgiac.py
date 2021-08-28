import turtle
t = turtle.Turtle()
def triangle(a,i):
    t.fillcolor(i)
    t.begin_fill()
    for i in range(3):
        t.forward(a)
        t.left(120)
    t.end_fill()
    turtle.done()


