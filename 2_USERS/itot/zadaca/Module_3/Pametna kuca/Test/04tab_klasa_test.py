'''
TODO:


'''

import tkinter as tk
from tkinter import *
from tkinter import ttk # ttk module which contains the Notebook widget


root = tk.Tk() # parent window
root.title('Pametna kuca') #Naslov peret windowa
tabControl = ttk.Notebook(root)  #Creating Tab Control
dnevni_boravak = ttk.Frame(tabControl) #Creating the tabs
hodnik = ttk.Frame(tabControl)
tabControl.add(dnevni_boravak, text='Dnevni Boravak')#Adding the tab
tabControl.add(hodnik, text='Hodnik')
#tabControl.pack(expand=1, fill="both") #Packing the tab control to make the tabs visible
tabControl.grid(column=0, row=0)


class Gumb(Button):
    def __init__(self, Frame, text, row, col, command, color=None, **kwargs):
        self.Frame = Frame
        self.text = text
        self.row = row
        self.column = col
        self.command = command
        self.color = color
        super().__init__()
       
        self['bg'] = self.color
        self['text'] = self.text
        self['command'] = self.command
        self.grid(row=self.row, column=self.column)

def test_gumb():
    print('Gumb je stisnut, radi!')

'''
gumb_svijetlo_db = Button(dnevni_boravak, text='Svijetlo', height=2, width=10,
                     font=('Segoe UI',14),
                     fg='white',
                     bg='grey',
                     command=test_gumb) # LAMBDA - da prenese u fukciju
gumb_svijetlo_db.grid(row=1, column=0)
'''
btn1 = Gumb(hodnik, "Click Me", 0, 2, test_gumb, 'green')
btn2 = Gumb(hodnik, "Click Me2", 0, 1, test_gumb, 'red')


#Creating Label widget as a child of the parent window (root)
ttk.Label(dnevni_boravak, 
          text ='Welcome to \
          GeeksForGeeks').grid(column = 0, 
                               row = 0,
                               padx = 30,
                               pady = 30)  

ttk.Label(hodnik,
          text ='Lets dive into the \
          world of computers').grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)


root.mainloop()