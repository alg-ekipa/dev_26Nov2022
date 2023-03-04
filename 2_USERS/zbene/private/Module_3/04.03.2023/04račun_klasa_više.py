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

def kreiraj_račun (brojač_računa):
    račun_stavke = {}
    račun_broj = f'R-1-{brojač_računa}-2023'
    račun_datum = '04.03.2023.'
    
    while True:
        proizvod = input ('Unesi proizvod: ')
        cijena = float (input ('Unesi cijenu: '))
        račun_stavke[proizvod] = cijena
        if not input ('Nastavljamo sa stavkama? Za prekid pritisnite ENTER: '):
            break
    
    račun_objekta = Račun(račun_broj, račun_datum, račun_stavke)
    return račun_objekta

lista_objekata_računa = []
brojač_r =1

while True:
    račun = kreiraj_račun(brojač_r)
    brojač_r +=1

    lista_objekata_računa.append(račun)

    if not input ('Unosimo novi račun? Za prekid pritisnite ENTER: '):
        break