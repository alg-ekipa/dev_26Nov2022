class Osoba:                     #parent klasa

    def __init__(self,ime, prezime):
        self.ime = ime
        self.prezime = prezime

    def ispis(self):              #metoda prikaz info
        print(self.ime, self.prezime)

class Student(Osoba):
    pass

class Umirovljenik(Osoba):
    pass

osoba1 = Osoba('Pero', 'Peric')
osoba2 = Student('Mirko', 'Mirkic')
osoba3 = Umirovljenik('Jozo','Jozic')

osoba1.ispis()
osoba2.ispis()
osoba3.ispis()


