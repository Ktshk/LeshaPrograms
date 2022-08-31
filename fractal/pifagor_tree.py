import turtle


def f(l, n):
    if n == 0:
        t.forward(l)
        t.right(180)
        t.forward(l)
    else:
        t.forward(l)
        t.right(45)
        f(l - l / 3, n - 1)
        t.right(90)
        f(l - l / 3, n - 1)
        t.right(45)
        t.forward(l)


t = turtle.Turtle()
t.fillcolor("orange")
t.speed(0)
t.left(90)
while True:
    c = turtle.Screen().numinput("", "Length of side", default=100)
    z = turtle.Screen().numinput("", "Depth of fractal", default=5)
    x = turtle.Screen().numinput("", "Start x", default=0)
    y = turtle.Screen().numinput("", "Start y", default=0)
    t.penup()
    t.setpos(x, y)
    t.pendown()
    f(c, z)
    t.left(90)
