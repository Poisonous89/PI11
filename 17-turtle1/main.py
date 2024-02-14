import turtle

t = turtle.Turtle()
t.speed(0)

def stvorce(opakovanie):
    for j in range(1,opakovanie+1):
        for i in range(4):
            t.fd(50*j)
            t.right(90)
        t.penup()
        t.left(135)
        t.fd(35.35533906)
        t.right(135)
        t.pendown()

stvorce(5)


turtle.mainloop()