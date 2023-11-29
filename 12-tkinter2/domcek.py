import tkinter
# import random

canvas = tkinter.Canvas(width = 1000, height = 700)
canvas.pack()
x = 5
y = 5
d = 20
xx = x
for g in range(467//d):
    for j in range(998//d):
        canvas.create_polygon(x+d//2,y,x+d,y+d//2,x,y+d//2, fill="red")
        canvas.create_rectangle(x,y+d*0.5,x+d,y+d*1.5, fill='green')
        canvas.create_line(x,y+d//2,x+d,y+d//2)
        canvas.create_rectangle(x+d*0.25,y+d*0.75,x+d*0.75,y+d*1.25,fill="cyan")
        canvas.create_line(x+d//2,y+d*0.75,x+d//2,y+d*1.25)
        canvas.create_line(x+d*0.25,y+d,x+d*0.75,y+d)
        x= x+d
    y= y+d*1.5
    x = xx
canvas.mainloop()