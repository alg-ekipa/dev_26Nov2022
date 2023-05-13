from tkinter import *
import sqlite3

baza=sqlite3.connect('Korisnici.db')
stvori_query='CREATE TABLE IF NOT EXISTS Stanari(ime TEXT, prezime TEXT)'
baza.execute(stvori_query)
cursor=baza.cursor()


root=Tk()
root.title('Algebra-Unos u bazu')
root.geometry('600x400')

#varijable
ime_var=StringVar()
prezime_var=StringVar()

def dodaj_u_bazu():
    ime=ime_var.get()
    prezime=prezime_var.get()

    dodaj_query= f"INSERT INTO Stanari (ime, prezime) VALUES ('{ime}', '{prezime}')"

    baza.execute(dodaj_query)
    baza.commit()

def obrisi_tablicu():
    brisi_query='DELETE FROM Stanari'
    baza.execute(brisi_query)
    baza.commit()

#GUI
ime=Label(root, text='IME: ')
ime.grid(row=0, column=0, padx=10, pady=10)

prezime=Label(root, text='PREZIME: ')
prezime.grid(row=1, column=0, padx=10, pady=10)

entry_ime =Entry(root, textvariable=ime_var)
entry_ime.grid(row=0, column=1, padx=10, pady=10)

entry_prezime =Entry(root, textvariable=prezime_var)
entry_prezime.grid(row=1, column=1, padx=10, pady=10)

gumb1 = Button(root, text='Dodaj u bazu', command=dodaj_u_bazu)
gumb2 = Button(root, text='Obriši tablicu', command=obrisi_tablicu)   
gumb1.grid(row= 0, column=2, padx=10, pady=10)
gumb2.grid(row= 1, column=2, padx=10, pady=10)

ime=ime_var.get()
prezime=prezime_var.get()

root.mainloop()

