from tkinter import *

root = Tk()
root.geometry("600x400")

class Root():
    def __init__(self, master):
        my_frame = Frame(master)
        my_frame.pack()
           
        self.mybutton = Button(master, text='Click me.', command=self.click_me)
        self.mybutton.pack()
        
    def click_me(self):
        print("Button clicked!")

r = Root(root)    

root.mainloop()