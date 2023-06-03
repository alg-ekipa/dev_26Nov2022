from tkinter import *
from tkinter import messagebox
import sqlite3 as db

class PocetniPozvoniOtkljucaj:
    def __init__(self, root):
        self.root=root
        self.frameKey=LabelFrame(self.root, text='Key', padx=400, pady=20)
        self.frameKey.grid(row=0, column=0)

        self.pozvoniBtn=Button(self.frameKey, text='Zvono', padx=10, pady=10, command=self.pozvoni)
        self.pozvoniBtn.grid(row=0, column=1)

        self.otkljucajBtn=Button(self.frameKey, text='Otključaj', padx=10, pady=10)
        self.otkljucajBtn.grid(row=0, column=2)
    
    def pozvoni(self):
        messagebox.showinfo('Upozorenje', 'Pozvonili ste!')

    def otkljucaj(self):
        pass

#class PINPanel:

'''
Sve što stoji na pin panelu:
- LabelFrame, tipkovnica, ststus i poruke'''

#class AdminPanel:
'''
label frame upravljanje, natpisi Ime, Prezime, Pin, .....treeview

'''

#otvaranje konekcije prema bazi

baza=db.connect('SmartKeyUser.db')
baza.execute


root=Tk()

PocetniPozvoniOtkljucaj(root)



root.mainloop()