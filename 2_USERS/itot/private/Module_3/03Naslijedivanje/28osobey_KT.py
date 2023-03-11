class  Osoba:
    def __init__(self, ime, oib, adresa):
        self.ime = ime  
        self.oib = oib  
        self.adresa = adresa  



'''
# bez nasljeđivanja
class  TvrtkaOsoba:
    def __init__(self, ime, oib, adresa, broj_djelatnika, pravni_oblik):
        self.ime = ime  
        self.oib = oib  
        self.adresa = adresa  
        self.broj_djelatnika = broj_djelatnika 
        self.pravni_oblik = pravni_oblik 

class  TvrtkaOsoba:
    def __init__(self, ime, oib, adresa, radno_mjesto):
        self.ime = ime  
        self.oib = oib  
        self.adresa = adresa  
        self.radno_mjesto = radno_mjesto
'''

# sa nasljeđivanjem, skrati kod

class Tvrtka(Osoba):
    def __init__ (self, ime, oib, adresa, broj_djelatnika, pravni_oblik):
        super().__init__(ime, oib, adresa)     # nasljeduje iz perent klase
        self.broj_djelatnika = broj_djelatnika
        self.pravni_oblik = pravni_oblik

class Djelatnik(Osoba):
    def __init__ (self, ime, oib, adresa, radno_mjesto):
        super().__init__(ime, oib, adresa)     # nasljeduje iz perent klase
        self.radno_mjesto = radno_mjesto


d = Djelatnik('Mirko Mirkic', '123345456', 'Velika u1.6', 'developer')
print(d.ime, d.oib, d.adresa, d.radno_mjesto)    
t = Tvrtka('PyP', '1233453425', 'Ulica 4', 100, 'd.o.o.')
print(t.ime, t.oib, t.adresa ,t.broj_djelatnika, t.pravni_oblik)  