import tkinter
canvas = tkinter.Canvas(width= 500, height=500)
canvas.pack()
def kruh(x, y, r, color):
    canvas.create_oval(x-r,y-r,x+r,y+r,fill=color)


def kruhy_riadok(x,y,pocet,r,color):
    for i in range(pocet):
        kruh(x,y,r,color)
        x = x+2*r


def kruhy_stvorec(x,y,pocet,hlbka,r,color):
    for j in range(hlbka):
        kruhy_riadok(x,y,pocet,r,color)
        y = y + 2*r

kruhy_stvorec(50,50,5,5,30,'red')

canvas.mainloop()