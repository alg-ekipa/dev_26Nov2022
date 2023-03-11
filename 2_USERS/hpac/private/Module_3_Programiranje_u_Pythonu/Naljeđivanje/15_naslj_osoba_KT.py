class Osoba:
    def __init__ (self, ime, OIB, adresa):
        self.ime = ime
        self.OIB = OIB
        self.adresa = adresa

# Bez nasljeđivanja
'''
class TvrtkaOsoba:
    def __init__ (self, ime, OIB, adresa, broj_djelatnika, pravni_oblik):
        self.ime = ime
        self.OIB = OIB
        self.adresa = adresa 
        self.broj_djelatnika = broj_djelatnika
        self.pravni_oblik = pravni_oblik

class DjelatnikOsoba:
    def __init__ (self, ime, OIB, adresa, radno_mjesto):
        self.ime = ime
        self.OIB = OIB
        self.adresa = adresa
        self.radno_mjesto = radno_mjesto
'''

# Sa nasljeđivanjem

class Tvrtka(Osoba):
    def __init__ (self, ime, OIB, adresa, broj_djelatnika, pravni_oblik):
        super().__init__(ime, OIB, adresa)
        self.broj_djelatnika = broj_djelatnika
        self.pravni_oblik = pravni_oblik

class Djelatnik(Osoba):
    def __init__ (self, ime, OIB, adresa, radno_mjesto):
        super().__init__(ime, OIB, adresa)
        self.radno_mjesto = radno_mjesto

t = Djelatnik('Hrvoje Horvat','1234567','Mala ulica 12','developer')
print(t.ime, t.OIB, t.adresa, t.radno_mjesto)

p = Tvrtka('Jedan','987654','Ulica 2', 12, 'd.o.o.')
print(p.ime, p.pravni_oblik, p.OIB, p.adresa)