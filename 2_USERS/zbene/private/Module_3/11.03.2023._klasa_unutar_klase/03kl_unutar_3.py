class Student:
    def __init__ (self, ime, MB, dan, mjesec, godina):
        self.ime = ime
        self.MB = MB
        self.dat_rođ = self.Datum_rođenja(dan, mjesec, godina)

    def ispiši (self):
        print (f'Ime: {self.ime}, MB: {self.MB}')
        self.dat_rođ.prikaži()

    class Datum_rođenja:
        def __init__ (self, dan, mjesec, godina):
            self.dan = dan
            self.mjesec = mjesec
            self.godina = godina

        def prikaži (self):
            print (f'Datum rođenja: {self.dan}.{self.mjesec}.{self.godina}.')

s1 = Student('Krešo', 3144, 10, 12, 2000)
s1.ispiši()