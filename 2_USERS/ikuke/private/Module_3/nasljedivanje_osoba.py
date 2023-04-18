

class Osoba:

    def __init__(self,ime,prezime):
        self.ime = ime
        self.prezime=prezime
    
    def ispis(self):
        print(self.ime, self.prezime)

   

class Student(Osoba):
    pass

class Umirovljenik(Osoba):
    pass

class Djelatnik(Osoba):
    pass


class Tvrtka(Osoba):
    def __init__(self, ime,oib, adresa, broj_djelatnika, pravni_oblik):
        super().__init__(ime, oib, adresa)
        self.broj_djelatnika = broj_djelatnika
        self.pravni_oblik=pravni_oblik
        
class Djelatnik(Osoba):
    def __init__(self, ime, oib, adresa, radno_mjesto):
        super().__init__(ime, oib, adresa)
        self.radno_mjesto=radno_mjesto

osoba1 = Student("igor","kukec")

osoba2 = Umirovljenik("pero","peric")

osoba1.ispis()


t= Djelatnik("Hrvoje Horvat" , 1234567, "Velika ul 6", "developer")
print (t.ime)
p=Tvrtka ("Py", "333333", "Uska 3", 100, "d.o.o.")
print (p.ime, p.broj_djelatnika, p.pravni_oblik)
