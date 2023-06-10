from tkinter import *

class PocetniPozvoniOtkljucaj:
    def __init__(self, root):
        self.root = root
        self.frameKey = LabelFrame(self.root, text = "Key", padx=400, pady=20)
        self.frameKey.grid(row=0, column=0)

        self.pozvoniBtn = Button(self.frameKey, text = "Zvono", padx=10, pady=10)
        self.pozvoniBtn.grid(row=0, column=1)

        self.otkljucajBtn = Button(self.frameKey, text="Otkljucaj", padx=10, pady=10)
        self.otkljucajBtn.grid(row=0, column=2)

    def pozvoni(self):
        messagebox.showinfo(("Upozorenje", "Pozvonili ste, pričekajte"))
    
    def otkljucaj(self):
        PINPanel
        

class PINPanel:
    #Sve što stoji na pin panelu, LabelFrame PIN Panel, tipkovnica, status i poruke



class AdminPanel:
    #LabelFrame Upravljanje, natpisi IME, Prezime, PIN, Aktivan, polja za unos (ista4)


baza = db.connect("SmartKeyUsers.db")
baza.execute("CREATE TABLE IF NOT EXISTS Korisnici ( ime TEXTNOT NULL, prezime TEXT, pin NUMBER)")
cursor = baza.cursor()
baza.commit()

def new_user():
    baza = db.connect("SmartKeyUsers.db")
    ime = ime_var.get()
    prezime = prezime_var.get()
    pin = pin_var.get()

    baza.execute("INSERT INTO Korisnici(ime, prezime, pin) VALUES(?, ?, ?)", (ime, prezime, pin))


root = Tk()

PocetniPozvoniOtkljucaj(root)

root.mainloop()