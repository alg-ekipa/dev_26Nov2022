from tkinter import *

class Window:
    def __init__(self,root, title, geometry, message):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)

        Label(self.root, text= message).pack()

        button1 = Button(self.root, text = "Otvori novi prozor", command=self.otvori_novi)
        button1.pack()

    def otvori_novi(self):
        root2 = Tk()
        window2 = Window(root2, "Drugi", "500x500", "Poruka2")
        root2.mainloop()

    
root1 = Tk()

window1 = Window(root1, "GUI s klasama", "400x400", "Poruka")

root1.mainloop()
