class Racun:
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

    def racunaj_pdv(self, iznos):
        return iznos * self.pdv

    def ispisi_racun(self):
        print(self.broj)
        print(self.datum)
        print("------------------")
        print("Proizvod\tCijena")
        for proizvod, cijena in self.stavke.items():
            print(f"{proizvod}\t\t{cijena}")

        print("-"*20)
        print(f"UKUPNO:\t\t\t{self.ukupan_iznos + self.racunaj_pdv(self.ukupan_iznos)}")
        print(f"PDV:\t\t\t{self.racunaj_pdv(self.ukupan_iznos)}")
    
def kreiraj_racun(brojac_racuna):   #Izvan klase!!!
    racun_stavke = {}

    racun_broj = f"R-{brojac_racuna}-2023"
    racun_datum = "4.03.2023."

    while True:
        proizvod = input("Unesi cijenu: ")
        cijena = float(input("Unesi cijenu: "))
        racun_stavke[proizvod] = cijena   #punjenje riječnika
        if not input("Nastavljamo sa stavkama? Ako NE Enter."):
            break

    racun_objekt = Racun(racun_broj, racun_datum, racun_stavke)
    return racun_objekt

lista_objekata_racuna = []
brojac_r = 1

while True:
    racun = kreiraj_racun(brojac_r)
    brojac_r += 1

    lista_objekata_racuna.append(racun)

    if not input ("Unosimo novi racun? NE - enter "):
        break

for racun in lista_objekata_racuna:
    racun.ispisi_racun()

