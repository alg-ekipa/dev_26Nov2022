import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

def procitaj_podatke():
    datoteka = open('C:/Users/hyperv/Desktop/H/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/07_GUI/adresar.txt','r')

    for broj,redak in enumerate(datoteka):
        redak = redak.rstrip().split(',')       # rstrip - briše /n na kraju svakog retka u adresaru (jer kad pritisnemo enter idemo udrgi red, iako ga ne vidim)
        #print(broj,redak)
        tree.insert('',tk.END, iid=broj, text=redak[0],values=redak[1:])
        # '' - prazan string jer parent string
        # tk.END - appenda na kraj podatke
        # iid - redni broj, automatski ga generira 'enumerate' od 0
        # text - prvi član u listi, početak uzimanja podataka
        # values - sljedće vrijednosti podataka koje uzima, od indeksa 1 do kraja

stupci = ('e-mail','mobitel')       # već postoji prvi stupac, zato ne moramo stavljati stupac za ime i prezime

tree= ttk.Treeview(root, columns=stupci, height=10)
tree.pack(padx=5, pady=5)

tree.heading('#0',text='Ime i Prezime')
tree.heading('e-mail',text='E-mail')
tree.heading('mobitel',text='Mobitel')

procitaj_podatke()


root.mainloop()