import tkinter, time
canvas = tkinter.Canvas(width=1000, height=1000)
canvas.pack()

s1 = canvas.create_rectangle(10, 10,110,110, fill= 'red')
for k in range(5):
    for g in range(500):
        canvas.update()
        time.sleep(0.005)
        canvas.move(s1, 0.5,0) #posunie objekt s1, o 100, co je na osi x a 0 je posunutie na osi y
    for i in range(500):
        canvas.update()
        time.sleep(0.005)
        canvas.move(s1, 0,0.5)
    for t in range(500):
        canvas.update()
        time.sleep(0.005)
        canvas.move(s1, -0.5,0)
    for j in range(500):
        canvas.update()
        time.sleep(0.005)
        canvas.move(s1, 0,-0.5)
canvas.mainloop()