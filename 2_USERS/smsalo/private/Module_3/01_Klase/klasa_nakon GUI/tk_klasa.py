from tkinter import *

root=Tk()
root.geometry('600x400')

class Root():
    def __init__(self, master):
        myFrame=Frame(master)
        myFrame.pack()

        self.myButton=Button(master, text='Klikni me!', command=self.klikni_me)
        self.myButton.pack(padx=20)

    def klikni_me(self):
        print('Gumb stisnut')


r=Root(root)

root.mainloop()