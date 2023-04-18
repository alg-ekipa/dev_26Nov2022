class Student:
    def __init__(self, ime, mbr, dan, mjesec, godina):
        self.ime = ime
        self.mbr = mbr
        self.datum_rodj = self.Datum_rodjenja(dan, mjesec, godina)

    def ispisi(self):
        print(f'Ime: {self.ime}, Matični broj: {self.mbr}')
        self.datum_rodj.prikazi()

    class Datum_rodjenja:
        def __init__(self, dan, mjesec, godina):
            self.dan = dan
            self.mjesec = mjesec
            self.godina = godina

        def prikazi(self):
            print(f'Datum rođenja: {self.dan}.{self.mjesec}.{self.godina}.')

s1 = Student('Krešo',3144, 10, 12, 2000)

s1.ispisi()  # ispis svega
s1.datum_rodj.prikazi()     # ispis samo datuma rođenja
    