# ZADATAK
# kreirati klasu Korisnik, svojstva po izboru, no mora imati datum rođenja i ime i prezime unosi se kao jedna varijabla, koju zatim razdvojite u dvije
# u klasi definirati metodu kojom se računa starost korinika na način da se oduzme današnji datum od njegovog datuma rođenja
# koristiti modul datetime

# kreirati par objekata, pozivati metodu i ispisati starost korisnika/objekata 

import datetime

class Korisnik:
    def __init__(self, ime_prezime, rodjen):
        self.puno_ime = ime_prezime
        self.rodjen = rodjen  # yyyymmdd

        odvojeno = ime_prezime.split(' ')
        self.ime = odvojeno[0]
        self.prezime = odvojeno[1]

    def racunaj_starost(self):
        danas = datetime.date.today() 
        godina = int(self.rodjen[0:4])
        mjesec = int(self.rodjen[4:6])
        dan = int(self.rodjen[6:8])
        datum_rodj = datetime.date(godina,mjesec,dan)
        starost_dani = (danas - datum_rodj).days
        starost_godine = int(starost_dani/365)
        return starost_godine


korisnik_objekt = Korisnik('Iva Ivić','19660412')
print(korisnik_objekt.racunaj_starost())
print(korisnik_objekt.ime)

'''
sadasnji_trenutak = datetime.datetime.now()
datum = f'\n{sadasnji_trenutak.strftime("%A")}\t\t{sadasnji_trenutak.strftime("%d.%m.%Y %H:%M:%S")}.'
print(datum) 
'''
