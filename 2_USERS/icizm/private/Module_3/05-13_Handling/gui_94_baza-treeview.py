import tkinter as tk
import tkinter.ttk as ttk
import sqlite3



query_select_all_data = ''' SELECT * FROM Stanari'''


database_name = 'Korisnici.db'

try: 
    sql_conn = sqlite3.connect(database_name)
    cursor = sql_conn.cursor()
    print('Baza je uspješno kreirana!')

    cursor.execute(query_select_all_data)
    records_all = cursor.fetchall()
    print(records_all)

    cursor.close()

except sqlite3.Error as e: 
    print('Pogreška', e)

# zatvaranje konekcije prema bazi
finally: 
    if sql_conn: 
        sql_conn.close
        print('Veza prema SQL bazi je uspješno zatvorena!')

root = tk.Tk()


def procitaj_podatke(): 

    for broj, redak in enumerate(records_all): 
        print(broj, redak)
        tree.insert('', tk.END, iid=broj, text=redak[0], values=redak[1:]) 
    

stupci = ('prezime') #

tree = ttk.Treeview(root, column=stupci, height=8) 
tree.pack(padx=5, pady=5)



tree.heading('#0', text='Ime') 
tree.heading('prezime', text='Prezime')

procitaj_podatke()

root.mainloop()