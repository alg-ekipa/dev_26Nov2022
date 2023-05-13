import tkinter as tk
import tkinter.ttk as ttk

root=tk.Tk()
root.title('Adresar')

def procitaj_podatke():
    datoteka = open('adresar.txt', 'r')
    
    for broj, redak in enumerate(datoteka):
        redak=redak.rstrip.split(';')              #rstrip briše s kraja redka razmak, enter, točka zarez
        #print(broj, redak)
        tree.insert('', tk.END, iid=broj, text=redak[0], values=redak[1:])      
        #'' prazan string je parent string
        # tk.END appenda na kraj podatke
        # iid = redni broj, automatski enumerate od 0
        # text - prvi član u listi, početak uzimanja podataka, index 0
        # values  - sljedeće vrijednosti podatka koje uzima, od indexa 1 do kraja



stupci=('e-mail', 'mobitel')            #vec postoji defaultni prvi stupac

tree=ttk.Treeview(root, columns=stupci, height=10)
tree.pack(padx=5, pady=5)

tree.heading('#0', text='Ime i prezime')
tree.heading('e-mail', text='E-mail')
tree.heading('mobitel', text='Mobitel')

procitaj_podatke()


root.mainloop()