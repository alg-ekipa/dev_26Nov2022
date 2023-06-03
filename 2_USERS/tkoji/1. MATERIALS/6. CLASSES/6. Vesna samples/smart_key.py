from tkinter import *
from tkinter import messagebox
import sqlite3 as db

root = Tk()

class PozvoniOtkljucaj:
    def __init__(self, root):
        self.root = root
        self.framKey = LabelFrame(self.root, text="Key", padx=400, pady=20)
        self.framKey.grid(row=0, column=0)
        
        self.pozvoni = Button(self.framKey, text="Zvono", padx=10, pady=10,command= self.pozvoni)
        self.pozvoni.grid(row=0, column=0)
        
        self.otkljucaj = Button(self.framKey, text="Otkljucaj", padx=10, pady=10)
        self.otkljucaj.grid(row=0, column=1)
        
    def pozvoni(self):
        messagebox.showinfo("Upozorenje!", "De se kupas?")


class PINPanel:

    pass

class AdminPanel:
    ''' label frame, natpisi gumbiju - ime prezime, pin, is user active, polja za unos, Treeview'''
    
    
# tvaranje konekcie prema bazi, kreiranje tablice koju cemo spremati unso
baza = db.connect("tom_users.db")
baza.execute('CREATE TABLE IF NOF EXIST users (IME, ')
cursor = baza.cursor()
baza.commit()

def new_user():
    baza = db.connect("tom_users.db")
    -
PozvoniOtkljucaj(root)
root.mainloop()
        
    
    