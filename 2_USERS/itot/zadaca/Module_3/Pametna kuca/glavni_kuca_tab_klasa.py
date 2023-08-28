'''
TODO:

'''


import tkinter as tk
from tkinter import *
from tkinter import ttk # ttk module which contains the Notebook widget



class Gumb(Button):
    def __init__(self, Frame ,text, height, width, row, col, command, color_fg=None, color_bg=None, **kwargs):
        self.Frame = Frame
        self.text = text
        self.height = height
        self.width = width
        self.row = row
        self.column = col
        self.command = command
        self.color_fg = color_fg
        self.color_bg = color_bg
        super().__init__()
        self.Frame= self.Frame
        self['height'] = self.height
        self['width'] = self.width
        self['bg'] = self.color_bg
        self['fg'] = self.color_fg
        self['text'] = self.text
        self['command'] = self.command
        #self.grid(row=self.row, column=self.column)
        self.pack(expand=1, fill="both")





def test_gumb():
    print('Gumb je stisnut, radi!')

velicina_prozora='400x400'
root = tk.Tk() # parent window
root.title('Pametna kuca') #Naslov peret windowa
root.geometry(velicina_prozora)
root.eval('tk::PlaceWindow . center') #centriranje ekrana TODO: doraditi poziciju
tabControl = ttk.Notebook(root)  #Creating Tab Control
dnevni_boravak = ttk.Frame(tabControl) #Creating the tabs
hodnik = ttk.Frame(tabControl)
tabControl.add(dnevni_boravak, text='Dnevni Boravak')#Adding the tab
tabControl.add(hodnik, text='Hodnik')
tabControl.pack(expand=1, fill="both") #Packing the tab control to make the tabs visible

#tabControl.grid(row=0, column=0)


#Otvaranje novoga prozora
def otvori_novi(naziv_prozora):
    root2 = Tk()
    window2 = (root2, "Drugi", "500x500", "Poruka 2")
    root2.title(naziv_prozora)
    root2.geometry(velicina_prozora)
    root2.eval(f'tk::PlaceWindow {str(root2)} center')

    back_gumb = Button(root2, text='Back', height=2, width=10,
                     font=('Segoe UI',14),
                     fg='white',
                     bg='grey',
                     command=root2.destroy) # gašenje prozora
    back_gumb.grid(row=0, column=0)

    root2.mainloop()


# promjena boje gumba i slova pod uvjetom boje
def promjena_boje(naziv_gumba):
    if naziv_gumba['bg'] == 'grey':
        naziv_gumba.configure(fg='black',bg ="yellow") # promjena boje gumba i slova
    else:
        naziv_gumba.configure(fg='white',bg ="grey") 


#dodavanje gumbi     root pozicija                visina    dužina

gumb_svijetlo_db = Gumb(dnevni_boravak,"Svijetlo DB", 2, 10, 1, 0,lambda:promjena_boje(gumb_svijetlo_db), 'white', 'grey')
#gumb_TV_db = Gumb(dnevni_boravak,"TV", 2, 10, 2, 0,lambda:otvori_novi(gumb_TV_db['text']), 'white', 'green')
#gumb_radio_db = Gumb(dnevni_boravak,"Radio", 2, 10, 2, 1,lambda:otvori_novi(gumb_TV_db['text']), 'white', 'blue')

gumb_svijetlo_hod = Gumb(hodnik,"Svijetlo H", 2, 10, 1, 2,lambda:promjena_boje(gumb_svijetlo_hod ), 'white', 'grey')




'''
gumb_svijetlo_db = Button(dnevni_boravak, text='Svijetlo', height=2, width=10,
                     font=('Segoe UI',14),
                     fg='white',
                     bg='grey',
                     command=lambda:promjena_boje(gumb_svijetlo_db)) # LAMBDA - da prenese u fukciju
gumb_svijetlo_db.grid(row=1, column=0)

gumb_TV_db = Button(dnevni_boravak, text='TV', height=2, width=10,
                     font=('Segoe UI',14),
                     fg='white',
                     bg='green',
                     command=lambda:otvori_novi(gumb_TV_db['text']))
gumb_TV_db.grid(row=2, column=0)
gumb_radio_db = Button(dnevni_boravak, text='Radio', height=2, width=10,
                     font=('Segoe UI',14),
                     fg='white',
                     bg='blue',
                     command=lambda:otvori_novi(gumb_radio_db['text']))
gumb_radio_db.grid(row=2, column=1)

gumb_svijetlo_hod = Button(hodnik, text='Svijetlo', height=2, width=10,
                     font=('Segoe UI',14),
                     fg='white',
                     bg='grey',
                     command=lambda:promjena_boje(gumb_svijetlo_hod))
gumb_svijetlo_hod.grid(row=0, column=0)
'''
root.mainloop()