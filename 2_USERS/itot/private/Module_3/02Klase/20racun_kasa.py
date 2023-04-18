class Racun:
    def __init__(self, broj, datum, stavke, pdv=0.25):
        self.broj =  broj
        self.datum = datum
        self.stavke = stavke
        self.pdv = pdv
        self.ukupan_iznos = 0

    def racunaj_ukupan_iznos(self):  #nesto ne zbraja dobro
        for cijena in self.stavke.values():
            self.ukupan_iznos = self.ukupan_iznos + cijena


    def racunaj_pdv(self, iznos):
        return iznos * self.pdv

    def ispisi_racuna(self):
        print(self.broj)
        print(self.datum)
        print('-'*35)
        print('Proizvod\t\tCijena')
        for proizvod, cijena in self.stavke.items():
            print(f'{proizvod}\t\t\t{cijena}')
        print('-'*35)
        print(f'Ukupno:\t\t\t{self.ukupan_iznos + self.racunaj_pdv(self.ukupan_iznos)}')
        print(f'PDV:\t\t\t{self.racunaj_pdv(self.ukupan_iznos)}')





        
# varijable
broj = 'R1-2023-01'
datum = '04.03.2023.'
stavke = {
    'Laptop' : 12000,
    'Monitor' : 2000,
    'Miš' : 100,
    'Tipkov' : 1200

}

racun1 = Racun(broj, datum, stavke)

racun1.ispisi_racuna()