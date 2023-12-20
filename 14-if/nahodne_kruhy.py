import tkinter
import random
cw = 500
ch = 500
r = 5
canvas = tkinter.Canvas(width=cw, height=ch)
canvas.pack()

for i in range(2000):
    x = random.randint(r+2, cw-r-2)
    y = random.randint(r+2, ch-r-2)
    if x <= cw//2 and y <= ch//2:
        color = 'yellow'
    elif x <= ch//2 and y >= ch//2:
        color = 'pink'
    elif x >= ch//2 and y >= ch//2:
        color = 'orange'
    else:
        color = 'green'
    canvas.create_oval(x-r,y-r,x+r,y+r,fill=color)


canvas.mainloop()