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

klijenti = []
appointment = []

while True: 
    ime = input("Unesite ime klijenta: ")
    prezime = input("Unesite prezime klijenta: ")
    klijenti.append(Klijent(ime, prezime))

    dolazak = input("Unesite termin u formati dd.mm.yyyy: ")
    appointment.append(Termini(dolazak))

    pitanje = input("Želite li unjeti novog klijenta DA/NE: ")
    if pitanje == "NE":

        break
    else:
        True 


#for klijent in klijenti:
#    klijent.ispis()

for vrijeme in appointment:
    vrijeme.ispis()




    
              


        