class Student:
    def __init__(self, ime, mbr, dan, mjesec, godina):
        self.ime = ime
        self.mbr = mbr
        self.datum_rođ = self.Datum_rođenja(dan, mjesec, godina)
    
    def ispisi (self):
        print(f'Ime: {self.ime}, Matični broj: {self.mbr}')
        self.datum_rođ.prikazi()

    class Datum_rođenja:
        def __init__(self, dan, mjesec, godina):
            self.dan = dan
            self.mjesec = mjesec
            self.godina = godina

        def prikazi(self):
            print(f'Datum rođenja: {self.dan}.{self.mjesec}.{self.godina}.')

s1 = Student('Krešo', 22588, 10, 1, 1999)

s1.ispisi()