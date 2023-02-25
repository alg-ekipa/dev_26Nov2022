#iskoristite klasu Auto i instanciranje tri objekta
#spremite ta tri objekata u listu lista_objekata_auto
#dodajte metodu za ispis samo crvenih auta i pozovite ju

class Auto():

    def __init__(self, marka, boja, model, motor):
        self.marka = marka
        self.boja = boja
        self.model = model
        self.motor = motor
    
    def ispisi(self):
        print(self.marka, self.boja, self.model, self.motor)
        print(f"Treci auto je {self.marka}{self.model} koji je {self.boja} i jacine motora {self.motor}.")

    def promjena_boje(self, nova_boja):
        self.boja = nova_boja

    def ispisi_crveni(self):
        if self.boja == "Crvena":
            self.ispisi()

auto1 = Auto("Audi", "Crna", "A3", "1.8 TDI")
auto2 = Auto("Audi", "Siva", "Q5", "3.0 TDI")
auto3 = Auto("Audi", "Crvena", "A1", "1,6 TDI")

lista_objekata_auto =[auto1, auto2, auto3]

for auto in lista_objekata_auto:
    auto.ispisi_crveni()

#prepravite da se objekti pune preko petlje, napunite listu, napravite listu modela