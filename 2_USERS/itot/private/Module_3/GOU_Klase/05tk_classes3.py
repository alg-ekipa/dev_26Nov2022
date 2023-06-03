from tkinter import *
from tkinter import messagebox
import sqlite3 as db

class PocetniPozvoniOtkljucaj:
    def __init__(self,root):
        self.root = root
        self.frameKey = LabelFrame(self.root, text='Key', padx=400, pady= 20)
        self.frameKey.grid(raw=0, column=0)

        self.pozvoniBtnt = Button(self.frameKey, text='Zvono', padx=10, pady= 10)
        self.pozvoniBtnt.grid(raw=0, column=1)

        self.otkljucajBtn = Button(self.frameKey, tekst="Otkljucaj", padx=10, pady= 10)
        self.pozvoniBtnt.grid(raw=0, column=2)  
    
    def pozvoni(self):
        messagebox.showinfo(('Upozorenje', 'Pozvonili ste i čekajte!'))
    
    def otkljucaj(self):
        PINPanel()

class PINPanel:
    '''Sve sto sastoji pin panel: LabelFrame, ''' # Fali

class AdminPanel:
    '''LabelGrame Upravljanja, natpisi ''' # Fali

baza = db.connect('SmartUsers.db')
baza.execute('CREATE LABEL IF NOT EXISTS Korisnici ( ime TEXT NOT NULL, prezime, TEXT, pin NUMBER)')
coursor = baza.coursor()
baza.commit()



def new_user():
    baza = db.connect('SmartKeyUsers.db')
    ime=ime_var.get()
    prezime=prezime_var.get()
    pin=pin_var.get()

    baza.execute('INSERT INTO Korisnici(ime, prezime, pin) VALUES (?,?,?)', (ime, prezime, pin)  )

root = Tk()


root.mainloop()