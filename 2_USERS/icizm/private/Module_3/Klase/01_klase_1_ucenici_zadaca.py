# napraviti kreiranje objekata kroz petlju: unesite 5 učenika, koje zatim kreirajte kao objekte klase učenik

class Ucenik():
    # KONSTRUKTOR je metoda koja se zove __init__ (initialize), u nju se prenose parametri (PROPERTIES), odnosno karakteristike (svojstva) - ostavlja sve varijable prazne
    # prvi argument je uvijek SELF
    def __init__(self, ime, prezime, mbr, adresa, ocjena): #initialise, pokreni?
        # DEFINIRAMO da se pridruživanje vrijednosti uvijek odnosi na objekt koji inicijaliziramo
        self.ime = ime
        self.prezime = prezime
        self.mbr = mbr
        self.adresa = adresa
        self.ocjena = ocjena

       # metoda za ispis
    def ispisi(self): #MORA se napisati self
        print(self.ime, self.prezime, self.mbr, self. adresa, self. ocjena)

 
razred = []
broj_ucenika = 5

for i in range(broj_ucenika):
    ime_ucenik = input(f'Unesi ime {i+1}. učenika : ')
    prezime_ucenik = input(f'Unesi prezime {i+1}. učenika : ')
    mbr_ucenik = input(f'Unesi mbr {i+1}. učenika : ')
    adresa_ucenik = input(f'Unesi adresu {i+1}. učenika : ')
    ocjena_ucenik = int(input(f'Unesi ocjenu {i+1}. učenika : '))
    ucenik = Ucenik(ime_ucenik, prezime_ucenik, mbr_ucenik, adresa_ucenik, ocjena_ucenik)
    razred.append(ucenik) 


for ucenik in razred:
    ucenik.ispisi()
#print(lista_podataka_ucenik2)


