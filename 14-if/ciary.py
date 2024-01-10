import tkinter
cv = int(input('zadaj dlzku x:'))
ch = int(input('zadaj dlzku y:'))
canvas = tkinter.Canvas(width = cv, height = ch)
canvas.pack()
xx = int(input('zadaj medzeru medzi ciarami:'))
q = int(input('zadaj hrubku ciary:'))
x = xx
color = 'red'
for i in range(cv//xx):
    canvas.create_line(x,0,x,ch+2,fill=color,width=q)
    canvas.create_line(0,x,cv+2,x,fill=color,width=q)
    x = x + xx
    if color == 'red':
        color = 'blue'
    else:
        color = 'red'

canvas.mainloop()