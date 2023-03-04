class Racun:
    def __init__(self, broj, datum, stavke, pdv=0.25):
        self.broj = broj
        self.datum = datum
        self.stavke = stavke
        self.pdv = pdv
        self.ukupan_izos = 0

        self.racunaj_ukupan_izns()
    
    def racunaj_ukupan_izns(self):
        for cijena in self.stavke.values():
            self.ukupan_izos = self.ukupan_izos + cijena

    def racunaj_pdv(self, iznos):
        return iznos * self.pdv

    def ispisi_racuna(self):
        print(self.broj)
        print(self.datum)
        print("------------------")
        print("Proizvod\tCijena")
        for proizvod, cijena in self.stavke.items():
            print(f"{proizvod}\t\t{cijena}")

        print("-"*20)
        print(f"UKUPNO:\t\t\t{self.ukupan_izos + self.racunaj_pdv(self.ukupan_izos)}")
        print(f"PDV:\t\t\t{self.racunaj_pdv(self.ukupan_izos)}")

broj = "R1-202301"
datum = "4.03.2023."
stavke = {
    "Laptop": 12000,
    "Monitor": 2000,
    "Mis": 100,
    "Tipkovnica": 150
}

racun1 = Racun(broj, datum, stavke)

racun1.ispisi_racuna()