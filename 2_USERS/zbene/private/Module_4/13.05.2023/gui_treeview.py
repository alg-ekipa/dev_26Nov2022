import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

def pročitaj_podatke():
    datoteka = open('adresar.txt', 'r')

    for broj, redak in enumerate (datoteka):
        redak = redak.rstrip().split(',')
        #print(broj,redak)
    tree.insert('', tk.END, iid = broj, text = redak[0], values=redak[1:])
    #'' - prazan string je parent string
    #tk.END - appenda na kraj podatke
    #iid=redni broj, automatski ga generira enumerate od 0
    #text - prvi član u listi, početak uzimanja podataka, indeks 0
    #values - sljedeće vrijednosti podataka koje uzima, od indeksa 1 do kraja


stupci = ('e-mail', 'mobitel') #već postoji defaultni prvi stupac

tree = ttk.Treeview (root, columns = stupci, height = 10)
tree.pack(padx=5, pady=5)

tree.heading('#0', text='Ime i prezime')
tree.heading('e-mail',text='E-mail')
tree.heading('mobitel',text='Mobitel')

pročitaj_podatke()

root.mainloop()