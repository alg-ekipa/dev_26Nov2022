class Osoba:

    def __init__(self, ime, oib, adresa):
        self.ime=ime
        self.oib=oib
        self.adresa=adresa
'''
    #Bez nasljeđivanja
class TvrtkaOsoba:
    def __init__(self, ime, oib, adresa, broj_djelatnika, pravni_oblik):
        self.ime=ime
        self.oib=oib
        self.adresa=adresa
        self.broj_djelatnika=broj_djelatnika
        self.pravni_oblik=pravni_oblik

class DjelatnikOsoba:
    def __init__(self, ime, oib, adresa, radno_mjesto):
        self.ime=ime
        self.oib=oib
        self.adresa=adresa
        self.radno_mjesto=radno_mjesto
'''
class Tvrtka(Osoba):
    def __init__(self, ime, oib, adresa, broj_djelatnika, pravni_oblik):
        super().__init__(ime, oib,adresa)
        self.broj_djelatnika=broj_djelatnika
        self.pravni_oblik=pravni_oblik

class Djelatnik(Osoba):
    def __init__(self, ime, oib, adresa, radno_mjesto):
        super().__init__(ime, oib, adresa)
        self.radno_mjesto=radno_mjesto

t=Djelatnik('Hrvoje Horvat', '1234567','Velika ul.6','developer')
print(t.ime, t.oib, t.adresa, t.radno_mjesto)
p=Tvrtka('Py d.o.o.','33333','Uska 3', 100, 'd.o.o.')
print(p.ime ,p.pravni_oblik, p.adresa)
     