import tkinter, time, random

canvas_width = 400
canvas_height = 700
santa_x = canvas_width//2
santa_y = 128
x = santa_y
santa_posun = 1
canvas = tkinter.Canvas(width=canvas_width, height=canvas_height, bg='black')
canvas.pack()

image_santa = tkinter.PhotoImage(file="santa.png")
santa = canvas.create_image(santa_x, santa_y, image=image_santa)
while True:
    # santa = canvas.create_image(santa_x, santa_y, image=image_santa)
    # for i in range(400):
        canvas.update()
        time.sleep(0.0001)
        canvas.move(santa, 0,santa_posun)
        santa_y = santa_y + santa_posun
        if santa_y == canvas_height + x:
            canvas.delete(santa)
            santa_y = x
            santa = canvas.create_image(santa_x, santa_y, image=image_santa)

canvas.mainloop()