import tkinter

canvas = tkinter.Canvas()
canvas.pack()

vel = 30
x, y = 10,  10
col1, col2 = 'maroon', 'gold'
riadky = int(input('zadaj pocet riadkov:'))
stlpce = int(input('zadaj pocet stlpcov:'))
for j in range(stlpce):
    col1, col2 = col2, col1
    x = 10
    for i in range(riadky):
        if i % 2:
            color = col1
        else:
            color = col2
        canvas.create_rectangle(x,y,x+vel,y+vel, fill=color)
        x = x + (vel+3)
    y = y + vel + 3
canvas.mainloop()