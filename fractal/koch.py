import turtle


def a(l):
    t.forward(l)


def f(l, n):
    f1(l, n)
    t.right(120)
    f1(l, n)
    t.right(120)
    f1(l, n)
    t.right(120)


def f1(l, n):
    if n == 1:
        a(l)
    else:
        f1(l / 3, n - 1)
        t.left(60)
        f1(l / 3, n - 1)
        t.right(120)
        f1(l / 3, n - 1)
        t.left(60)
        f1(l / 3, n - 1)


t = turtle.Turtle()
t.fillcolor("orange")
t.speed(0)
t.left(90)
while True:
    c = turtle.Screen().numinput("", "Length of side", default=100)
    z = turtle.Screen().numinput("", "Depth of fractal", default=3)
    x = turtle.Screen().numinput("", "Start x", default=0)
    y = turtle.Screen().numinput("", "Start y", default=0)
    t.penup()
    t.setpos(x, y)
    t.pendown()
    f(c, z)
