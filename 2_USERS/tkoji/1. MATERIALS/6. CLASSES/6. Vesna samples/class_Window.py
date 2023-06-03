from tkinter import *
from webbrowser import open_new

root = Tk()

class Window:
    def __init__(self, root, title, geometry, message):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
        
        Label(self.root, text=message).pack()
        
        button1 = Button(self.root, text="Open new",command=self.open_new)
        button1.pack()
        
    def open_new(self):
        root1 = Tk()
        window2 = Window(root1, "GUI2", "400x600","Ovoooo")
        root1.mainloop()

window1=Window(root, "GUI Klasa", "400x500", "Hello world")



root.mainloop()

        
        
        

