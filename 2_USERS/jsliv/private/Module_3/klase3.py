# Zadatak
# Izradite klasu Auto u kojoj definirate 4 svojstva i 2 metode za ispis i promjenu boje
# instanciranje 3 objekata klase Auto, pozivanje metode za ispis i objajte auto

class Auto():

    def __init__(self, marka, boja, model, motor):
        self.marka = marka
        self.boja = boja
        self.model = model
        self.motor = motor
    
    def ispisi(self):
        print(self.marka, self.boja, self.model, self.motor)
        print(f"Treci auto je {self.marka} {self.model} koji je {self.boja} i jacine motora {self.motor}.")

    def promjena_boje(self, nova_boja):
        self.boja = nova_boja

auto1 = Auto("Audi", "Crna", "A3", "1.8 TDI")
auto2 = Auto("Audi", "Siva", "Q5", "3.0 TDI")
auto3 = Auto("Audi", "Crvena", "A1", "1,6 TDI")


auto1.ispisi()
print()

auto2.promjena_boje("bijela")
print(f"Automobilu Audi Q5 pogrešno je upisana boja, ispravna je {auto2.boja}")
print()

auto3.ispisi()
print()

#pogledaj ispise, ide duplo. Malo podesiti

