import tkinter as tk
import sqlite3

baza = sqlite3.connect("Korisnici.db") # Ako ne postoji, kreirati će ju, pazi da si u pathu dobrom
stvori_query = "CREATE TABLE IF NOT EXISTS Stanari (Ime TEXT, Prezime TEXT)" 
baza.execute(stvori_query)
cursor = baza.cursor()

root = tk.Tk()
root.title('Algebra - PyDev: Unos u bazu')
root.geometry('600x400')

# VARIJABLE 

ime_var = tk.StringVar()
prezime_var = tk. StringVar()

# FUNKCIJE

def dodaj(): 
    ime = ime_var.get()
    prezime = prezime_var.get()
    
    dodaj_query = f"INSERT INTO Stanari (Ime, Prezime) VALUES ('{ime}','{prezime}')"

    baza.execute(dodaj_query)
    baza.commit()

def obrisi_tablicu(): 
    brisi_query = 'DELETE FROM Stanari'
    baza.execute(brisi_query)
    baza.commit()

    #print(f'Ime: {ime}, {prezime}')


# SMJEŠTENI SU NA GUI

label_ime = tk.Label(root, text='Ime : ')
label_ime.grid(row=0, column=0, padx=5, pady=5)

entry_ime = tk.Entry(root, textvariable=ime_var, font=('calibre', 10, 'normal')) # textvariable sa entrijem povezujemo kako bi mogli manipulirati unosom
entry_ime.grid(row=0, column=1)

label_prezime = tk.Label(root, text='Prezime : ')
label_prezime.grid(row=1, column=0, padx=5, pady=5)

entry_prezime = tk.Entry(root, textvariable=prezime_var, font=('calibre', 10, 'normal'))
entry_prezime.grid(row=1, column=1)

dodaj_button = tk.Button(root, text='Dodaj u bazu', command=dodaj) 
dodaj_button.grid(row=0, column=3, padx=5, pady=5)

obrisi_button = tk.Button(root, text='Obriši tablicu', command=obrisi_tablicu) 
obrisi_button.grid(row=1, column=3, padx=5, pady=5)


root.mainloop()