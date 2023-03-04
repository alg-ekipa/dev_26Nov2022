# ZADATAK
# kreirati klasu Korisnik, svojstva po izboru, no mora imati datum rođenja + ime i prezime unosi se kao jedna varijabla koju zatim razdvojite u dvije
# U klasi definirati metodu kojom se računa starost korisnika na način da se oduzme današnji datum od njegvog datuma rođenja
# koristiti modul datetime
# kreirati par objekata, pozivati metodu i ispisati starost korisnika / objekata

import datetime as dt

datum_rodjenja = '20001203' #format 'yyymmdd'

datum1 = dt.date(2000, 11, 24)
datum2 = dt.date(2001)

'''dan = dt.datetime.now().day
mjesec = dt.datetime.now().month
godina = dt.datetime.now().year'''

class Korisnik: 
    def __init__(self, ime_prezime, rodjen):
        self.puno_ime = ime_prezime
        self.rodjen = rodjen

        odvojeno = ime_prezime.split(' ')
        self.ime = odvojeno[0]
        self.prezime = odvojeno[1]

    def racinaj_starost(self): 
        danas = dt.date.today()
        godina = int(self.rodjen[0:4])
        mjesec = int(self.rodjen[4:6])
        dan = int(self.rodjen[6:8])
        datum_rodj = dt.date(godina, mjesec, dan)
        starost_dani = (danas - datum_rodj).days
        

'''    def __init__(self, ime, prezime, datum_r):
        self.ime = ime
        self.prezime = prezime
        self.datum_r = datum_r

    def racunaj_starost(self): 
        godina_k = godina - godina_r

    def ime_i_prezime(self):
        ime_unos = input('Unesite ime i prezime: ')
        ime_prezime_r = ime_unos.split()
        ime = ime_prezime_r[0]
        prezime = ime_prezime_r[1]
'''
'''omg sve je krivo, iskopiraj i prostudiraj please'''
