import turtle


def a(l):
    t.forward(l)


def f(l, n):
    for i in range(0, 2):
        f1(l, n)
        t.right(120)
    f1(l, n)
    t.right(180)
    for i in range(0, 3):
        f1(l, n)
        t.left(120)


def f1(l, n):
    if n == 1:
        a(l)
    else:
        f1(l / 2, n - 1)
        t.left(120)
        f1(l / 4, n - 1)
        t.right(180)
        f1(l / 4, n - 1)
        t.left(120)
        f1(l / 4, n - 1)
        t.right(180)
        f1(l / 4, n - 1)
        t.left(120)
        f1(l / 2, n - 1)


t = turtle.Turtle()
t.hideturtle()
color2 = ["FireBrick", "coral", "ForestGreen", "RoyalBlue", "pink"]
t.speed(0)
t.left(90)
t.width(2)
while True:
    c = turtle.Screen().numinput("", "Length of side", default=100)
    z = turtle.Screen().numinput("", "Depth of fractal", default=3)
    x = turtle.Screen().numinput("", "Start x", default=0)
    y = turtle.Screen().numinput("", "Start y", default=0)
    t.penup()
    t.color(color2[int(1)])
    t.setpos(x, y)
    t.pendown()
    t.setheading(0)
    f(c, z)
    t.setheading(0)
