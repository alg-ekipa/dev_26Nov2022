import sqlite3
import tkinter as tk
import tkinter.ttk as ttk

#ČITANJE I DOHVAT PODATAKA IZ TABLICE

query_select_table = '''SELECT * FROM stanari'''

database_name='C:/dokumenti/algebra/dev_26Nov2022-1/Korisnici.db'

try:
    sqliteConnection = sqlite3.connect(database_name)
    cursor = sqliteConnection.cursor()
    cursor.execute(query_select_table)
    records = cursor.fetchall()
    #print (records)
    cursor.close()

except sqlite3.Error as e:
    print (f'Dogodila se pogreška pri spajanju na SQLite: {e}')

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQL konekcija je uspješno zatvorena!')

root = tk.Tk()

def pročitaj_podatke():
    for broj, redak in enumerate (records):
        print(broj, redak)
        tree.insert('', tk.END, iid = broj, text = redak[0], values=redak[1:])
    
stupci = ('prezime')

tree = ttk.Treeview (root, columns = stupci, height = 8)
tree.pack(padx=5, pady=5)

tree.heading('#0', text='Ime')
tree.heading('prezime', text='Prezime')

pročitaj_podatke()

root.mainloop()