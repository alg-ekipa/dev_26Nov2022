from tkinter import *

class Rezultati_otpornici(Frame):
    def __init__(self, root, color):
        super().__init__()
        self.root = root
        self.color = color
        self["hight"] = 500
        self["width"] = 200
        self["relief"] = RAISED
        self["BD"] = 5
        self["bg"] = color

    def izracunaj_seriju(self, R1, R2):
        Rserija = int(R1) + int(R2)

        rezultat_serija = Entry(self.root)
        rezultat_serija.grid(row=4, column=0)
        rezultat_serija.insert(END, str(Rserija))
    
    def izracunaj_paralelu(self, R1, R2):
        Rparalela = (int(R1) * int(R2))/(int(R1) + int(R2))
        print(Rparalela)

        rezultat_paralela = Entry(self.root)
        rezultat_paralela.grid(row=4, column=1, pady=20, sticky="n")
        rezultat_paralela.insert(END, str(Rparalela))
    
class NatpisUnosR(Label):
    pass
    

root = Tk()

uputa = Label(root, text = "Unesite iznos otpornika", font=("Segoe UI", 14), fg = "blue")
uputa.grid(row=1, column=0, columnspan=2)

oznakaR1 = Label(root, text = "R1").grid(row=1, column=0)
oznakaR2 = Label(root, text="R2").grid(row=2, column=0)

unosR1 = Entry(root)
unosR1.grid(row=1, column=1)

unosR2 = Entry(root)
unosR2.grid(row=2, column=1)

gumb_serija = Button(root, text="Serijski spoj", height=2, width=10,
                     font=("Sagoe UI", 14),
                     fg = "white",
                     bg="blue",
                     command = lambda: frame_serija.izracunaj_seriju(unosR1.get(), unosR2.get()))
gumb_serija.grid(row=3,column=0)

gumb_paralela.grid = Button(root, text="Paralelni spoj", height=2, width=10,
    font=("Sagoe UI", 14),
    




    



