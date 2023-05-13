from tkinter import *

root = Tk()
root.geometry('600x400')

img_py = PhotoImage(file='C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/13fotodatoteke/python-logo.png')

gumbek1 = Button(root, text='Gumbek')
gumbek2 = Button(root, text='Klikni me') #TODO Command!

# command - 
gumbek3 = Button(root, text='gumbek sa slikom',
                    image=img_py,
                    compound=LEFT,
                    relief=GROOVE,
                    state=DISABLED,
                    )


gumbek1.pack(pady=10)
gumbek2.pack(pady=10)
gumbek3.pack()




root.mainloop()