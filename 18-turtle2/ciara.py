import turtle, random

t = turtle.Turtle()
t.speed(0)
turtle.delay(0)

#picovina tie farby
# def r():
#     # Red component is always at its maximum (FF)
#     red = 'FF'
#     # Green and blue components are randomly chosen between 00 and FF
#     green = '{:02X}'.format(random.randint(0, 255))
#     blue = '{:02X}'.format(random.randint(0, 255))
#     # Combine all components to get the final color
#     color = '#' + red + green + blue
#     return color
#

def stvorec(dlzka):
    for i in range(4):
        t.fd(dlzka)
        t.rt(90)


def n_uholnik(n, dlzka):
    for i in range(n):
        t.fd(dlzka)
        t.lt(360//n)

# for i in range(3,16):
#     n_uholnik(i, 50)


def obluk(d):
    for i in range(9):
        t.fd(d)
        t.lt(10)


def lupen(d):
    for i in range(2):
        obluk(d)
        t.lt(90)


def kvet(n, d):
    for i in range(n):
        t.fillcolor(f'#{random.randrange(256 ** 3):06x}')
        t.begin_fill()
        lupen(d)
        t.lt(360//n)
        t.end_fill()


def kvety(n,d,p):
    for i in range(p):
        t.penup()
        t.setpos(random.randrange(-250,250),random.randint(-250,250))
        t.pendown()
        kvet(n,d)


kvety(20, 20, 5)
# print(r)

turtle.mainloop()