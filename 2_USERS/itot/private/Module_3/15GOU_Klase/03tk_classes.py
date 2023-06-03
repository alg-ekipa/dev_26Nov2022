from tkinter import *


root = Tk()

class Root():
    def __init__(self,master):
        myFrame = Frame(master)
        myFrame.pack()

        #dodavanje gumba
        self.myButton = Button(master, text="Click me!")
        self.myButton(padx=20)
        
    def click_me(self):
                      

                      #TODO fali dio