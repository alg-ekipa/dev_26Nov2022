from tkinter import *

root = Tk()

root.geometry("600x400")

img_py = PhotoImage(file="C:/Users/JulijanaS/Desktop/VisualStudioCode/dev_26Nov2022-1/2_USERS/jsliv/private/Module_3/GUI/python.gif")

gumb1 = Button(root, text = "Button")
gumb2 = Button(root, text="Klikni Button2")
gumb3 = Button(root, text="Prikazi sliku",
                image=img_py,
                command=LEFT,
                relief=GROOVE,  # ako stavimo RAISED tada će gumb biti ispupčen
                state=DISABLED   #ako stavimo umjesto DISABLED NORMAL onda će se gumb moći stisnuti
                )

gumb1.pack(pady=10)
gumb2.pack(pady=10)

gumb3.pack()

root.mainloop()