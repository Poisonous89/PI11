import turtle

t = turtle.Turtle()


def hakac(dlzka):
    for i in range(4):
        t.pendown()
        t.fd(dlzka)
        t.rt(90)
        t.fd(dlzka)
        t.penup()
        t.setpos(0, 0)


hakac(50)


turtle.mainloop()