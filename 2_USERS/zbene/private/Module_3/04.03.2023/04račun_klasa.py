class Račun:
    def __init__ (self, broj, datum ,stavke, pdv = 0.25):
        self.broj = broj
        self.datum = datum
        self.stavke = stavke
        self.pdv = pdv
        self.ukupan_iznos = 0

        self.računaj_ukupan_iznos()

    def računaj_ukupan_iznos(self):
        for cijena in self.stavke.values():
            self.ukupan_iznos = self.ukupan_iznos + cijena

    def računaj_pdv (self, iznos):
        return iznos * self.pdv
    
    def ispiši_račun(self):
        print (self.broj)
        print (self.datum)
        print ('*'*35)
        print ('Proizvod\t\tCijena')

        for proizvod, cijena in self.stavke.items():
            print (f'{proizvod}\t\t\t{cijena}')
        print ('-'*35)
        print (f'UKUPNO:\t\t\t {self.ukupan_iznos + self.računaj_pdv (self.ukupan_iznos)}')
        print (f'PDV:\t\t\t {self.računaj_pdv(self.ukupan_iznos)}')

broj = 'R1-2023-01'
datum = '4.03.2023.'
stavke = {
    'Laptop' : 12000,
    'Monitor' : 2000,
    'Miš' : 100,
}

račun1 = Račun (broj, datum, stavke)
račun1.ispiši_račun()