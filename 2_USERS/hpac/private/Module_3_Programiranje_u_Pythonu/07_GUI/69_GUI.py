from tkinter import *

root = Tk()
root.geometry('600x400')

img_py = PhotoImage(file='C:/Users/hyperv/Desktop/ph/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/07_GUI/python.gif')

gumbek1 = Button(root, text='Gumbek mali')

gumbek2 = Button(root, text='Gumbek 2')     #TO DO: naredba!

gumbek3 = Button(root, text='Gumbek sa sličkom',
                 image = img_py,
                 compound=RIGHT,
                 relief=RAISED,
                 state=NORMAL,
                 
                 )

gumbek1.pack(pady=10)
gumbek2.pack(pady=10)
gumbek3.pack(pady=10)

root.mainloop()