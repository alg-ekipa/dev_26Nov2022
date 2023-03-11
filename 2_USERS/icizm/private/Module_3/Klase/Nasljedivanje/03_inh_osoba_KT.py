class Osoba: 
    def __init__(self, ime, oib, adresa): 
        self.ime = ime
        self.oib = oib
        self.adresa = adresa

# Bez nasljeđivanja
# da se nebi ponavljale iste stvari radi se nasljeđivanje
'''class TvrtkaOsoba: 
    def __init__(self, ime, oib, adresa, broj_djelatnika, pravni_oblik): 
        self.ime = ime
        self.oib = oib
        self.adresa = adresa
        self.broj_djelatnika = broj_djelatnika
        self.pravni_oblik = pravni_oblik


class DjelatnikOsoba: 
     def __init__(self, ime, oib, adresa, radno_mjesto): 
        self.ime = ime
        self.oib = oib
        self.adresa = adresa
        self.radno_mjesto = radno_mjesto
       
'''


# Prijenos svojstava i neka dodatna svojstva


class Tvrtka(Osoba): 
    def __init__(self, ime, oib, adresa, broj_djelatnika, pravni_oblik): #ostaju svi elementi ali se kroz super definira koje elemente uzimamo iz parent klase
        super().__init__(ime, oib, adresa)
        self.broj_djelatnika = broj_djelatnika
        self.pravni_oblik = pravni_oblik

class Djelatnik(Osoba): 
     def __init__(self, ime, oib, adresa, radno_mjesto): 
        super().__init__(ime, oib, adresa)
        self.radno_mjesto = radno_mjesto

d = Djelatnik('Hrešimir Horbat', '123456789', 'Ulična ulica 56', 'developer')
print(d.ime, d.oib, d.adresa, d.radno_mjesto)

t = Tvrtka('Tvrtkica', 'oibek12345', 'Tvrtkova ulica 7', 123, 'd.o.o.')
print(t.ime, t.oib, t.adresa, t.broj_djelatnika, t.pravni_oblik)

