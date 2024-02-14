import tkinter, random

canvas = tkinter.Canvas(width=360,height=260)
canvas.pack()
r = 5
for i in range(10000):
    x = random.randint(10,350)
    y = random.randint(10,350)
    if y < 90:
        color = 'black'
    elif y < 170:
        color = 'red'
    else:
        color = 'gold'
    canvas.create_oval(x-r,y-r,x+r,y+r,outline='', fill=color)




canvas.mainloop()