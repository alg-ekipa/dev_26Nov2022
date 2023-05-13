from tkinter import *

root = Tk()
root.geometry('600x400')

img_py = PhotoImage(file='python.gif')

gumbek1 = Button(root, text='Klikni me!')

gumbek2 = Button(root, text='NE! MENE KLIKNI!') # To Do: command!

gumbek3 = Button(root, text='Sličica ', # na ovom botunu se nalazi sličica
                image=img_py, 
                compound=RIGHT, 
                relief=SUNKEN, # ima različite opcije za izgled gumba 
                state=NORMAL
)



gumbek1.pack(pady=10)
gumbek2.pack(pady=10)

gumbek3.pack()

root.mainloop()