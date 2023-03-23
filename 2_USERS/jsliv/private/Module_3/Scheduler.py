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

klijenti = []
termini = []

while True: 
    ime = input("Unesite ime klijenta: ")
    prezime = input("Unesite prezime klijenta: ")
    klijenti.append(Klijent(ime, prezime))

    dolazak = input("Unesite termin u formati dd mm yyyy: ")
    termini.append(Termini(dolazak))

    if input("Želite li unjeti novog klijenta DA/NE: "):
        break


for termin in termini:
    termin.ispis()




    
              


        