import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
turtle.delay(0)
t1.pu()
t1.setpos(-100,0)
t1.pd()
t2.pu()
t2.setpos(100,0)
t2.pd()
t3.pu()
t3.lt(90)
t3.fd(150)
t3.pd()


def ko(d,q):
    for i in range(q):
        for j in range(4):
            t1.fd(d)
            t1.lt(90)
            t2.fd(d)
            t2.lt(90)
            t3.fd(d)
            t3.lt(90)
        t1.lt(360//q)
        t2.lt(360//q)
        t3.lt(360//q)

ko(50,10)


turtle.mainloop()