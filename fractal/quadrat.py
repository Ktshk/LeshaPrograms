import turtle


def a(x, y, l):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.begin_fill()
    for i in range(0, 4):
        t.right(90)
        t.forward(l)
    t.end_fill()


def f(l, n, x, y):
    if n == 1:
        a(x, y, l)
    else:
        f(l / 3, n - 1, x, y)
        f(l / 3, n - 1, x - l / 3, y)
        f(l / 3, n - 1, x - (l / 3) * 2, y)
        f(l / 3, n - 1, x, y - l / 3)
        f(l / 3, n - 1, x - l / 3 * 2, y - l / 3)
        f(l / 3, n - 1, x, y - l / 3 * 2)
        f(l / 3, n - 1, x, y - l / 3 * 2)
        f(l / 3, n - 1, x - l / 3, y - l / 3 * 2)
        f(l / 3, n - 1, x - l / 3 * 2, y - l / 3 * 2)


t = turtle.Turtle()
t.fillcolor("orange")
t.speed(0)
while True:
    c = turtle.Screen().numinput("", "Length of side", default=100)
    z = turtle.Screen().numinput("", "Depth of fractal", default=3)
    x = turtle.Screen().numinput("", "Start x", default=0)
    y = turtle.Screen().numinput("", "Start y", default=0)
    f(c, z, x, y)
