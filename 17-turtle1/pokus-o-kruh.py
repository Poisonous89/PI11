import turtle

t = turtle.Turtle()


def kruh(opakovanie):
    for j in range(1, opakovanie):
        for i in range(72):
            t.forward(5)
            t.right(1*i)


def kruch():
    for i in range(72):
        t.forward(5)
        t.left(5)

kruh(10)

# print(t.pos())

turtle.mainloop()