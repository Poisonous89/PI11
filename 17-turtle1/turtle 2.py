import turtle, random

t = turtle.Turtle()
t.speed(0)


def stvorec(vel):
    for i in range(4):
        t.fd(vel)
        t.right(90)


def sachovnica(vel,farba1,farba2):
    for j in range(1,9):
        for i in range(8):
            farba1, farba2 = farba2, farba1
            t.fillcolor(farba1)
            t.begin_fill()
            stvorec(vel)
            t.end_fill()
            t.penup()
            t.fd(vel)
        farba1, farba2 = farba2, farba1
        t.setpos(0,vel*j)


sachovnica(20,'red','blue')


turtle.mainloop()