#ZADATAK
# Izradite klasu Auto, u kojoj doefinirate 4 svojstva i 2 metode: za ispis i bojanje auta
# instancirajte 3 objekta klase Auto, pozivajte metode za ispis i obojajte 2 auta po izboru


class Auto:
    def __init__(self, marka, model, godište, kilometri, boja, cijena):
        self.marka = marka
        self.model = model
        self.godište = godište
        self.kilometri = kilometri
        self.boja = boja
        self.cijena = cijena

    def ispisi(self):
        print(f'Auto marke {self.marka}, model {self.model} - {self.boja} boja - proizveden {self.godište}. godine boje prešao je {self.kilometri}km košta {self.cijena}€')

    def bojanje(self, nova_boja):
        self.boja = nova_boja

auto1 = Auto('VW','Passat',2018,95000,'crna',15000)
auto2 = Auto('Hyundai','Tucson',2014,186350,'srebrna',11630)
auto3 = Auto('Ford','Focus',2020,39500,'crvena',18600)
auto4 = Auto('Toyota','Corolla',2017,43700,'plava',13300)

auto1.ispisi()
auto2.ispisi()
auto3.ispisi()

auto2.bojanje('žuta')
print(f'{auto2.marka} {auto2.model} je obojan te je sada {auto2.boja} boje')

        