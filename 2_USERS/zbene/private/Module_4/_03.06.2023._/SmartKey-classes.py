from logging import root
from tkinter import *
from tkinter import messagebox
import sqlite3 as db

class PočetniPozvoniOtključaj:
    def __init__ (self, root):
        self.root = root
        self.frameKey = LabelFrame (self.root, text = 'Key', padx = 400, pady = 20)
        self.frameKey.grid (row=0, column=0)

        self.pozvoniBtn = Button (self.frameKey, text = 'Zvono', padx = 10, pady = 10)
        self.pozvoniBtn.grid (row = 0, column = 1)

        self.otključajBtn = Button (self.frameKey, text = 'Otključaj', padx = 10, pady = 10)
        self.otključajBtn.grid (row = 0, column = 2)

def pozvoni (self):
    messagebox.showinfo(('Upozorenje!', 'Pozvonili ste i čekajte!'))

def otključaj (self):
    pass

class PINPanel:
    '''sve što stoji na pin panelu: LabelFrame PIN Panel, tipkovnica, status i poruke'''

class AdminPanel:
    '''LabelFrame Upravljanje, natpisi IME, PREZIME, PIN, AKTIVAN, polja za unos (ista ta 4)'''

#otvaranje konekcije prema bazi, kreiranje tablice u koju ćemo spremiti unose
baza = db.connect ('SmartKeyUsers.db')
baza.execute ('CREATE TABLE IF NOT EXISTS Korisnici (ime TEXT NOT NULL, prezime TEXT, pun NUMBER)')
cursor = baza.cursor()
baza.commit()

def new_user():
    baza = db.connect ('SmartKeyUsers.db')
    ime = ime_var.get()
    prezime = prezime_var.get()
    pin = pin_var.get()

    baza.execute ('INSERT INTO Korisnici (ime, prezime, pin) VALUES(?,?,?)', (ime, prezime, pin))

root = Tk()

ime_var = StringVar()
prezime_var = StringVar()
pin_var = StringVar()

PočetniPozvoniOtključaj(root)

root.mainloop()