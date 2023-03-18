Class Student:
    def __int__(self, ime, mbr):
        self.ime = ime
        self.ime = mbr
        self.datum_rodj = self.Datum_rodenja(mjesec, dan, godina)

    def ispis(self):
        print(f'Ime: {self.ime}, Maticni broj: {self.mbr}')

    class Datum_rodenja:
        def __init__(self, dan, mjesec, godina):
            self.dan = dan
            self.mjesec = godina
            self.godina = godina
        
        def ispis(self):
            print('Datum rodenja: ')
