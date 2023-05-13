import tkinter as tk
import tkinter.ttk as ttk
import sqlite3


root = tk.Tk()


query_select_all = '''SELECT * FROM Stanari'''

database_name = 'C:/Users/hyperv/Desktop/H/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/07_GUI/Korisnici.db'

try:
    sql_conn = sqlite3.connect(database_name)
    cursor  =sql_conn.cursor()

    cursor.execute(query_select_all)
    records_all = cursor.fetchall()
    
    print(records_all)
    

except sqlite3.Error as e:
    print('Pogreška: ',e)

finally:
    if sql_conn:
        sql_conn.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')

def procitaj_podatke():
    
    for broj,redak in enumerate(records_all):
        print(broj, redak)
        tree.insert('',tk.END, iid=broj, text=redak[0],values=redak[1:])
      

stupci = ('prezime')       # već postoji prvi stupac, zato ne moramo stavljati stupac za ime i prezime

tree= ttk.Treeview(root, columns=stupci, height=10)
tree.pack(padx=5, pady=5)

tree.heading('#0',text='Ime ')
tree.heading('prezime',text='Prezime')

procitaj_podatke()


root.mainloop()