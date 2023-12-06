import tkinter
import random
canvas = tkinter.Canvas(width=500,height=500)
canvas.pack()

meno = 'Janko'
priezvisko = 'Mrkva'
vek = 255

print('Volam sa', meno, priezvisko, 'a mam', vek, 'rokov')
print(f'Volam sa {meno} {priezvisko} a mam {vek:02x} rokov') #vek:02x, 02 je pocet cifier a x prevedie do 16tkovej sustavy
for i in range(20):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    farba = f'#{r:02x}{g:02x}{b:02x}'
    x = random.randint(2,480)
    y = random.randint(2,480)
    q = 20
    canvas.create_oval(x-q,y-q,x+q,y+q,fill=farba)

canvas.mainloop()