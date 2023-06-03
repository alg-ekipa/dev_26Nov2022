from tkinter import *

root=Tk()

class Root():
    def __init__(self, master):
        myFrame=Frame(master)
        myFrame.pack()

        self.myButton=Button(master, text='Click me!', command=self.click_me)
        self.myButton.pack(padx=20)

    def click_me(self):
        print("Button clicked")

r=Root(root)

root.mainloop()