import tkinter
canvas = tkinter.Canvas(width=600, height=600)
canvas.pack()
def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


def stvorce(x, y, pocet, d, r=255, g=255, b=255):
    dd = d
    krok = 255 // pocet
    for i in range(pocet):
        canvas.create_rectangle(x,y,x+d,y+dd, fill=rgb(r,g,b))
        x = x+dd
        if r > krok:
            r -= krok
        if g > krok:
            g -= krok
        if b > krok:
            b -= krok


stvorce(50, 50, 10, 30, 255, 0, 0)
stvorce(50, 100, 10, 30, 0, 255, 0)
stvorce(50, 150, 10, 30, 0, 0, 255)
canvas.mainloop()