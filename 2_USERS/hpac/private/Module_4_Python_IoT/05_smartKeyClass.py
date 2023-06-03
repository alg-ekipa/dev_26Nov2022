from logging import root
from tkinter import *
from tkinter import messagebox
import sqlite3 as db

class PocetniPozvoniOtkljucaj:
    def __init__(self,root):
        self.root = root
        self.frameKey = LabelFrame(self.root, text='Key', padx=400, pady=20)
        self.frameKey.grid(row=0, column=0)

        self.pozvoniBtn = Button(self.frameKey, text='Zvono', padx=10, pady=10)
        self.pozvoniBtn.grid(row=0,column=0)

        self.otkljucajBtn = Button(self.frameKey, text='Otključaj', padx=10, pady=10)
        self.otkljucajBtn.grid(row=0,column=1)

    def pozvoni (self):
        messagebox.showinfo('Upozorenje', 'Pozvonili ste i čekajte')
    
    def otključaj(self):
        pass

class PINPanel:
    '''Sve što stoji na PIN panelu: LabelFrame PIN Panel, tipkovnica, status i poruke'''
    pass

class AdminPanel:
    '''Sve što stoji na Admin panelu: LabelFrame Upravljanje, natpisi, IME, PREZIME, PIN, AKTIVAN, polja za unos (ista ta 4),
    gumbe za spremanje, dodavanje, brisanje itd... '''
    pass

# Otvaranje konekcije prema bazi, kreiranje tablice u koju ćemo spremati unos

baza = db.connect('SmartKeyUsers.db')
baza.execute('CREATE TABLE IF NOT EXISTS Korisnici (ime TEXT NOT NULL, prezime TEXT, pin NUMBER)')
cursor = baza.cursor()
baza.commit()

def new_user():
    baza = db.connect('SmartKeyUsers.db')
    ime = ime_var.get()
    prezime = prezime_var.get()
    pin = pin_var.get()

    baza.execute('INSERT INTO  Korisnici(ime, prezime, pin) VALUES (?, ?, ?)', (ime, prezime, pin))

root = Tk()

ime_var = StringVar()
prezime_var = StringVar()
pin_var = StringVar()

PocetniPozvoniOtkljucaj(root)

root.mainloop()