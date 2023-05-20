from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import sqlite3

root=Tk()
root.title('Zvono')

#Stanari
create_table_query = '''CREATE TABLE Stanari (
            ime text,
            prezime text,
            pin text
            )'''
database_name = "Stanari_kljuc.db"

try:
    sql_connect = sqlite3.connect(database_name)
    cursor = sql_connect.cursor()
    cursor.execute(create_table_query)
    cursor.execute("INSERT INTO Stanari VALUES ('Admin', 'Admin', '1234')")
    cursor.execute("INSERT INTO Stanari VALUES ('Ante', 'Kovačić', '1111')")
    cursor.execute("INSERT INTO Stanari VALUES ('Tin', 'Ujević', '2222')")
    sql_connect.commit()

    record_all = cursor.fetchall()

    cursor.close()

except sqlite3.Error as e:
    print('Pogreška: ', e)

finally:
    if sql_connect:
        sql_connect.close()

#funkcije
def pozvoni():
    messagebox.showinfo('Zvono', 'Pozvonili ste!')

def otkljucaj():
    #prozor za pin
    pin_entry=Entry(frame_kljuc)
    pin_entry.grid(row=0, columnspan=3, column=0, padx=10, pady=10)

    #poruka
    poruka=Label(frame_kljuc, text='Unesite 4-znamenkasti pin za otključavanje')
    poruka.grid(row=0, columnspan=3, column=3, padx=10, pady=10)

    #tipkovnica
    button0=Button(frame_kljuc, text='0', padx=30, pady=30, command=lambda: dod_broj('0'))
    button0.grid(row=4, column=1)

    button1=Button(frame_kljuc, text='1', padx=30, pady=30, command=lambda: dod_broj('1'))
    button1.grid(row=1, column=0)

    button2=Button(frame_kljuc, text='2', padx=30, pady=30, command=lambda: dod_broj('2'))
    button2.grid(row=1, column=1)

    button3=Button(frame_kljuc, text='3', padx=30, pady=30, command=lambda: dod_broj('3'))
    button3.grid(row=1, column=2)

    button4=Button(frame_kljuc, text='4', padx=30, pady=30, command=lambda: dod_broj('4'))
    button4.grid(row=2, column=0)

    button5=Button(frame_kljuc, text='5', padx=30, pady=30, command=lambda: dod_broj('5'))
    button5.grid(row=2, column=1)

    button6=Button(frame_kljuc, text='6', padx=30, pady=30, command=lambda: dod_broj('6'))
    button6.grid(row=2, column=2)

    button7=Button(frame_kljuc, text='7', padx=30, pady=30, command=lambda: dod_broj('7'))
    button7.grid(row=3, column=0)

    button8=Button(frame_kljuc, text='8', padx=30, pady=30, command=lambda: dod_broj('8'))
    button8.grid(row=3, column=1)

    button9=Button(frame_kljuc, text='9', padx=30, pady=30, command=lambda: dod_broj('9'))
    button9.grid(row=3, column=2)

    buttonC=Button(frame_kljuc, text='C', padx=30, pady=30)
    buttonC.grid(row=4, column=0)

    buttonE=Button(frame_kljuc, text='E', padx=30, pady=30, command=lambda:potvrdi(pin_entry))
    buttonE.grid(row=4, column=2)

def dod_broj(broj):
    br = pin_entry.get()
    pin_entry.delete(0, END)
    pin_entry.insert(0, br+broj)

#ne radi 

def obrisi_tekst():
    pin_entry.delete(0, END)

def potvrdi(pin_entry):
    sql_connect = sqlite3.connect(database_name)
    cursor = sql_connect.cursor()
    cursor.execute("SELECT pin FROM Stanari WHERE pin=?", (pin_entry.get(),))
    pin = cursor.fetchone()[0]

    # Provjera PIN
    if pin == pin_entry.get() and pin != "1234":
        cursor.execute("SELECT ime, prezime FROM Stanari WHERE pin=?",(pin_entry.get(),))
        ime, prezime = cursor.fetchone()
        status_label = Label(frame_kljuc, text=f'Dobro došli, {ime} {prezime}!')
        status_label.grid(row=2, column=5)

    elif pin == "1234":
        status_label = Label(frame_kljuc, text=f'Dobro došli Admin!')
        status_label.grid(row=2, column=5)
        record_all = cursor.fetchall()
        for broj, redak in enumerate(record_all):
            tree.insert('', END, iid=broj, text=redak[0], values=redak[1:])      

        stupci=('prezime', 'pin')

        tree=ttk.Treeview(frame_admin, columns=stupci, height=10)
        tree.grid(row=5, column=0, padx=5, pady=5)

        tree.heading('#0', text='Ime' )
        tree.heading('prezime', text='Prezime')
        tree.heading('pin', text='PIN')

        # Kreiranje gumba za uređivanje, brisanje i dodavanje

        btn_uredi = Button(frame_admin, text="Uredi", command=lambda: uredi)
        btn_uredi.grid(row=5, column=7)

        btn_obrisi = Button(frame_admin, text="Obriši", command=lambda: obrisi)
        btn_obrisi.grid(row=5, column=8)

        btn_dodaj = Button(frame_admin, text="Novi", command=lambda: dodaj)
        btn_dodaj.grid(row=5, column=9)

    else:
        status_label = Label(frame_kljuc, text='Neispravan PIN')
        status_label.grid(row=2, column=5)

    #status_label.config(text='')

    sql_connect.close()

def dodaj(ime, prezime, pin):
    sql_connect = sqlite3.connect(database_name)
    cursor = sql_connect.cursor()
    cursor.execute("INSERT INTO korisnici VALUES (?, ?, ?)", (ime, prezime, pin))
    sql_connect.commit()
    sql_connect.close()

def uredi(ime, prezime, pin):
    sql_connect = sqlite3.connect(database_name)
    cursor = sql_connect.cursor()
    cursor.execute("UPDATE korisnici SET ime=?, prezime=?, pin=? WHERE pin=?", (ime, prezime, pin, pin))
    sql_connect.commit()
    sql_connect.close()


def obrisi(pin):
    sql_connect = sqlite3.connect(database_name)
    cursor = sql_connect.cursor()
    cursor.execute("DELETE FROM korisnici WHERE pin=?", (pin))
    sql_connect.commit()
    sql_connect.close()

#GUI

#okviri
frame_pocetni=Frame(root)
frame_pocetni.grid(row=0, column=0, padx=20, pady=20)

frame_kljuc=Frame(root)
frame_kljuc= LabelFrame(root, text='Tipkovnica', padx=20, pady=20)
frame_kljuc.grid(row=1, column=0, padx=20, pady=20)

frame_admin=Frame(root)
frame_admin=LabelFrame(root, text='Administrator', padx=20, pady=20)
frame_admin.grid(row=5, columnspan=10, column=0, padx=20, pady=20)

label_frame_pocetni=LabelFrame(frame_pocetni, text='Ulaz')
label_frame_pocetni.grid(row=0, column=0)

btn_zvono = Button(frame_pocetni, text='ZVONO', font=('Verdana',10, 'bold' ), bg='#EBDEF0', padx=30, command=pozvoni)        
btn_otkljucaj = Button(frame_pocetni, text='OTKLJUČAJ',font=('Verdana',10, 'bold' ), bg='#EBDEF0', padx=30, command=otkljucaj)
btn_zvono.grid(row=0, column=1, padx=30)
btn_otkljucaj.grid(row=0, column=2, padx=30)


root.mainloop()