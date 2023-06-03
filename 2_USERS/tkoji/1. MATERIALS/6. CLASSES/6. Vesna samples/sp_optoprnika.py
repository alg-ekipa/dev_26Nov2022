from cProfile import label
from distutils.cmd import Command
from tkinter import *

class RezultatiOtpornici(Frame):
    def __init__(self, root, color):
        super().__init__()
        self.root = root
        self.color = color    
        
        #height=500, width=200, bg='blue', relief=RAISED, bd=2
        self["height"] = 500
        self["width"] = 200
        self["relief"] = RAISED
        self["bd"] = 5
        self["bg"] = color
        
        
    def izracunaj_seriju(self, R1, R2):
        Rserija = int(R1) + int(R2)
        print(Rserija)
        rezultat_serija = Entry(self.root)
        rezultat_serija.grid(row=4, column=0)
        rezultat_serija.insert(END, str(Rserija))
            

    def izracunaj_paralelu(self, R1, R2):
        Rparalela = int(R1) * int(R2)  / int(R1) + int(R2)
        print(Rparalela)
        rezultat_paralela = Entry(self.root)
        rezultat_paralela.grid(row=4, column=1)
        rezultat_paralela.insert(END, str(Rparalela))
            
class NatpisiUnosR(Label):
    def __init__(self, root, text, fg):
        super().__init__()
        self.root = root
        print(self.root)
        self.text = text
        self
        print(self.text)
        self.fg = fg
        print(self.fg)
        self["underline"] = 0
        self["fg"] = fg
        self["text"] = text
        
            
root = Tk()

uputa = NatpisiUnosR(root, "Unesite iznose otpornika", "blue")
uputa.grid(row=0, column=0, columnspan=2)

# uputa = Label(root, text="Unesite iznose otpornika", fg='blue')
# uputa.grid(row=0, column=0, columnspan=2)

oznakaR1 = Label(root, text="R1").grid(row=1,column=0)
oznakaR2 = Label(root, text="R1").grid(row=2,column=0)

unosR1 = Entry(root)
unosR1.grid(row=1,column=1)

unosR2 = Entry(root)
unosR2.grid(row=2,column=1)

gumb_serija = Button(root, text='Serijski spoj', command= lambda: frame_serija.izracunaj_seriju(unosR1.get(),unosR2.get()))
gumb_serija.grid(row=3, column=0)
gumb_paralela = Button(root, text='Paralelni spoj', command= lambda: frame_paralela.izracunaj_paralelu(unosR1.get(),unosR2.get()))
gumb_paralela.grid(row=3, column=1)

# PREBACENO U KLASU
# frame_serija = Frame(root, height=500, width=200, bg='blue', relief=RAISED, bd=2).grid(row=4, column=0)
# frame_paralela = Frame(root, height=500, width=200, bg='green', relief=RAISED, bd=2).grid(row=4, column=1)

frame_serija = RezultatiOtpornici(root, "blue")
frame_serija.grid(row=4, column=0)
frame_paralela = RezultatiOtpornici(root, "green")
frame_paralela.grid(row=4, column=1)

root.mainloop()
