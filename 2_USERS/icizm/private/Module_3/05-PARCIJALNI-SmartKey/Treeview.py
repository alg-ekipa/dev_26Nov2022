from tkinter import *
import sqlite3

baza = sqlite3.connect("Stanari.db") # Ako ne postoji, kreirati će ju, pazi da si u pathu dobrom
stvori_query = "CREATE TABLE IF NOT EXISTS Stanari (Ime TEXT, Prezime TEXT, PIN TEXT)" 
baza.execute(stvori_query)
cursor = baza.cursor()

root = Tk()

# VARIJABLE 

ime_var = StringVar()
prezime_var = StringVar()
PIN_var = StringVar()

# FUNKCIJE

def dodaj(): 
    ime = ime_var.get()
    prezime = prezime_var.get()
    PIN = PIN_var.get()
    
    dodaj_query = f"INSERT INTO Stanari (Ime, Prezime, PIN) VALUES ('{ime}','{prezime}', {PIN})"

    baza.execute(dodaj_query)
    baza.commit()

def obrisi_tablicu(): 
    brisi_query = 'DELETE FROM Stanari'
    baza.execute(brisi_query)
    baza.commit()

    #print(f'Ime: {ime}, {prezime}')


# SMJEŠTENI SU NA GUI

label_ime = Label(root, text='Ime : ')
label_ime.grid(row=0, column=0, padx=5, pady=5)

entry_ime = Entry(root, textvariable=ime_var, font=('calibre', 10, 'normal')) # textvariable sa entrijem povezujemo kako bi mogli manipulirati unosom
entry_ime.grid(row=0, column=1)

label_prezime = Label(root, text='Prezime : ')
label_prezime.grid(row=1, column=0, padx=5, pady=5)

entry_prezime = Entry(root, textvariable=prezime_var, font=('calibre', 10, 'normal'))
entry_prezime.grid(row=1, column=1)

label_PIN = Label(root, text='PIN : ')
label_PIN.grid(row=2, column=0, padx=5, pady=5)

entry_PIN = Entry(root, textvariable=PIN_var, font=('calibre', 10, 'normal'))
entry_PIN.grid(row=2, column=1)

dodaj_button = Button(root, text='Dodaj u bazu', command=dodaj) 
dodaj_button.grid(row=0, column=3, padx=5, pady=5)

obrisi_button = Button(root, text='Obriši tablicu', command=obrisi_tablicu) 
obrisi_button.grid(row=1, column=3, padx=5, pady=5)

query_select_all_data = ''' SELECT * FROM Stanari'''

database_name = 'Stanari.db'

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

root.mainloop()