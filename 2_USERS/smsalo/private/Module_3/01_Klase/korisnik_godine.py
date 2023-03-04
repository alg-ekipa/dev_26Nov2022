#ZADATAK
# Kreirati klasu Korisnik, svojstav po izboru, no mora imati datum rođenja
# ime i prezime se unosi kao jedna varijabla, koja se razdvaja na dva dijela
# u klasi definirati metodu kojom se računa starost korisnika na nacin da se oduzme današnji datum od njegovog datuma rođenja
# koristiti modul datetime
# kreirati par objekata, pozivati metodu i ispisati starost korinika


import datetime

class Korisnik:
    def __init__(self, naziv, datum_rodenja, mjesto_rodenja):
        self.naziv=naziv
        self.datum_rodenja=datum_rodenja #format yyyymmdd
        self.mjesto_rodenja=mjesto_rodenja
        
        ime_prezime=naziv.split(' ')
        self.ime=ime_prezime[0]
        self.prezime=ime_prezime[1]

    def starost_racun(self):
        danas=datetime.date.today()
        godina=int(self.datum_rodenja[0:4])
        mjesec=int(self.datum_rodenja[4:6])
        dan=int(self.datum_rodenja[6:8])
        datum_r=datetime.date(godina, mjesec, dan)
        starost_dani=(danas-datum_r).days
        starost_godine=int(starost_dani/365)
        return starost_godine

korisnik=Korisnik('Iva Ivic', '19660412', 'Zagreb')
print(korisnik.starost_racun())
print(korisnik.ime())
        

