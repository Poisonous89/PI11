import tkinter

canvas= tkinter.Canvas(width=800,height=600)
canvas.pack()

#pismeno S
canvas.create_arc(50,50,100,100, start= 0, extent= x+d*13,style="arc",width= 2,outline='cyan')
canvas.create_arc(100,100,50,150, start= 90, extent= -270,style="arc",width= 2,outline='cyan')

#pismeno A
canvas.create_line(120,150,150,50,width=3,fill='blue')
canvas.create_line(150,50,180,150,width=3,fill='blue')
canvas.create_line(135,100,165,100,width=3,fill='blue')

#pismeno M
canvas.create_line(200,150,200,50,230,80,260,50,260,150,width=4,fill='red')

#pismeno U
canvas.create_arc(280,150,330,110, start= 0, extent= -180,style="arc",width=5,outline='green')
canvas.create_line(280,50,280,130,width=5,fill='green')
canvas.create_line(330,50,330,130,width=5,fill='green')

#pismeno E
canvas.create_line(350,50,350,150,395,150,width=6,fill='pink')
canvas.create_line(350,50,395,50,width=6,fill='pink')
canvas.create_line(350,100,395,100,width=6,fill='pink')

#pismeno L
canvas.create_line(415,50,415,150,460,150,width=7,fill='yellow')

#pismeno S + mekcen
canvas.create_arc(50,200,100,y+d*12, start= 0, extent= 270,style="arc",width=8,outline='magenta')
canvas.create_arc(100,y+d*12,50,300, start= 90, extent= -270,style="arc",width=8,outline='magenta')
canvas.create_line(55,y+d*8,75,190,95,y+d*8,width=8,fill='magenta')

#pismeno K
canvas.create_line(120,200,120,300,width=9,fill='turquoise')
canvas.create_line(120,y+d*12,165,200,width=9,fill='turquoise')
canvas.create_line(120,y+d*12,165,300,width=9,fill='turquoise')

#pismeno U
canvas.create_arc(185,300,235,260, start= 0,extent= -180,style="arc",width=10,outline='orange')
canvas.create_line(185,200,185,280,width=10,fill='orange')
canvas.create_line(235,200,235,280,width=10,fill='orange')

#pismeno T
canvas.create_line(255,200,305,200,width=11,fill='purple')
canvas.create_line(280,200,280,300,width=11,fill='purple')

#pismeno A
canvas.create_line(320,300,350,200,width=15,fill='khaki')
canvas.create_line(350,200,380,300,width=15,fill='khaki')
canvas.create_line(335,y+d*12,365,y+d*12,width=15,fill='khaki')

canvas.mainloop()