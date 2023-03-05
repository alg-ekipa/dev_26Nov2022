class Racun():
    def __init__(self, broj, datum, stavke, pdv=0.25):
        self.broj = broj
        self.datum = datum
        self.stavke = stavke
        self.pdv = pdv
        self.ukupan_iznos = 0
            
        self.racunaj_ukupan_iznos()
        
    def racunaj_ukupan_iznos(self):
        for cijena in self.stavke.values():
            self.ukupan_iznos = self.ukupan_iznos + cijena
            
    
    def racunaj_pdv(self,iznos):
        return iznos * self.pdv
    
    
    def ispis_racun(self):
        print(self.broj)
        print(self.datum)
        print('*'*35)
        print('Proizvod\t\tCijena')
        for proizvod,cijena in self.stavke.items():
            print(f'{proizvod}\t\t\t{cijena}')
        print('-'*35)
        print(f'UKUPNO:\t\t\t{self.ukupan_iznos}')
        print(f'UKUPNO PDV:\t\t{self.ukupan_iznos + self.racunaj_pdv(self.ukupan_iznos)}')

        

def kreiraj_racun(brojac_racuna):
    racun_stavke = dict()
    racun_broj = f'R-{brojac_racuna}-2023'
    racun_datum = '4th Mar 2023'
    
    while True:
        proizvod = input("Unesi proizvod: ") 
        cijena = float(input("Unesi cijena: "))
        racun_stavke[proizvod] = cijena
        if not input("Nastavljamo sa stavkama (za NE pristisnite ENTER: "):
            break
        
    racun_objekt = Racun(racun_broj, racun_datum, racun_stavke) 
    return racun_objekt    


lista_objekata_racuna = []
brojac_r = 1

while True:
    racun = kreiraj_racun(brojac_r)
    brojac_r = brojac_r + 1
    lista_objekata_racuna.append(racun)
    
    if not input("Novi racun ili ENTER za izlaz."):
        break

for racun in lista_objekata_racuna:
    racun.ispis_racun()
    