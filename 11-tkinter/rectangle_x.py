import tkinter

canvas = tkinter.Canvas()
canvas.pack()

x = 10
y = 10
d = 20
c = "green"
canvas.create_rectangle(x,y,x+d,y+d,fill=c)
canvas.create_rectangle(x+d,y+d,x+2*d,y+2*d,fill=c)
canvas.create_rectangle(x+2*d,y+2*d,x+3*d,y+3*d,fill=c)
canvas.create_rectangle(x+3*d,y+3*d,x+4*d,y+4*d,fill=c)
canvas.create_rectangle(x+4*d,y+4*d,x+5*d,y+5*d,fill=c)
canvas.create_rectangle(x+3*d,y+d,x+4*d,y+2*d,fill=c)
canvas.create_rectangle(x+4*d,y,x+5*d,y+d,fill=c)
canvas.create_rectangle(x+d,y+3*d,x+2*d,y+4*d,fill=c)
canvas.create_rectangle(x,y+4*d,x+d,y+5*d,fill=c)

x = 6 * d
y = 10
c = "red"
canvas.create_rectangle(x,y,x+d,y+d,fill=c)
canvas.create_rectangle(x+d,y+d,x+2*d,y+2*d,fill=c)
canvas.create_rectangle(x+2*d,y+2*d,x+3*d,y+3*d,fill=c)
canvas.create_rectangle(x+3*d,y+3*d,x+4*d,y+4*d,fill=c)
canvas.create_rectangle(x+4*d,y+4*d,x+5*d,y+5*d,fill=c)
canvas.create_rectangle(x+3*d,y+d,x+4*d,y+2*d,fill=c)
canvas.create_rectangle(x+4*d,y,x+5*d,y+d,fill=c)
canvas.create_rectangle(x+d,y+3*d,x+2*d,y+4*d,fill=c)
canvas.create_rectangle(x,y+4*d,x+d,y+5*d,fill=c)

canvas.mainloop()