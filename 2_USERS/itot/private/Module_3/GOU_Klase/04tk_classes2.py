# TODO Ne radi, provjeriti


from tkinter import *

class Window:
    def __init__(self,root, title, geomertry, message):
        self.root = root
        self.root.title(title)
        self.root.geomertry(geomertry)
        

        Label(self.root, text=message).pack

        button1 = Button(self.root, text="Otvorni novi prozor", command=self.otvori_novi)
        button1.pack()

    def otvori_novi(self):
        root2 = Tk()
        window2 = Window(root2, "Drugi", "500x500", "Poruka 2")
        root2.mainloop()



root = Tk()

Window1 = Window(root, "GUI s klasama", "400x400", "Puruka!")


root.mainloop()