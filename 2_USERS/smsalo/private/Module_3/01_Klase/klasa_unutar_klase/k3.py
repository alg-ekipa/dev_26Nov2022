class Student:
    def __init__(self, ime, mbr, dan, mjesec, godina):
        self.ime=ime
        self.mbr=mbr
        self.dat_rod=self.Datum_rodenja(dan, mjesec, godina)

    def ispisi(self):
        print(f'Ime: {self.ime}. MB: {self.mbr}')
        self.dat_rod.ispisi_1()

    class Datum_rodenja:
        def __init__(self, dan, mjesec, godina):
            self.dan=dan
            self.mjesec=mjesec
            self.godina=godina
        def ispisi_1(self):
            print(f'Dan: {self.dan} mjesec: {self.mjesec} godina: {self.godina}')

s1=Student('Krešo', '12345', 10, 12, 2000)
s1.ispisi()
