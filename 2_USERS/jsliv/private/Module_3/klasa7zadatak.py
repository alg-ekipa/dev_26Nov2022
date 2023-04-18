#ZADATAK
#Kkreirati klasu Korisnik, svojstva po izboru, mora imati datum rođenja, ime prezime (jedna varijabla) - koju zatim razdvojite u dvije
#u klasi definirati metodu kojom se računa starost korisnika na naćin da se oduzme današnji datum od njegova datuma rođenja
#koristiti modul datetime
#kreirati par objekata, pozvati metodu i ispsati starost korisnika/objekta
import datetime


class Korisnik:
    def __init__(self, ime_prezime, datum_rodjenja, visina):
        self.ime_prezime = ime_prezime
        self.datum_rodjenja = datum_rodjenja
        self.visina = visina
    
        odvojeno = ime_prezime.split(" ")
        self.ime = odvojeno[0]
        self.prezime = odvojeno[1]

    def racunaj_starost(self):
        danas = datetime.date.today()
        godina = int(self.datum_rodjenja[0:4])
        mjesec = int(self.datum_rodjenja[4:6])
        dan = int(self.datum_rodjenja[6:8])
        datum_rodj = datetime.date(godina, mjesec, dan)
        starost_dani = (danas - datum_rodj).days
        starost_godine = int(starost_dani/365)
        return starost_godine
    
    def ispis(self):
        print(self.ime_prezime, self.datum_rodjenja, self.visina)

korisnik_objekt = Korisnik("Julijana Slivnjak", "10051983", "1.72")
print(korisnik_objekt.racunaj_starost())
print(korisnik_objekt.ime)


"""   
baza_podataka = []

for i in range(1):
    imeprezime_unos = input("Unesi ime i prezime klijenta: ")
    datumrodjenja_unos = str(input("Unesi datum rođenja klijenta: "))
    visina_unos = float(input("Unesi visinu klijenta: "))
    print()

    korisnik_objekt = Korisnik(imeprezime_unos, datumrodjenja_unos, visina_unos)

    baza_podataka.append(korisnik_objekt)

for korisnik in baza_podataka:
    korisnik.ispis()

datum1 = datetime.date(2000, 11, 24)
datum2 = datetime.date(2023, 3,4)
print(round((datum2 - datum1).days/365),2)
"""

korisnik_objekt = Korisnik("Petar Petrić", "10.05.1983.", 1.85)




   

