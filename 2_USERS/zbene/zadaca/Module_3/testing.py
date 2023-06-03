from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import sqlite3

def otključaj():
    print("Otključano!")

def pozvoni():
    messagebox.showinfo(title="Pozvonili ste!", message="Zvono aktivirano, uskoro će doći netko i otvoriti vrata.")

def prikazi_administraciju():
    # Logika za prikaz administracije
    pass

def otvori_administraciju():
    admin_pin = unos_pina.get()
    if admin_pin == "0006":
        unos_pina.delete(0, END)
        prikazi_administraciju()
        window.destroy()  # Zatvaranje početnog prozora
    else:
        messagebox.showwarning(title="Pogrešan PIN", message="Uneseni PIN nije ispravan.")

prikazi_pocetni_ekran = True

window = Tk()
window.title("SmartKey")
window.geometry("400x450")

otključaj_gumb = Button(window, text="Otključaj", command=otključaj)
otključaj_gumb.pack()

pozvoni_gumb = Button(window, text="Pozvoni", command=pozvoni)
pozvoni_gumb.pack()

root = Frame(window, padx=40, pady=40)
root.pack()

unos_pina = Entry(root)
unos_pina.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

gumb0 = Button(root, text='0', padx=40, pady=20, command=lambda: upiši_broj('0'))
gumb0.grid(row=3, column=1)

gumb1 = Button(root, text='1', padx=40, pady=20, command=lambda: upiši_broj('1'))
gumb1.grid(row=0, column=0)

gumb2 = Button(root, text='2', padx=40, pady=20, command=lambda: upiši_broj('2'))
gumb2.grid(row=0, column=1)

gumb3 = Button(root, text='3', padx=40, pady=20, command=lambda: upiši_broj('3'))
gumb3.grid(row=0, column=2)

gumb4 = Button(root, text='4', padx=40, pady=20, command=lambda: upiši_broj('4'))
gumb4.grid(row=1, column=0)

gumb5 = Button(root, text='5', padx=40, pady=20, command=lambda: upiši_broj('5'))
gumb5.grid(row=1, column=1)

gumb6 = Button(root, text='6', padx=40, pady=20, command=lambda: upiši_broj('6'))
gumb6.grid(row=1, column=2)

gumb7 = Button(root, text='7', padx=40, pady=20, command=lambda: upiši_broj('7'))
gumb7.grid(row=2, column=0)

gumb8 = Button(root, text='8', padx=40, pady=20, command=lambda: upiši_broj('8'))
gumb8.grid(row=2, column=1)

gumb9 = Button(root, text='9', padx=40, pady=20, command=lambda: upiši_broj('9'))
gumb9.grid(row=2, column=2)

gumbC = Button(root, text='C', padx=40, pady=20, command=lambda: obriši_zadnji_broj('broj'))
gumbC.grid(row=3, column=0)

gumbE = Button(root, text='E', padx=40, pady=20, command=otvori_administraciju)
gumbE.grid(row=3, column=2)

if prikazi_pocetni_ekran:
    window.mainloop()
