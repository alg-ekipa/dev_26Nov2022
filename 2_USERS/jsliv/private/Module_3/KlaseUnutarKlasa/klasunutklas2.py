class Student:
    def __init__(self, ime, oib, dan, mjesec, godina):
        self.ime = ime
        self.oib = oib
        self.datum_rodj = self.Datum_rodjenja(dan, mjesec, godina)

    
    def ispis(self):
        print(f"Ime: {self.ime}, osobni broj {self.oib}")
        self.datum_rodj.prikazi()

    class Datum_rodjenja:
        def __init__(self, dan, mjesec, godina):
            self.dan = dan
            self.mjesec = mjesec
            self.godina = godina

        def prikazi(self):
            print(f"Datum rodjenja {self.dan}.{self.mjesec}.{self.godina}.")
    

s1 = Student("Luka Lukic", 31542, 10, 5, 1983)
s1.ispis()


