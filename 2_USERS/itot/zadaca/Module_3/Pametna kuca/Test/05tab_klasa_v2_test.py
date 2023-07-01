

import tkinter as tk
from tkinter import *
from tkinter import ttk # ttk module which contains the Notebook widget

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        
        self.title('Pametna kuca') #Naslov peret windowa
        tabControl = ttk.Notebook(self)  #Creating Tab Control
        self.dnevni_boravak = ttk.Frame(tabControl) #Creating the tabs
        self.hodnik = ttk.Frame(tabControl)
        velicina_prozora='400x400'
        self.geometry(velicina_prozora)

        tabControl.add(self.dnevni_boravak, text='Dnevni Boravak')#Adding the tab
        tabControl.add(self.hodnik, text='Hodnik')
        tabControl.grid(column=0, row=0)

        self.dodavanje_gumba()
        self.dodavanje_gumba2(self.dnevni_boravak, "Click Me", 0, 2, self.test_gumb, 'white','green')
    
    #test ispis za provjeru
    def test_gumb(self):
        print('Gumb je stisnut, radi!')

    #dodavanje gumba verzija 2
    def dodavanje_gumba2(self, Frame, txt, b_row, b_col, b_command, c_fg,c_bg):

        novi_gumb = Button(Frame, text=txt, height=2, width=10,
                     font=('Segoe UI',14),
                     fg=c_fg,
                     bg=c_bg,
                     command=b_command) # LAMBDA - da prenese u fukciju
        novi_gumb.grid(row=b_row, column=b_col)
        return novi_gumb
    
    #dodavanje gumba verzija 1
    def dodavanje_gumba(self):
        btn1 = Button(self.hodnik, text="Submit",command=self.test_gumb())
        btn1.grid(row=1, column=0)
 
'''
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

btn1 = Gumb(hodnik, "Click Me", 0, 2, test_gumb, 'green')

gumb_svijetlo_db = Button(dnevni_boravak, text='Svijetlo', height=2, width=10,
                     font=('Segoe UI',14),
                     fg='white',
                     bg='grey',
                     command=test_gumb) # LAMBDA - da prenese u fukciju
gumb_svijetlo_db.grid(row=1, column=0)

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
'''

root = Root()
root.mainloop()
