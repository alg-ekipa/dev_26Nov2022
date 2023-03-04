# ZADATAK: 
# Kreirati klasu korisnik (svojstva po izboru), ali mora imati datum rođenja. Ime i prezme unosi se kao jedna varijabla, koju zatim razdvojite u dvije
# u klasi definirati metodu kojem se računa starost korinsika na način da se oduzme danjašnji datum od datuma njegovog rođenja
# koristiti modul datetime
# Kreirati par objekata i pozivati metodu i ispisati starost korisnika

import datetime

class Korisnik:
    def __init__(self, ime_i_prezime, datum_rodenja, mjesto_rodenja):
        self.ime_i_prezime = ime_i_prezime
        self.datum_rodenja = datum_rodenja
        self.mjesto_rodenja = mjesto_rodenja

    def dobiti_ime(self):
        return self.ime_i_prezime.split[0]
    
    def dobiti_prezime(self):
        return self.ime_i_prezime.split[1]
    
korisnik1 = Korisnik('Josip Matić','','Osijek')
korisnik2 = Korisnik('Ivana Ivić','','Gračac')

print(datetime.date.today())
