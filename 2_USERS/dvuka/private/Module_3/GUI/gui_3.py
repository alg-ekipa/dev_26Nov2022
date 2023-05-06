from tkinter import *

root=Tk()
root.geometry('600x400')

img_py=PhotoImage(file='C:/Users/danij/Downloads/dev_26Nov2022/1_ALG/_vzbo_/m3_07_GUI/python.gif')

gumbek1=Button(root, text='gumbek')

gumbek2=Button(root, text='klikni me') #TO DO: command!

gumbek3=Button(root, text='gumbek sa slikom',
              image=img_py, 
              compound=RIGHT, 
              relief=SUNKEN,
              state=NORMAL
               
)

gumbek1.pack(pady=10)
gumbek2.pack(pady=10)

gumbek3.pack()






root.mainloop()