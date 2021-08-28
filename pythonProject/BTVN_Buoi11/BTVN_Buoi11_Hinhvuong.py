import turtle
t = turtle.Turtle()
def square(w,c):
    t.fillcolor(c)
    t.begin_fill()
    for i in range(4):
        t.forward(w)
        t.right(90)
    t.end_fill()
    turtle.done()

square(200,"red")


