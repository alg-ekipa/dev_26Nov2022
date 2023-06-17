from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import sqlite3

def otključaj():
    prozor_pina = Toplevel()
    prozor_pina.title("Unos PIN-a")
    
    unos_pina = Entry(prozor_pina)
    unos_pina.pack(padx=10, pady=10)
    
    gumb_unesi = Button(prozor_pina, text="Unesi", command=lambda: provjeri_pin(unos_pina.get()))
    gumb_unesi.pack(pady=10)

def provjeri_pin(pin):
    if pin == "1234":  # Ovdje provjerite željeni PIN
        messagebox.showinfo(title="PIN ispravan", message="PIN je ispravan. Otključavanje...")
        # Ovdje dodajte kod za otključavanje ili druge akcije
    else:
        messagebox.showwarning(title="PIN pogrešan", message="Uneseni PIN nije ispravan.")

def pozvoni():
    messagebox.showinfo(title="Pozvonili ste!", message="Zvono aktivirano, uskoro će doći netko i otvoriti vrata.")

window = Tk()
window.title("SmartKey")
window.geometry("400x400")

otključaj_gumb = Button(window, text="Otključaj", command=otključaj)
otključaj_gumb.pack()

pozvoni_gumb = Button(window, text="Pozvoni", command=pozvoni)
pozvoni_gumb.pack()

window.mainloop()
