# Modificiramo program za generiranje i unos racuna, tako da unutar klase Racun napravimo klsau Stavke

class Racun:
    def __init__(self, broj, datum, proizvod, cijena):
        self.broj = broj
        self.datum = datum
        self.stavka = self.Stavke(proizvod, cijena)

    def ispis(self):
        print(f"Račun broj {self.broj}, datum {self.datum}")
        self.stavka.prikaz()

    def unos_stavki(self):
        lista_objekata_stavki = []
        while True:
            proizvod = input("Unesi proizvod: ")
            cijena = float(input("Unesi cijenu: "))
            stavka_objekt = self.Stavke(proizvod, cijena)
            lista_objekata_stavki.append(stavka_objekt)
            odluka = input("Nastavljas unos DA/NE: ")

            if odluka == "NE":
                break
            
        return lista_objekata_stavki

    
    class Stavke:
        def __init__(self, proizvod, cijena):
            self.proizvod = proizvod
            self.cijena = cijena
        
        def prikaz(self):
            print(self.proizvod, self.cijena)

r = Racun(1, "2.1.2023", " ", " 1")
r.unos_stavki()
            