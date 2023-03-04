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

        
def kreiranje_racuna(brojac_racuna, pdv):
    racun_stavke = {}
    racun_broj = f'R-{brojac_r}-2023'
    racun_datum = '04.03.2023.'

    while True:
        proizvod = input('Unesi proizvod: ')
        cijena = float('Unesi cijenu: ')
        racun_stavke[proizvod] = cijena
        if not input('Nastavljamo sa stavkama? (za NE pritisni enter)'):
            break

    racun_objekata_racuna = []
    brojac_r = 1

    while True:
        racun = kreiraj_racun(brojac_r)
        brojac_r += 1

        lista_objekata_racuna.append(racun)

        if not input ('Unesimo novi racun? ( NE - Enter)'):
            break

    kreirani_racun = kreiraj_racun(brojac_r, datum, PDV)

    brojac_r += 1
    racuni[racun_broj] = kreirani_racun



# varijable

racun1 = Racun(broj, datum, stavke)

racun1.ispisi_racuna()