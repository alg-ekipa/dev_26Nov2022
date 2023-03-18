class Ucenik():

    # KONSTRUKTOR - metoda koja se zove _init_ (initialaze), u nju se prenose parametri odnosno svojstva, karakteristike
    # prvi argument je uvijek SELF

    def __init__(self, ime, prezime, mbr, adresa, ocjena):
        # definiramo da se pridruživanje vrijednosti uvijek odnosi na objekt koji inicijaliziramo
        self.ime= ime
        self.prezime= prezime
        self.mbr= mbr
        self.adresa= adresa
        self.ocjena= ocjena

    #metoda za ispis
    def ispisi(self):
        print(f'Ime ucenika: {self.ime}, prezime: {self.prezime}, mbr: {self.mbr}, adresa: {self.adresa}, ocjena: {self.ocjena}')


ucenik1 = Ucenik('Josip', 'Matic', '345678', 'Velika ul. 3', 5)
print(ucenik1.ime, ucenik1.prezime)

lista_podataka_ucenik1= [ucenik1.ime, ucenik1.prezime, ucenik1.mbr, ucenik1.adresa, ucenik1.ocjena]
print(lista_podataka_ucenik1)

ucenik2= Ucenik( 'Ana', 'Matic','456789', 'Gornji grad 12', 4)
print(ucenik2.ime, ucenik2.prezime)
lista_podataka_ucenik2= [ucenik2.ime, ucenik2.prezime, ucenik2.mbr, ucenik2.adresa, ucenik2.ocjena]

ime_ucenika3='Ante'
prezime_ucenik3= 'Antic'
mbr_ucenika3='7894561'
adresa_ucenik3='Uska cesta'
ocjena_ucenik3= 2

ucenik3=Ucenik(ime_ucenika3, prezime_ucenik3, mbr_ucenika3, adresa_ucenik3, ocjena_ucenik3)
print(ucenik3.ime, ucenik3.prezime)

lista_ocjena=[ucenik1.ocjena, ucenik2.ocjena, ucenik3.ocjena]
print(lista_ocjena)

#napravi kreiranje objekta kroz petlju: unesite 5 ucenika, koje zatim kreirate kao objekte klase ucenik

print(ucenik1)   #nema smisla, prikazuje da je rijec o nekom objektu na nekoj memorijskoj lokaciji

ucenik1.ispisi()        #koristimo metodu za ispis koja se nalazi unutar klase Ucenik
ucenik2.ispisi()
ucenik3.ispisi()

