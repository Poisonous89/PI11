import turtle, random

t = turtle.Turtle()
t.speed(0)


def stvorec(vel):
    for i in range(4):
        t.fd(vel)
        t.right(90)

for i in range(50):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.fillcolor(f'#{random.randrange(256 ** 3):06x}')
    t.begin_fill()
    stvorec(30)
    t.end_fill()
    t.penup()
    t.setpos(x,y)
    t.seth(random.randint(1,90))
    t.pendown()



turtle.mainloop()