import turtle


def a(x, y, l):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.begin_fill()
    t.right(120)
    t.forward(l)
    for i in range(0, 2):
        t.left(120)
        t.forward(l)
    t.end_fill()
    t.right(120)


def f(l, n, x, y):
    if n == 1:
        a(x, y, l)
    else:
        c = (l ** 2 - (l / 2) ** 2) ** 0.5 / 2
        f(l / 2, n - 1, x, y)
        f(l / 2, n - 1, x - l / 4, y - c)
        f(l / 2, n - 1, x + l / 4, y - c)


t = turtle.Turtle()
t.fillcolor("orange")
t.speed(0)
while True:
    c = turtle.Screen().numinput("", "Length of side", default=100)
    z = turtle.Screen().numinput("", "Depth of fractal", default=4)
    x = turtle.Screen().numinput("", "Start x", default=0)
    y = turtle.Screen().numinput("", "Start y", default=0)
    f(c, z, x, y)
