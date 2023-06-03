import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import sqlite3

root=tk.Tk()
root.title('Zvono')

#Varijable
imeN_var=tk.StringVar()
prezimeN_var=tk.StringVar()
pinN_var=tk.StringVar()

#Stanari
q_select='''SELECT * FROM Stanari'''
database_name ='Stanari_kljuc.db'

try:
    sql_connect = sqlite3.connect(database_name)
    cursor = sql_connect.cursor()

    cursor.execute(q_select)
    record_all = cursor.fetchall()
        
    cursor.close()

except sqlite3.Error as e:
    print('Pogreška: ', e)

finally:
    if sql_connect:
        sql_connect.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')

#funkcije
def pozvoni():
    messagebox.showinfo('Zvono', 'Pozvonili ste!')

def procitaj_podatke():
    global tree
    stupci=('prezime', 'pin')
    tree=ttk.Treeview(frame_admin, columns=stupci, height=10)
    tree.grid(row=5, column=0, padx=5, pady=5)
    tree.heading('#0', text='Ime' )
    tree.heading('prezime', text='Prezime')
    tree.heading('pin', text='PIN')
    for broj, redak in enumerate(record_all):
        tree.insert('', tk.END, iid=broj, text=redak[0], values=redak[1:]) 

def dodaj_stanara():
    imeN=imeN_var.get()
    prezimeN=prezimeN_var.get()
    pinN=pinN_var.get()
    sql_connect = sqlite3.connect(database_name)
    dodaj_query= f"INSERT INTO Stanari (ime, prezime, pin) VALUES ('{imeN}', '{prezimeN}', '{pinN}')"
    sql_connect.execute(dodaj_query)
    sql_connect.commit()
    update_treeview()
    
def obrisi_stanara():
    pinN=pinN_var.get()
    sql_connect = sqlite3.connect(database_name)
    brisi_q='DELETE FROM Stanari WHERE pin=?'
    sql_connect.execute(brisi_q, (pinN,))
    sql_connect.commit()
    update_treeview()

def update_treeview():
    global tree
    tree.delete(*tree.get_children())

    try:
        sql_connect = sqlite3.connect(database_name)
        cursor = sql_connect.cursor()
        cursor.execute(q_select)
        record_all = cursor.fetchall()
        cursor.close()
    except sqlite3.Error as e:
        print('Pogreška: ', e)
        return
    finally:
        if sql_connect:
            sql_connect.close()

    # Insert the latest records into the Treeview
    for broj, redak in enumerate(record_all):
        tree.insert('', tk.END, iid=broj, text=redak[0], values=redak[1:])

