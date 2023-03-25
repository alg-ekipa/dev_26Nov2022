import datetime as dt

class Klijent:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime

    def ispis(self):
        print(f"{self.ime} {self.prezime}")
      

class Termini(Klijent):
    def __init__(self, termin):
        super().__init__(ime, prezime)
        self.termin = termin
    
    def ispis(self):
        #super().ispis()
        print(f"{self.ime} {self.prezime} {self.termin}")


sastanci = []

def unos_klijenta():
    unos_ime = input("Unesi ime: ")
    unos_prezime = input("Unesi prezime: ")
    termin_sastanka = input("Unesi termin u obilku dd.mm.yyyy: ")
    sastanci.append(Termini(unos_ime, unos_prezime, termin_sastanka))
    odabir = ("Želite unjeti novi termin? DA/NE ---> ")
    if odabir == "Da":
        unos_klijenta()
           

#for klijent in klijenti:
#    klijent.ispis()

unos_klijenta()

for vrijeme in sastanci:
    vrijeme.ispis()

