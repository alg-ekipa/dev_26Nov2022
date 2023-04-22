from tkinter import *

root = Tk()
root.geometry('600x600')
slika=PhotoImage(file='python.gif')

gumbek1 = Button(root, text='gumbek')

gumbek2 = Button(root, text='klikni me!', bg='gray')       #to do: command!

gumbek3 = Button(root, text='gumbek sa slikom',
                 image=slika,
                 compound=RIGHT,
                 relief=GROOVE,
                 state=NORMAL)

gumbek1.pack(pady=10)
gumbek2.pack(pady=10)
gumbek3.pack(pady=10)


root.mainloop()