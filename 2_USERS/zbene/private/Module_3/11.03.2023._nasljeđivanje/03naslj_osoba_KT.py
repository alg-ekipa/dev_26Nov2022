class Osoba:
    def __init__ (self, ime, OIB, adresa):
        self.ime = ime
        self.OIB = OIB
        self.adresa = adresa

#bez nasljeđivanja

'''class TvrtkaOsoba:
    def __init__ (self, ime, OIB, adresa, broj_djelatnika, pravni_oblik):
        self.ime = ime
        self.OIB = OIB
        self.adresa = adresa
        self.broj_djelatnike = broj_djelatnika
        self.pravni_oblik = pravni_oblik

class DjelatnikOsoba:
    def __init__ (self, ime, OIB, adresa, radno_mjesto):
        self.ime = ime
        self.OIB = OIB
        self.adresa = adresa
        self.radno_mjesto = radno_mjesto'''

class Tvrtka(Osoba):
    def __init__(self, ime, OIB, adresa, broj_djelatnika, pravni_oblik):
        super().__init__ (ime, OIB, adresa)
        self.broj_djelatnika = broj_djelatnika
        self.pravni_oblik = pravni_oblik

class Djelatnik(Osoba):
    def __init__(self, ime, OIB, adresa, radno_mjesto):
        super().__init__(ime, OIB, adresa)
        self.radno_mjesto = radno_mjesto

t = Djelatnik('Hrvoje Horvat', '1234567890', 'Ulica 1', 'developer')
print(t.ime, t.OIB, t.adresa, t.radno_mjesto)
p = Tvrtka ('Py d.o.o.', '9876543210', 'Prava 1', 100, 'd.o.o.')
print (p.ime, p.OIB, p.adresa, p.pravni_oblik)