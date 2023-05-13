import sqlite3
import tkinter as tk
import tkinter.ttk as ttk

#ČITANJE I DOHVAT PODATAKA IZ TABLICE

query_select_table = '''SELECT * FROM stanari'''

database_name='C:/dokumenti/algebra/dev_26Nov2022-1/Korisnici.db'

try:
    sqliteConnection = sqlite3.connect(database_name)
    


root = tk.Tk()

def pročitaj_podatke():
    datoteka = open('C:/dokumenti/algebra/dev_26Nov2022-1/Korisnici.db', 'r')

    for broj, redak in enumerate (datoteka):
        redak = redak.rstrip().split(',')
        tree.insert('', tk.END, iid = broj, text = redak[0], values=redak[1:])
    
stupci = ('ime', 'prezime')

tree = ttk.Treeview (root, columns = stupci, height = 10)
tree.pack(padx=5, pady=5)

tree.heading('#0', text='Ime i prezime')

pročitaj_podatke()

root.mainloop()