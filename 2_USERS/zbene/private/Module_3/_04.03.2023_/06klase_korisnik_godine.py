#ZADATAK
#kreirati klasu Korisnik, svojstva po izboru, no mora imati datum rođenja i ime i prezime unosi se kao jedna varijabla koju zatim razdvojite u dvije
#u klasi definirati metodu kojom se računa starost korisnika na način da se oduzme današnji datum od njegovog datuma rođenja
#koristiti modul datetime
#kreirati par objekata i pozivati metodu i ispisati starost korisnika/objekata

import datetime

class Korisnik:
    def __init__(self, ime_i_prezime, mjesto_rođenja, datum_rođenja):
        self.ime_i_prezime = ime_i_prezime
        self.mjesto_rođenja = mjesto_rođenja
        self.datum_rođenja = datum_rođenja

    def dođi_do_imena(self):
        return self.ime_i_prezime.split()[0]
    
    def dođi_do_prezimena(self):
        return self.ime_i_prezime.split()[1]

    def dođi_do_starosti(self):
        danas = datetime.date.today()
        godina = int(self.datum_rođenja[0:4])
        mjesec = int(self.datum_rođenja[4:6])
        dan = int(self.datum_rođenja[6:8])
        datum_rođenja = datetime.date(godina, mjesec, dan)
        starost_dani = (danas - datum_rođenja).days
        starost_godine = int(starost_dani/365)
        return starost_godine
            
korisnik_objekta1 = Korisnik('Marko Marković', 'Zagreb', '19900101')
korisnik_objekta2 = Korisnik('Ana Anić', 'Split', '19850515')
korisnik_objekta3 = Korisnik('Ivan Ivanović', 'Rijeka', '20001130')

korisnici = [korisnik_objekta1, korisnik_objekta2, korisnik_objekta3]

for korisnik in korisnici:
    print(f"Ime: {korisnik.dođi_do_imena()}")
    print(f"Godine: {korisnik.dođi_do_starosti()}")
    print(f"Mjesto rođenja: {korisnik.mjesto_rođenja}")
    print()