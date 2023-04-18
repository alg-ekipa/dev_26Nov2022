'''Zadatak
Kreirati klasu korisnika: 
- svojstva po izboru
- mora imati datum rodenja
- ime i prezime se unosi kao jedna varijabla koja se radvzaja na 2 djela (split)
Uklasi definirati metodu kojom se racuna starost korisnika:
- oduzima danasnji datum od njegova datuma rođenja, Koristiti modul datetime

kreirati par objekata, pozivati metodu i ispisati starost korisnika/objekta'''


import datetime


class Osoba:
    def __init__(self, ime, prezime, datum_rodenja,godine):
        self.ime = ime
        self.prezime = prezime
        self.datum_rodenja = datum_rodenja
        self.godine = godine
        
    def kreiranje_osobe():
        registar_osoba = {}
        danas = datetime.date.today()

        while True:
            kreirani_korisnik = kreirani_korisnik(ime, prezime, datum_rodenja, godine)
            ime_prezime = input('Unesi ime i prezime: ').split()
            ime = ime_prezime[0]
            prezime = ime_prezime[1]
            datum_rodenja = input('Datum rođenja DD.MM.GGGG.: ')
            datum_split = datum_rodenja.split('.')
            date1 = datetime.date(int(datum_split[2]),int(datum_split[1]),int(datum_split[0]))
            date2 = datetime.date(danas.year,danas.month,danas.day)
            godine = ((date2 - date1).days%365)

            if not input('Nastavljamo sa Unosom osoba? (za NE pritisni enter)'):
                break


korisnik_objekt = Osoba()
print(korisnik_objekt.kreiranje_osobe())




