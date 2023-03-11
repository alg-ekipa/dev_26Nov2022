class Osoba:
    def __init__(self, ime, oib, adresa):
        self.ime = ime
        self.oib = oib
        self.adresa = adresa

#bez nasljedjivanja
"""
class TvrtkaOsoba:
    def __init__(self, ime, oib, adresa, broj_djelatnika, pravni_oblik):
        self.ime = ime
        self.oib = oib
        self.adresa = adresa
        self.broj_djelatnika = broj_djelatnika
        self.pravni_oblik = pravni_oblik


class DjelanikOsoba:
    def __init__(self, ime, oib, adresa, radno_mjesto):
        self.ime = ime
        self.oib = oib
        self.adresa = adresa
        self.radno_mjesto = radno_mjesto
"""
class Tvrtka(Osoba):
     def __init__(self, ime, oib, adresa, broj_djelatnika, pravni_oblik):
         super().__init__(ime, oib, adresa)
         self.broj_djelatnika = broj_djelatnika
         self.pravni_oblik = pravni_oblik

class Djelatnik(Osoba):
    def __init__(self, ime, oib, adresa, radno_mjesto):
        super().__init__(ime, oib, adresa)
        self.radno_mjesto = radno_mjesto

d = Djelatnik("Luka Lukić", "12345678", "Zagrebačka 5", "Developer")
print(d.ime, d.oib, d.adresa, d.radno_mjesto)
p = Tvrtka("Sunset", "987654331", "Dalmatinska 6", "7", "D.o.o.")
print(p.ime,p.oib, p.adresa, p.broj_djelatnika, p.pravni_oblik)


