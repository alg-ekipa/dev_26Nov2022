from tkinter import *

class Prozor:
    def __init__(self, root, title, geometry, message):
        self.root=root
        self.root.title(title)
        self.root.geometry(geometry)

        Label(self.root, text=message).pack()

        button1=Button(self.root, text="Otvori novi prozor!", command=self.otvori_novi)
        button1.pack()
    
    def otvori_novi(self):
        root2=Tk()
        prozor2=Prozor(root2,"Drugi", "500x500", "Poruka 2" )
        root2.mainloop()


root1=Tk()

prozor1=Prozor(root1, "GUI s klasama", "600x400", "Poruka")


root1.mainloop()
