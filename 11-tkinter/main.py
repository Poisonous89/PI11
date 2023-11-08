import tkinter

canvas = tkinter.Canvas()
canvas.pack()
x = 20
y = 10
dlzka = 20
canvas.create_rectangle(x,y,x+dlzka,y+dlzka,fill="red")
canvas.create_rectangle(x+dlzka,y,x+dlzka*2,y+dlzka,fill="red")
canvas.create_rectangle(x+dlzka*2,y,x+dlzka*3,y+dlzka,fill="red")
canvas.create_oval(x+dlzka,y+dlzka,x+dlzka*2,y+dlzka*2,fill="red")
canvas.create_oval(x+dlzka,y+dlzka*2,x+dlzka*2,y+dlzka*3,fill="red")
canvas.create_rectangle(x+dlzka,y+dlzka*3,x+dlzka*2,y+dlzka*4,fill="red")
canvas.create_rectangle(x,y+dlzka*3,x+dlzka,y+dlzka*4,fill="red")
canvas.create_rectangle(x+dlzka*2,y+dlzka*3,x+dlzka*3,y+dlzka*4,fill="red")
canvas.mainloop()