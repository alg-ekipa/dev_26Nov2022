class Racun:
    def __init__(self, broj, datum, stavke, pdv=0.25):
        self.broj = broj
        self.datum = datum
        self.stavke = stavke
        self.pdv = pdv
        self.ukupan_iznos = 0

        self.računaj_ukupan_iznos()

    def računaj_ukupan_iznos(self):
        for cijena in self.stavke.values():
            self.ukupan_iznos = self.ukupan_iznos + cijena
    
    def racunaj_pdv(self,iznos):
        return iznos * self.pdv

    def ispisi_racun(self):
        print()
        print(self.broj)
        print(self.datum)
        print('-'*25)
        print('Proizvod\tCijena')
        for proizvod,cijena in self.stavke.items():
            print(f'{proizvod}\t\t{cijena}')
        print('*'*25)
        print(f'UKUPNO:\t\t{self.ukupan_iznos + self.racunaj_pdv(self.ukupan_iznos)}')
        print(f'PDV:\t\t{self.racunaj_pdv(self.ukupan_iznos)}')

def kreiraj_racun(brojac_racuna):
    racun_stavke = {}
    racun_broj = f'R-{brojac_racuna}-2023'
    racun_datum = '4.3.2023.'

    while True:
        proizvod =input('Unesite proizvod: ')
        cijena = float(input('Unesi cijenu: '))
        racun_stavke[proizvod] = cijena
        if not input ('Nastavljamo sa unosom stavki? (Ako NE pritisni ENTER)  '):
            print()
            break
    
    racun_objekt = Racun(racun_broj, racun_datum, racun_stavke)
    return racun_objekt

lista_objekata_racuna = []
brojac_r = 1

while True:
    racun = kreiraj_racun(brojac_r)
    brojac_r += 1
    lista_objekata_racuna.append(racun)

    if not input('Unosimo novi račun? (Ako NE pritisni ENTER)  '):
        print()
        break

for racun in lista_objekata_racuna:
    racun.ispisi_racun()