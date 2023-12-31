import tkinter
import random
canvas = tkinter.Canvas(width=1000,height=700)
canvas.pack()
d = 9
z = d*35
c = d*8
width = 998//z
height = 698//c
x = 5
y = 5
# d = 4
xx = x
for g in range(height):
    for j in range(width):
        color = f'#{random.randrange(256 ** 3):06x}'
        #pismeno S
        canvas.create_rectangle(x+d,y,x+2*d,y+d,fill=color)
        canvas.create_rectangle(x+2*d,y,x+3*d,y+d,fill=color)
        canvas.create_rectangle(x+3*d,y,x+4*d,y+d,fill=color)
        canvas.create_rectangle(x+4*d,y,x+5*d,y+d,fill=color)
        canvas.create_rectangle(x,y+d,x+d,y+2*d,fill=color)
        canvas.create_rectangle(x,y+2*d,x+d,y+3*d,fill=color)
        canvas.create_rectangle(x+d,y+3*d,x+2*d,y+4*d,fill=color)
        canvas.create_rectangle(x+2*d,y+3*d,x+3*d,y+4*d,fill=color)
        canvas.create_rectangle(x+3*d,y+3*d,x+4*d,y+4*d,fill=color)
        canvas.create_rectangle(x+4*d,y+4*d,x+5*d,y+5*d,fill=color)
        canvas.create_rectangle(x+4*d,y+5*d,x+5*d,y+6*d,fill=color)
        canvas.create_rectangle(x+3*d,y+6*d,x+4*d,y+7*d,fill=color)
        canvas.create_rectangle(x+2*d,y+6*d,x+3*d,y+7*d,fill=color)
        canvas.create_rectangle(x+d,y+6*d,x+2*d,y+7*d,fill=color)
        canvas.create_rectangle(x,y+6*d,x+d,y+7*d,fill=color)
        #pismeno A
        color = f'#{random.randrange(256**3):06x}'
        canvas.create_rectangle(x+6*d,y+6*d,x+7*d,y+7*d,fill=color)
        canvas.create_rectangle(x+6*d,y+5*d,x+7*d,y+6*d,fill=color)
        canvas.create_rectangle(x+6*d,y+4*d,x+7*d,y+5*d,fill=color)
        canvas.create_rectangle(x+6*d,y+3*d,x+7*d,y+4*d,fill=color)
        canvas.create_rectangle(x+6*d,y+2*d,x+7*d,y+3*d,fill=color)
        canvas.create_rectangle(x+6*d,y+d,x+7*d,y+2*d,fill=color)
        canvas.create_rectangle(x+7*d,y,x+8*d,y+d,fill=color)
        canvas.create_rectangle(x+8*d,y,x+9*d,y+d,fill=color)
        canvas.create_rectangle(x+9*d,y,x+10*d,y+d,fill=color)
        canvas.create_rectangle(x+10*d,y+6*d,x+11*d,y+7*d,fill=color)
        canvas.create_rectangle(x+10*d,y+5*d,x+11*d,y+6*d,fill=color)
        canvas.create_rectangle(x+10*d,y+4*d,x+11*d,y+5*d,fill=color)
        canvas.create_rectangle(x+10*d,y+3*d,x+11*d,y+4*d,fill=color)
        canvas.create_rectangle(x+10*d,y+2*d,x+11*d,y+3*d,fill=color)
        canvas.create_rectangle(x+10*d,y+d,x+11*d,y+2*d,fill=color)
        canvas.create_rectangle(x+9*d,y+3*d,x+10*d,y+4*d,fill=color)
        canvas.create_rectangle(x+d*8,y+d*3,x+d*9,y+d*4,fill=color)
        canvas.create_rectangle(x+d*7,y+d*3,x+d*8,y+d*4,fill=color)
        #pismeno M
        color = f'#{random.randrange(256**3):06x}'
        canvas.create_rectangle(x+d*12,y+d*6,x+d*13,y+d*7,fill=color)
        canvas.create_rectangle(x+d*12,y+d*5,x+d*13,y+d*6,fill=color)
        canvas.create_rectangle(x+d*12,y+d*4,x+d*13,y+d*5,fill=color)
        canvas.create_rectangle(x+d*12,y+d*3,x+d*13,y+d*4,fill=color)
        canvas.create_rectangle(x+d*12,y+d*2,x+d*13,y+d*3,fill=color)
        canvas.create_rectangle(x+d*12,y+d,x+d*13,y+d*2,fill=color)
        canvas.create_rectangle(x+d*12,y,x+d*13,y+d,fill=color)
        canvas.create_rectangle(x+d*13,y+d,x+d*14,y+d*2,fill=color)
        canvas.create_rectangle(x+d*14,y+d*2,x+d*15,y+d*3,fill=color)
        canvas.create_rectangle(x+d*14,y+d*3,x+d*15,y+d*4,fill=color)
        canvas.create_rectangle(x+d*15,y+d,x+d*16,y+d*2,fill=color)
        canvas.create_rectangle(x+d*16,y,x+d*17,y+d,fill=color)
        canvas.create_rectangle(x+d*16,y+d,x+d*17,y+d*2,fill=color)
        canvas.create_rectangle(x+d*16,y+d*2,x+d*17,y+d*3,fill=color)
        canvas.create_rectangle(x+d*16,y+d*3,x+d*17,y+d*4,fill=color)
        canvas.create_rectangle(x+d*16,y+d*4,x+d*17,y+d*5,fill=color)
        canvas.create_rectangle(x+d*16,y+d*5,x+d*17,y+d*6,fill=color)
        canvas.create_rectangle(x+d*16,y+d*6,x+d*17,y+d*7,fill=color)
        #pismeno U
        color = f'#{random.randrange(256**3):06x}'
        canvas.create_rectangle(x+d*18,y,x+d*19,y+d,fill=color)
        canvas.create_rectangle(x+d*18,y+d,x+d*19,y+2*d,fill=color)
        canvas.create_rectangle(x+d*18,y+2*d,x+d*19,y+d*3,fill=color)
        canvas.create_rectangle(x+d*18,y+d*3,x+d*19,y+d*4,fill=color)
        canvas.create_rectangle(x+d*18,y+d*4,x+d*19,y+d*5,fill=color)
        canvas.create_rectangle(x+d*18,y+d*5,x+d*19,y+d*6,fill=color)
        canvas.create_rectangle(x+d*19,y+d*6,x+d*20,y+d*7,fill=color)
        canvas.create_rectangle(x+d*20,y+d*6,x+d*21,y+d*7,fill=color)
        canvas.create_rectangle(x+d*21,y+d*6,x+d*22,y+d*7,fill=color)
        canvas.create_rectangle(x+d*22,y+d*5,x+d*23,y+d*6,fill=color)
        canvas.create_rectangle(x+d*22,y+d*4,x+d*23,y+d*5,fill=color)
        canvas.create_rectangle(x+d*22,y+d*3,x+d*23,y+d*4,fill=color)
        canvas.create_rectangle(x+d*22,y+2*d,x+d*23,y+d*3,fill=color)
        canvas.create_rectangle(x+d*22,y+d,x+d*23,y+2*d,fill=color)
        canvas.create_rectangle(x+d*22,y,x+d*23,y+d,fill=color)
        #pismeno E
        color = f'#{random.randrange(256**3):06x}'
        canvas.create_rectangle(x+d*24,y,x+d*25,y+d,fill=color)
        canvas.create_rectangle(x+d*25,y,x+d*26,y+d,fill=color)
        canvas.create_rectangle(x+d*26,y,x+d*27,y+d,fill=color)
        canvas.create_rectangle(x+d*27,y,x+d*28,y+d,fill=color)
        canvas.create_rectangle(x+d*28,y,x+d*29,y+d,fill=color)
        canvas.create_rectangle(x+d*24,y+d,x+d*25,y+2*d,fill=color)
        canvas.create_rectangle(x+d*24,y+2*d,x+d*25,y+d*3,fill=color)
        canvas.create_rectangle(x+d*24,y+d*3,x+d*25,y+d*4,fill=color)
        canvas.create_rectangle(x+d*24,y+d*4,x+d*25,y+d*5,fill=color)
        canvas.create_rectangle(x+d*24,y+d*5,x+d*25,y+d*6,fill=color)
        canvas.create_rectangle(x+d*24,y+d*6,x+d*25,y+d*7,fill=color)
        canvas.create_rectangle(x+d*25,y+d*3,x+d*26,y+d*4,fill=color)
        canvas.create_rectangle(x+d*26,y+d*3,x+d*27,y+d*4,fill=color)
        canvas.create_rectangle(x+d*27,y+d*3,x+d*28,y+d*4,fill=color)
        # canvas.create_rectangle(x+d*28,y+d*3,x+d*29,y+d*4,fill=color)
        canvas.create_rectangle(x+d*25,y+d*6,x+d*26,y+d*7,fill=color)
        canvas.create_rectangle(x+d*26,y+d*6,x+d*27,y+d*7,fill=color)
        canvas.create_rectangle(x+d*27,y+d*6,x+d*28,y+d*7,fill=color)
        canvas.create_rectangle(x+d*28,y+d*6,x+d*29,y+d*7,fill=color)
        #pismeno L
        color = f'#{random.randrange(256**3):06x}'
        canvas.create_rectangle(x+d*30,y,x+d*31,y+d,fill=color)
        canvas.create_rectangle(x+d*30,y+d,x+d*31,y+2*d,fill=color)
        canvas.create_rectangle(x+d*30,y+2*d,x+d*31,y+d*3,fill=color)
        canvas.create_rectangle(x+d*30,y+d*3,x+d*31,y+d*4,fill=color)
        canvas.create_rectangle(x+d*30,y+d*4,x+d*31,y+d*5,fill=color)
        canvas.create_rectangle(x+d*30,y+d*5,x+d*31,y+d*6,fill=color)
        canvas.create_rectangle(x+d*30,y+d*6,x+d*31,y+d*7,fill=color)
        canvas.create_rectangle(x+d*31,y+d*6,x+d*32,y+d*7,fill=color)
        canvas.create_rectangle(x+d*32,y+d*6,x+d*33,y+d*7,fill=color)
        canvas.create_rectangle(x+d*33,y+d*6,x+d*34,y+d*7,fill=color)
        canvas.create_rectangle(x+d*34,y+d*6,x+d*35,y+d*7,fill=color)
        canvas.update()
        x = x+d*36
    y = y+d*8
    x = xx
canvas.mainloop()