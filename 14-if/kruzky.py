import tkinter
n = 13
ch = n*20
cv = n*20
canvas = tkinter.Canvas(width=cv, height=ch)
canvas.pack()

for i in range(n):  # riadky
    for j in range(n):  # stlpce
        x = j*20 + 10
        y = i*20 + 12
        if i == 6:
            color = 'red'
        elif j == 6:
            color = 'red'
        else:
            color = 'white'
        canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill=color)

canvas.mainloop()