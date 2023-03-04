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
        print()
        print()
    

def kreiraj_racun(brojac_racuna): 
    racun_stavke = {}

    racun_broj = f'R-{brojac_racuna}-2023'
    racun_datum = '01.06.2023.'

    while True: 
        proizvod = input('Unesi proizvod: ')
        cijena = float(input('Unesi cijenu: '))
        racun_stavke[proizvod] = cijena
        if not input('nastavljamo sa stavkom? Ako NE pritisnite Enter   '): 
            break

    racun_objekt = Racun(racun_broj, racun_datum, racun_stavke)
    return racun_objekt

lista_objekata_racuna = []
brojac_r = 1

while True: 
    racun = kreiraj_racun(brojac_r)
    brojac_r += 1

    lista_objekata_racuna.append(racun)

    if not input('Unosimo novi račun? (NE = Enter)  '): 
        break


#nad svakim računom ćemo pozivati funkciju ispiši

for racun in lista_objekata_racuna: 
    racun.ispisi_racun()

