#napraviti da su karakteristike prazne (ime, prezime....) Tako da kasnije možemo puniti
#konstruktor - metoda koja se zove __init__ (initialize), u nju se prenose parametri, karakteristike/svojstva
#prvi argument je uvijek: self!

class Ucenik():
    def __init__(self, ime, prezime, mbr, adresa, ocjena):
        #definiramo da se pridruživanje vrijednosti uvijek odnosi na objekt koji inicjaliziramo
        self.ime = ime
        self.prezime = prezime
        self.mbr = mbr
        self.adresa = adresa
        self.ocjena = ocjena

#metoda/funkcija za ispis (svi podaci za svakog ucenika) Možemo napraviti i formatiran ispis
    def ispisi(self):
        print(self.ime, self.prezime, self.mbr, self.adresa, self.ocjena)


ucenik1 = Ucenik("Josip", "Matić", "345678", "Velika ulica 3", 5)
print(ucenik1.ime, ucenik1.prezime)

#možemo staviti u listu
lista_podataka_ucenik1 = [ucenik1.ime, ucenik1.prezime, ucenik1.mbr, ucenik1.adresa, ucenik1.ocjena]
print(lista_podataka_ucenik1)

ucenik2 = Ucenik("Ivana", "Ivic", "987654", "Uska ulica 2", 4)
print(ucenik2.ime, ucenik2.prezime)

lista_podataka_ucenik2 = [ucenik2.ime, ucenik2.prezime, ucenik2.mbr, ucenik2.adresa, ucenik2.ocjena]
print(lista_podataka_ucenik2)


ime_ucenik3 = input("Unesi ime ucenika3: ")
prezime_ucenik3 = input("Unesi prezime ucenika3: ")
mbr_ucenik3 = input("Unesi mbr ucenika3: ")
adresa_ucenik3 = input("Unesi adresu ucenika3: ")
ocjena_ucenik3 = int(input("Unesi ocjenu ucenika3: "))

ucenik3 = Ucenik(ime_ucenik3, prezime_ucenik3, mbr_ucenik3, adresa_ucenik3, ocjena_ucenik3)
print(ucenik3.ime, ucenik3.prezime)

#Popuniti listu ocjena sva tri učenika i izračunati prosjek
lista_ocjena = [ucenik1.ocjena, ucenik2.ocjena, ucenik3.ocjena]
prosjek = round((sum(lista_ocjena)/len(lista_ocjena)),2)
print(prosjek)

#metoda za ispis, funkcija gore formirana
ucenik1.ispisi()
ucenik2.ispisi()
ucenik3.ispisi()



#To do - kreiranje objekata kroz petlju: unesite 5 učenika, koje zatim kreirajte kao objekte klase učenika (Unos preko tipkovnike)