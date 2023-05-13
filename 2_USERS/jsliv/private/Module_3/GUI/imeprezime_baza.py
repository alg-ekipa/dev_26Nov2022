from tkinter import *
import sqlite3

baza = sqlite3.connect("Korisnici.db")
stvori_query = "CREATE TABLE IF NOT EXISTS Stanari (Ime TEXT, Prezime TEXT)"
baza.execute(stvori_query)
cursor = baza.cursor()


root = Tk()
root.title("Baza imena")
root.geometry("400x400")

def dodaj_u_bazu():
    ime = ime_var.get()
    prezime = prezime_var.get()

    dodaj_query = f"INSERT INTO Stanari (Ime, Prezime) VALUES ('{ime}','{prezime}')"

    baza.execute(dodaj_query)
    baza.commit()

def obrisi_tablicu():
    brisi_query = "DELETE FROM Stanari"
    baza.execute(brisi_query)
    baza.commit()



#Varijable
ime_var = StringVar()
prezime_var = StringVar()


#Smještanje elemenata na GUI

ime = Label(root, text="Ime:")
ime.grid(row = 0, column=0, padx=5, pady=5)

ime_entry = Entry(root, textvariable=ime_var)
ime_entry.grid(row=0, column=1)

prezime = Label(root, text="Prezime: ")
prezime.grid(row = 1, column=0, padx=5, pady=5)

prezime_entry = Entry(root, textvariable=prezime_var)
prezime_entry.grid(row=1, column=1, padx=5, pady=5)

button_dodaj = Button(root, text="Dodaj u bazu", command= dodaj_u_bazu)
button_dodaj.grid(row=0, column=4, padx=40, pady=10,)

button_obrisi = Button(root, text="Obrisi tablicu", command = obrisi_tablicu,  bg="#FF1493")
button_obrisi.grid(row=1, column=4, padx=40,pady=5)


root.mainloop()