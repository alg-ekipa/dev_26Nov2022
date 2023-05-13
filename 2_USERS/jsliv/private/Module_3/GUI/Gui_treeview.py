import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

def procitaj_podatke():
    datoteka = open("C:/Users/JulijanaS/Desktop/VisualStudioCode/dev_26Nov2022-1/2_USERS/jsliv/private/Module_3/GUI/adresar.txt", "r")
   
    for broj, redak in enumerate(datoteka):
        redak = redak.rstrip().split(",")
        #print(broj, redak)
        tree.insert("",tk.END, iid=broj, text=redak[0], values = redak[1:])

    

stupci = ("e-mail", "Mobitel")  #već postoji po defaultu prvi stupac

tree = ttk.Treeview(root, columns=stupci, height=10)
tree.pack(padx=5, pady=5)

tree.heading("#0", text="Ime i prezime")
tree.heading("e-mail", text="E-mail")
tree.heading("Mobitel", text="Mobitel")

procitaj_podatke()

root.mainloop()