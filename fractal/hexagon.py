import turtle


def a(l):
    for i in range(0, 6):
        t.right(60)
        t.forward(l)


def f(l, n):
    if n == 1:
        a(l)
    else:
        f(l / 3, n - 1)
        t.right(60)
        t.penup()
        t.forward(l / 3 * 2)
        t.pendown()
        t.left(60)
        f(l / 3, n - 1)
        t.right(120)
        t.penup()
        t.forward(l / 3 * 2)
        t.pendown()
        t.left(120)
        f(l / 3, n - 1)
        t.left(120)
        t.penup()
        t.forward(l / 3 * 2)
        t.pendown()
        t.right(120)
        f(l / 3, n - 1)
        t.left(120)
        t.penup()
        t.forward(l / 3 * 2)
        t.pendown()
        t.right(120)
        f(l / 3, n - 1)
        t.right(120)
        t.penup()
        t.forward(l / 3 * 2)
        t.pendown()
        t.left(120)
        f(l / 3, n - 1)
        t.right(60)
        t.penup()
        t.forward(l / 3 * 2)
        t.pendown()
        t.left(60)
        f(l / 3, n - 1)
        t.left(60)
        t.penup()
        t.forward(l / 3 * 4)
        t.pendown()
        t.right(60)


t = turtle.Turtle()
color2 = ["FireBrick", "coral", "ForestGreen", "RoyalBlue", "pink"]
t.speed(0)
t.left(90)
t.hideturtle()
t.right(60)
while True:
    c = turtle.Screen().numinput("", "Length of side", default=100)
    z = turtle.Screen().numinput("", "Depth of fractal", default=2)
    x = turtle.Screen().numinput("", "Start x", default=0)
    y = turtle.Screen().numinput("", "Start y", default=0)
    t.penup()
    t.color(color2[1])
    t.setpos(x, y)
    t.pendown()
    f(c, z)
