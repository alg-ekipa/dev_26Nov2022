from tkinter import *
from tkinter import messagebox
import sqlite3 as db

baza_path = 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/GOU_Klase/05SmartKeyUsers.db'

class PocetniPozvoniOtkljucaj: 
    def __init__(self, root): 
        self.root = root 
        self.frameKey = LabelFrame(self.root, text='Key', padx=400, pady=20)
        self.frameKey.grid(row=0, column=0)

        self.pozvoniBtn = Button(self.frameKey, text='Zvono', pady=10, padx=10)
        self.pozvoniBtn.grid(row=0, column=1)

        self.otkljucajBtn = Button(self.frameKey, text='Otključaj', pady=10, padx=10)
        self.otkljucajBtn.grid(row=0, column=2)

    def pozvoni(self): 
        messagebox.showinfo(('Upozorenje', 'Pozvonili ste i čekajte!'))

    def otkljucaj(self): 
        PINPanel()

# klasa u kojoj ide sve za admina
class PINPanel: 
    ''' Sve što stoji na pin panelu: tLabelFrame PIN Panel, tipkovnica, status i poruke '''

class AdminPanel: 
    '''LabelFrame Upravljanje, natpisi IME, PREZIME, PIN, AKTIVAN, polja za unos(ista ta 4) i treeview ako ima'''


# otvaranje konekcije prema bazi, kreiranje tablice u koju ćemo spremati unose 

baza = db.connect(baza_path)
baza.execute('CREATE TABLE IF NOT EXISTS Korisnici (ime TEXT NOT NULL, prezime TEXT, pin NUMBER)')
cursor = baza.cursor()
baza.commit()

def new_user(): 
    baza = db.connect(baza_path)
    ime = ime_var.get()
    prezime = prezime_var.get()
    pin = pin_var.get()

    baza.execute('INSERT INTO Korisnici(ime, prezime, pin) VALUES (?,?,?)', (ime, prezime, pin))

root = Tk()

ime_var = StringVar()
prezime_var = StringVar()
pin_var = StringVar()

PocetniPozvoniOtkljucaj(root)

root.mainloop()