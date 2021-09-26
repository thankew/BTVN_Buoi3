import turtle
t = turtle.Turtle()
# Hinh vuong
def square(w,c):
    t.fillcolor(c)
    t.begin_fill()
    for i in range(4):
        t.forward(w)
        t.right(90)
    t.end_fill()
    turtle.done()


# Hinh tron
def circle(r,c):
    t.fillcolor(c)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    turtle.done()


# Hinh tam giac deu
def triangle(a,i):
    t.fillcolor(i)
    t.begin_fill()
    for i in range(3):
        t.forward(a)
        t.left(120)
    t.end_fill()
    turtle.done()

# Hinh chu nhat
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

a = "Xin chao! Hay nhap hinh ban muon ve" \
    " Hinh vuong: S." \
    " Hinh tam giac: T." \
    " Hinh tron: C." \
    " Hinh chu nhat: R.  "
print(a)
m = raw_input("Hinh muon ve la: ",)
if m == "S":
    w = input("Hay nhap do dai: ")
    c = str(input("Hay nhap mau: "))
    square(w,c)
elif m == "C":
    w = input("Hay nhap ban kinh: ")
    c = input("Hay nhap mau: ")
    circle(w,c)
elif m == "T":
    w = input("Hay nhap do dai canh tam giac: ")
    c = input("Hay nhap mau: ")
    triangle(w,c)
elif m == "R":
    a = input("Hay nhap do dai canh a: ")
    b = input("Hay nhap do dai canh b: ")
    c = input("Hay nhap mau: ")
    rectangular(a,b,c)

