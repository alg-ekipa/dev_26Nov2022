import tkinter as tk
import tkinter.ttk as ttk
import sqlite3

root=tk.Tk()
root.title('Adresar')

query_select = '''SELECT * FROM Stanari'''
database_name = 'Korisnici.db'

try:
    sql_connect = sqlite3.connect(database_name)
    cursor = sql_connect.cursor()

    cursor.execute(query_select)
    record_all = cursor.fetchall()
        
    cursor.close()

except sqlite3.Error as e:
    print('Pogreška: ', e)

finally:
    if sql_connect:
        sql_connect.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')

def procitaj_podatke():
    for broj, redak in enumerate(record_all):
        tree.insert('', tk.END, iid=broj, text=redak[0], values=redak[1:])      

stupci=('prezime')

tree=ttk.Treeview(root, columns=stupci, height=10)
tree.pack(padx=5, pady=5)

tree.heading('#0', text='Ime' )
tree.heading('prezime', text='Prezime')

procitaj_podatke()

root.mainloop()