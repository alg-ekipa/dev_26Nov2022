# ZADAĆA: kreiranje objekata kroz petlju: unesite nekoliko učenika koje zatim kreirajte kao objekte klase učenik

class Ucenik():
    def __init__ (self, ime, prezime, mbr, adresa):
        self.ime = ime
        self.prezime = prezime
        self.mbr = mbr
        self.adresa = adresa
    def ispis(self):
        print(f'Školu pohađa učenik {self.ime} {self.prezime}, {self.adresa}. Njegov MBR je: {self.mbr}')

lista_ucenika = []
broj_ucenika = int(input('Koliko učenika treba upisat: '))

for i in range(broj_ucenika):
    ime_uc = input(f'Unesi ime {i+1}. učenika: ')
    prezime_uc = input(f'Unesi prezime {i+1}. učenika: ')
    mbr_uc = input(f'Unesi MBR {i+1}. učenika: ')
    adresa_uc = input(f'Unesi adresu {i+1}. učenika: ')

    ucenik = Ucenik(ime_uc, prezime_uc, mbr_uc, adresa_uc)

    lista_ucenika.append(ucenik)



for ucenik in lista_ucenika:
    ucenik.ispis()
