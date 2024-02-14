import tkinter, random

canvas = tkinter.Canvas(width=380,height=380)
canvas.pack()


def kruhy(x, y):
    for i in range(10):
        r = 50 - 5*i
        color = f'#{random.randrange(256 ** 3):06x}'
        canvas.create_oval(x-r,y-r,x+r,y+r, fill=color)


for j in range(10):
    kruhy(random.randint(50,330),random.randint(50,330))
canvas.mainloop()