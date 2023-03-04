class Racun: 
    def __init__(self, broj, datum, stavke, pdv = 0.025):
        self.broj = broj
        self.datum = datum
        self.stavke = stavke
        self.pdv = pdv
        self.ukupan_iznos = 0 #ne prenosimo ga, on je nešto novo što se generira

        self.racunaj_ukupan_iznos()


    def racunaj_ukupan_iznos(self): 
        for cijena in self.stavke.values():
            self.ukupan_iznos = self.ukupan_iznos + cijena 

    def racunaj_PDV(self, iznos): #nad čime se računa PDV u zagradi
        return iznos * self.pdv 

    def ispisi_racun(self):
        print(self.broj)
        print(self.datum)
        print('*'*40)
        print('Proizvod \t\t Cijena')
        for proizvod,cijena in self.stavke.items():
            print(f'{proizvod} \t\t {cijena}')
            print('-'*40)
            print(f'Ukupno: \t\t\t{self.ukupan_iznos + self.racunaj_PDV(self.ukupan_iznos )}')
            print(f'PDV: \t\t\t\t{self.racunaj_PDV(self.ukupan_iznos)}')


broj = 'R1-2023-01'
datum = '04.03.2023.'
stavke = {
    'Laptop' : 12000, 
    'Monitor' : 2000, 
    'Miš' : 100, 
    'Tipkovnica' : 150
}

racun1 = Racun(broj, datum, stavke)

racun1.ispisi_racun()
