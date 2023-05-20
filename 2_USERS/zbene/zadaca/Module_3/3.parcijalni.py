'''PARCIJALNI ISPIT - Programiranje u Pythonu
1. Kreirajte projekt unutar foldera SmartKey te u njemu kreirajte jednu datoteku koja će predstavljati početnu datoteku za izvršavanje Vašeg programa. Ova aplikacija se može dodati u jednu veću aplikaciju tako da možete dodati i __init__.py datoteku.
2. Funkcionalnosti koje program treba imati su:
a. Prikaz korisničkog sučelja kao na shemi niže
    i. Početni ekran prikazuje samo gumbe za Pozvoniti i Otključati
b. Gumb Pozvoni otvara ekran s porukom da je zvono aktivirano te da će uskoro netko doći i otvoriti vrata
c. Gumb Otključaj otkriva srednji panel u kojem se nalazi ploča za unos PIN-a te dio na kojem se ispisuju poruke kao uspješno unesen PIN te Dobro došli Ime i prezime osobe čiji PIN je unesen.
d. Ukoliko se unese Admin PIN, onda se otvori novi ekran s pitanjem je li se želi pokrenuti administracija sustava. Ako korisnik potvrdi, otkriva se panel s listom korisnika koji imaju pravo pristupa u kuću. 
    i. Ako je neko ime selektirano, tada su polja za unos popunjena informacijama selektirane osobe. Nakon unosa izmjena potrebno je kliknuti na spremi, odustani ili izbriši da se osoba makne s popisa.
    ii. Osoba može biti aktivna ili neaktivna. Samo aktivna osoba može ući u kuću, odnosno otključati vrata
    iii. Ako se klikne na odustani i u formu se unesu podaci te klikne na gumb Spremi, onda se u sustav doda nova osoba.
e. Sve poruke se prikazuju na okviru za prikaz statusa i poruka.
f. Podaci trebaju biti pohranjeni u SQLite bazu podataka.
'''

from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import sqlite3

root = Tk()

def pozvoni():
    messagebox.showinfo(title="Pozvoni", message="Zvono aktivirano, uskoro će netko doći i otvoriti vrata.")

def upiši_broj(broj):
    brojevi = unos_pina.get()
    unos_pina.delete(0,END)
    unos_pina.insert(0,brojevi+broj)

frameTIP = LabelFrame (root, text='Dobrodošao korisniče!', padx=40, pady= 40)
frameTIP.grid(row=0, column=0)

unos_pina = Entry(frameTIP)
unos_pina.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

gumb0 = Button (frameTIP, text='0', padx=40, pady= 20, command=lambda: upiši_broj('0'))
gumb0.grid(row=3, column=1)

gumb1 = Button (frameTIP, text='1', padx=40, pady= 20, command=lambda: upiši_broj('1'))
gumb1.grid(row=0, column=0)

gumb2 = Button (frameTIP, text='2', padx=40, pady= 20, command=lambda: upiši_broj('2'))
gumb2.grid(row=0, column=1)

gumb3 = Button (frameTIP, text='3', padx=40, pady= 20, command=lambda: upiši_broj('3'))
gumb3.grid(row=0, column=2)

gumb4 = Button (frameTIP, text='4', padx=40, pady= 20, command=lambda: upiši_broj('4'))
gumb4.grid(row=1, column=0)

gumb5 = Button (frameTIP, text='5', padx=40, pady= 20, command=lambda: upiši_broj('5'))
gumb5.grid(row=1, column=1)

gumb6 = Button (frameTIP, text='6', padx=40, pady= 20, command=lambda: upiši_broj('6'))
gumb6.grid(row=1, column=2)

gumb7 = Button (frameTIP, text='7', padx=40, pady= 20, command=lambda: upiši_broj('7'))
gumb7.grid(row=2, column=0)

gumb8 = Button (frameTIP, text='8', padx=40, pady= 20, command=lambda: upiši_broj('8'))
gumb8.grid(row=2, column=1)

gumb9 = Button (frameTIP, text='9', padx=40, pady= 20, command=lambda: upiši_broj('9'))
gumb9.grid(row=2, column=2)

gumbC = Button (frameTIP, text='C', padx=40, pady= 20, command=lambda: obriši_zadnji_broj('broj'))
gumbC.grid(row=3, column=0)

gumbE = Button (frameTIP, text='E', padx=40, pady= 20, command=lambda: (''))
gumbE.grid(row=3, column=2)

def obriši_zadnji_broj(broj):
    brojevi = unos_pina.get()
    if brojevi:
        novi_brojevi = brojevi [:-1]
        unos_pina.delete(0,END)
        unos_pina.insert(0,novi_brojevi)

#def obriši_sve_brojeve(broj):      ako želimo da C briše sve brojeve
    #unos_pina.delete(0,END)

root.mainloop()