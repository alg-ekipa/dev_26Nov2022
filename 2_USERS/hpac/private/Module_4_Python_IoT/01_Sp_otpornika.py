from tkinter import Label
from tkinter import *


root = Tk()

uputa = Label(root, text='Unesite iznose otpornika', font=('Segore',14), fg='blue')
uputa.grid(row=0,column=0, columnspan=2)

oznakaR1 = Label(root, text='R1').grid(row=1,column=0)
oznakaR2 = Label(root, text='R2').grid(row=2,column=0)

unosR1 = Entry(root)
unosR1.grid(row=1,column=1)

unosR2 = Entry(root)
unosR2.grid(row=2,column=1)

gumb_serija = Button(root, text='Serijski spoj', height=2, width=10,
                    font=('Segore',14), 
                    fg='white',
                    bg='blue')
gumb_serija.grid(row=3,column=0)

gumb_paralela = Button(root, text='Serijski spoj', height=2, width=10,
                    font=('Segore',14), 
                    fg='white',
                    bg='green')
gumb_paralela.grid(row=3,column=1)

frame_serija = Frame(root, height=500, width=200,bg='blue')
frame_serija.grid(row=4,column=0)

frame_paralela = Frame(root, height=500, width=200,bg='green')
frame_paralela.grid(row=4,column=1)


root.mainloop()