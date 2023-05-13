import tkinter as tk
import tkinter.ttk as ttk 
# ttk za treeview

# Unošenje informacija sa tekstualne datoteke i stavljanje u treeview pregled

root = tk.Tk()

def procitaj_podatke(): 
    datoteka = open('adresar.txt','r') # Pazi da si na pravom pathu kada pokrećeš 

    for broj, redak in enumerate(datoteka): 
        redak = redak.rstrip().split(',') # Svaki redak da pročita i rasporedi ih u liste
        #print(broj, redak)
        tree.insert('', tk.END, iid=broj, text=redak[0], values=redak[1:]) 
        # Prazan string je parent string 
        # tk.END - appenda na kraj podatke
        # iid = redni broj, automatski ga generira enumerate od 0
        # text - prvi član u listi, početak uzimanja podataka, indeks 0
        # values - sljedeće vrijednosti podataka koje uzima, od indeksa 1 do kraja


stupci = ('e-mail','mobitel') # Već postoji defoltni prvi stupac pa je u n-torku dovoljno za sad staviti ova dva

tree = ttk.Treeview(root, column=stupci, height=10) # Treeview je isto widget i ide na root
tree.pack(padx=5, pady=5)

# Dodijeliti naslove stupaca

tree.heading('#0', text='Ime i prezime') # Prvi stupac #0
tree.heading('e-mail', text='E-mail')
tree.heading('mobitel', text='Mobitel')

procitaj_podatke()



root.mainloop()