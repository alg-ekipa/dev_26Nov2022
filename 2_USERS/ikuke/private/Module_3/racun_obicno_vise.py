class Racun:
    def __init__(self, broj, datum, stavke, pdv=0.25):
        self.broj = broj
        self.datum=datum
        self.stavke=stavke
        self.pdv=pdv
        self.ukupan_iznos=0

        self.racunaj_ukupan_iznos()

    def racunja_ukupan_iznos()
        for cijena in self.stavke.values():
            self.ukupan_iznos=self.ukupan_iznos + cijena

    def racunaj_pdv (self, iznos):
        return iznos * self.pdv

    def ispisi_racun(self):
        print(self.broj)


def kreiraj_racun(brojac_racuna, datum,  pdv):

    stavke = {}

    while True:
        proizvod = input('Unesi proizvod: ')
        cijena = float(input('Unesi cijenu proizvoda: '))
        stavke[proizvod] = cijena
        if not input('Unos nove stavke? Za NE pritisnite Enter  '):
            break

    return stavke

brojac_r = 1
PDV = 0.25
datum = '4.03.2023.'

racuni = {}

while True:
    kreirani_racun = kreiraj_racun(brojac_r, datum, PDV)
    racun_broj = f'R-{brojac_r}-2023'
    brojac_r +=1
    racuni[racun_broj] = kreirani_racun

    if not input('Želite li novi račun? (Enter ako NE)  '):
        break

for rbr,racun in racuni.items():
    print(rbr, racun)

