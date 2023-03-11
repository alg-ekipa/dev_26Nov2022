class Osoba: 
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime
        
    def ispis(self): 
        print(self.ime, self.prezime)

class Student(Osoba): 
    pass

class Umirovljenik(Osoba): 
    pass

osoba1 = Osoba('Petar', 'Pajdo')
osoba2 = Student('Marija', 'Marijić')
osoba3 = Umirovljenik('Vlatko', 'Vladimirović')

osoba1.ispis()
osoba2.ispis()
osoba3.ispis()