def otkljucaj():
    #prozor za pin
    pin_entry=tk.Entry(frame_kljuc)
    pin_entry.grid(row=0, columnspan=3, column=0, padx=10, pady=10)

    #poruka
    poruka=tk.Label(frame_kljuc, text='Unesite 4-znamenkasti pin za otključavanje')
    poruka.grid(row=0, columnspan=3, column=3, padx=10, pady=10)

    #tipkovnica
    button0=tk.Button(frame_kljuc, text='0', padx=30, pady=30, command=lambda: dod_broj('0'))
    button0.grid(row=4, column=1)

    button1=tk.Button(frame_kljuc, text='1', padx=30, pady=30, command=lambda: dod_broj('1'))
    button1.grid(row=1, column=0)

    button2=tk.Button(frame_kljuc, text='2', padx=30, pady=30, command=lambda: dod_broj('2'))
    button2.grid(row=1, column=1)

    button3=tk.Button(frame_kljuc, text='3', padx=30, pady=30, command=lambda: dod_broj('3'))
    button3.grid(row=1, column=2)

    button4=tk.Button(frame_kljuc, text='4', padx=30, pady=30, command=lambda: dod_broj('4'))
    button4.grid(row=2, column=0)

    button5=tk.Button(frame_kljuc, text='5', padx=30, pady=30, command=lambda: dod_broj('5'))
    button5.grid(row=2, column=1)

    button6=tk.Button(frame_kljuc, text='6', padx=30, pady=30, command=lambda: dod_broj('6'))
    button6.grid(row=2, column=2)

    button7=tk.Button(frame_kljuc, text='7', padx=30, pady=30, command=lambda: dod_broj('7'))
    button7.grid(row=3, column=0)

    button8=tk.Button(frame_kljuc, text='8', padx=30, pady=30, command=lambda: dod_broj('8'))
    button8.grid(row=3, column=1)

    button9=tk.Button(frame_kljuc, text='9', padx=30, pady=30, command=lambda: dod_broj('9'))
    button9.grid(row=3, column=2)

    buttonC=tk.Button(frame_kljuc, text='C', padx=30, pady=30, command=lambda:obrisi_tekst())
    buttonC.grid(row=4, column=0)

    buttonE=tk.Button(frame_kljuc, text='E', padx=30, pady=30, command=lambda:potvrdi(pin_entry))
    buttonE.grid(row=4, column=2)

    def dod_broj(broj):
        br = pin_entry.get()
        pin_entry.delete(0, tk.END)
        pin_entry.insert(0, br+broj)

    def obrisi_tekst():
        pin_entry.delete(first=0, last=100)
       
    def potvrdi(pin_entry):
        pin_unos = pin_entry.get()
        sql_connect = sqlite3.connect(database_name)
        cursor = sql_connect.cursor()
        cursor.execute('SELECT pin FROM Stanari WHERE pin=?', (pin_unos, ))
        pin = cursor.fetchone()[0]
        print(pin)
        print(pin_unos)

        # Provjera PIN
        if pin == pin_unos and pin_unos != "1234":
            cursor.execute("SELECT ime, prezime FROM Stanari WHERE pin=?",(pin_unos,))
            ime, prezime = cursor.fetchone()
            status_label = tk.Label(frame_kljuc, text=f'Dobro došli, {ime} {prezime}!')
            status_label.grid(row=2, column=5)

        elif pin_unos == "1234":
            status_label = tk.Label(frame_kljuc, text=f'Dobro došli Admin!')
            status_label.grid(row=2, column=5)
            procitaj_podatke()      
        
            # Kreiranje gumba za brisanje i dodavanje stanara

            btn_obrisi = tk.Button(frame_admin, text="Obriši", command=obrisi_stanara)
            btn_obrisi.grid(row=1, column=3)

            btn_dodaj = tk.Button(frame_admin, text="Novi", command=dodaj_stanara)
            btn_dodaj.grid(row=2, column=3)

            imeN=tk.Label(frame_admin, text='IME: ')
            imeN.grid(row=0, column=1, padx=10, pady=10)

            prezimeN=tk.Label(frame_admin, text='PREZIME: ')
            prezimeN.grid(row=1, column=1, padx=10, pady=10)

            pinN=tk.Label(frame_admin, text='PIN: ')
            pinN.grid(row=2, column=1, padx=10, pady=10)

            entry_imeN =tk.Entry(frame_admin, textvariable=imeN_var)
            entry_imeN.grid(row=0, column=2, padx=10, pady=10)

            entry_prezimeN =tk.Entry(frame_admin, textvariable=prezimeN_var)
            entry_prezimeN.grid(row=1, column=2, padx=10, pady=10)

            entry_pinN =tk.Entry(frame_admin, textvariable=pinN_var)
            entry_pinN.grid(row=2, column=2, padx=10, pady=10)

#GUI

#okviri
frame_pocetni=tk.Frame(root)
frame_pocetni.grid(row=0, column=0, padx=20, pady=20)

frame_kljuc=tk.Frame(root)
frame_kljuc= tk.LabelFrame(root, text='Tipkovnica', padx=20, pady=20)
frame_kljuc.grid(row=1, column=0, padx=20, pady=20)

frame_admin=tk.Frame(root)
frame_admin=tk.LabelFrame(root, text='Administrator', padx=20, pady=20)
frame_admin.grid(row=5, columnspan=10, column=0, padx=20, pady=20)

label_frame_pocetni=tk.LabelFrame(frame_pocetni, text='Ulaz')
label_frame_pocetni.grid(row=0, column=0)

btn_zvono = tk.Button(frame_pocetni, text='ZVONO', font=('Verdana',10, 'bold' ), bg='#EBDEF0', padx=30, command=pozvoni)        
btn_otkljucaj = tk.Button(frame_pocetni, text='OTKLJUČAJ',font=('Verdana',10, 'bold' ), bg='#EBDEF0', padx=30, command=otkljucaj)
btn_zvono.grid(row=0, column=1, padx=30)
btn_otkljucaj.grid(row=0, column=2, padx=30)

root.mainloop()