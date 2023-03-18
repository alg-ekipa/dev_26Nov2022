#Napravite klasu Osoba (parent) koja će nasljediti klase Učenik i Nastavnik
# Neka se unose nekoliko učenik i nastavnika preko tipkovnice, kreirju kao objekti a zatim spreme u neku listu
# lista_ucenici i lista_nastavnici

class Osoba: 
    def __init__(self, ime, prezime, OIB):
        self.ime = ime 
        self.prezime = prezime
        self.OIB = OIB

    def ispisi(self): 
        print(self.ime, self.prezime, self.OIB)

class Ucenik(Osoba): 
    def __init__(self, ime, prezime, OIB, mbr_ucenik):
        super().__init__(ime, prezime, OIB)
        self.mbr_ucenik = mbr_ucenik

class Nastavnik(Osoba): 
    def __init__(self, ime, prezime, OIB, mbr_nastavnik):
        super().__init__(ime, prezime, OIB)
        self.mbr_ucenik = mbr_nastavnik

razred = []
broj_ucenika = 2

for i in range(broj_ucenika):
    ime_ucenik = input(f'Unesi ime {i+1}. učenika : ')
    prezime_ucenik = input(f'Unesi prezime {i+1}. učenika : ')
    OIB_ucenik = input(f'Unesi OIB {i+1}. učenika : ')
    mbr_ucenik = input(f'Unesi mbr {i+1}. učenika : ')
    
    ucenik = Ucenik(ime_ucenik, prezime_ucenik, OIB_ucenik, mbr_ucenik)
    razred.append(ucenik) 
