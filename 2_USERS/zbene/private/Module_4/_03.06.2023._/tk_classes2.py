from tkinter import *

class Window:
    def __init__ (self, root, title, geometry, message):
        self.root = root
        self.root.title (title)
        self.root.geometry(geometry)

        Label(self.root, text=message).pack()

root = Tk()

window1 = Window (root, 'GUI s klasama', '400x400', 'Poruka!')

root.mainloop()