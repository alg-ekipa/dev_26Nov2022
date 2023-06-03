from tkinter import *
from typing import Any

root = Tk()

root.geometry("600x400")

class Root():
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.myButton = Button(master, text = "Click me")
        self.myButton.pack(padx=20)
    
    def click_me(self):
        print("Button clicked")

r = Root(root)

root.mainloop()