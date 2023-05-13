import tkinter as tk
import sqlite3

baza = sqlite3.connect("Korisnici.db")
stvori_query = "CREATE TABLE IF NOT EXISTS Stanari (ime TEXT, prezime TEXT)"
baza.execute(stvori_query)
cursor = baza.cursor()

root = tk.Tk()
root.geometry('600x600')

# VARIJABLE
ime_var = tk.StringVar()
prezime_var = tk.StringVar()

def dodaj_u_bazu():
    ime = ime_var.get()
    prezime = prezime_var.get() 

    dodaj_query = f"INSERT INTO Stanari (ime, prezime) VALUES ('{ime}','{prezime}')"

    baza.execute(dodaj_query)
    baza.commit()

def obrisi_tablicu():
    brisi_query = 'DELETE FROM Stanari'
    baza.execute(brisi_query)
    baza.commit()

    #print(f'Ime: {ime}, Prezime: {prezime}')

# SMJEŠTANJE NA GUI

ime_label = tk.Label(root, text='Username', font=('calibre', 10, 'bold'))
ime_label.grid(row=0, column=0)

ime_entry = tk.Entry(root, textvariable=ime_var, font=('calibre', 10, 'normal') )
ime_entry.grid(row=0, column=1)

prezime_label = tk.Label(root, text='Password', font=('calibre', 10, 'bold'))
prezime_label.grid(row=1, column=0)

prezime_entry = tk.Entry(root, textvariable=prezime_var, font=('calibre', 10, 'normal'), show='*' )
prezime_entry.grid(row=1, column=1)

dodaj_button = tk.Button(root, text="Dodaj u bazu", command=dodaj_u_bazu)
dodaj_button.grid(row=0, column=2)

brisi_button = tk.Button(root, text="Obrisi tablicu", command=obrisi_tablicu)
brisi_button.grid(row=1, column=2)


root.mainloop()