import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

def pročitaj_podatke():
    datoteka = open('adresar.txt', 'r')

    for broj, redak in enumerate (datoteka):
        redak = redak.rstrip().split(',')
        print(broj,redak)

stupci = ('e-mail', 'mobitel') #već postoji defaultni prvi stupac

tree = ttk.Treeview (root, columns = stupci, height = 10)
tree.pack(padx=5, pady=5)

tree.heading('#0', text='Ime i prezime')
tree.heading('e-mail',text='E-mail')
tree.heading('mobitel',text='Mobitel')

pročitaj_podatke()

root.mainloop()