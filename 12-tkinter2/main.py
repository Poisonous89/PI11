import tkinter
import random

canvas = tkinter.Canvas(width = 1000, height = 700)
canvas.pack()
x = 10
y = 10
d = 50
pocet = 998//d         # // je celociselne delenie
dalsi = 698//d
for j in range(dalsi):
    for i in range(pocet):
        color = f'#{random.randrange(256 ** 3):06x}'
        canvas.create_rectangle(x+d,y,x,y+d, fill=color)
        canvas.create_line(x,y,x+d,y+d)
        canvas.create_line(x+d,y,x,y+d)
        x = x+d
    x = x-d*pocet
    y = y+d

canvas.mainloop()