import tkinter
# import random

canvas = tkinter.Canvas(width = 1000, height = 700)
canvas.pack()
x = 50
y = 50
d = 200

canvas.create_polygon(x+d//2,y,x+d,y+d//2,x,y+d//2)
canvas.create_line(x+d//2,y,x+d,y+d//2,x+d,y+d*1.5,x,y+d*1.5,x,y+d//2,x+d//2,y)
canvas.create_line(x,y+d//2,x+d,y+d//2)
canvas.create_rectangle(x+d*0.25,y+d*0.75,x+d*0.75,y+d*1.25,fill="cyan")
canvas.create_line(x+d//2,y+d*0.75,x+d//2,y+d*1.25)
canvas.create_line(x+d*0.25,y+d,x+d*0.75,y+d)

canvas.mainloop()