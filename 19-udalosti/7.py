import tkinter

def tahaj(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='red')

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<Motion>', tahaj)      # '<Motion>' namiesto '<ButtonPress>'

tkinter.mainloop()