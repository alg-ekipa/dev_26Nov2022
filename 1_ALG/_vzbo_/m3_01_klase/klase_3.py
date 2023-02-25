# ZADATAK: 
# Izradite klasu Auto, u kojoj definirajte 4 svojstva i 2 metode: za ispis i bojanje auta
# Zatim instancirajte 3 objekta klase Auto, pozivajte metode za ispis i obojajte 2 auta po izboru

class Auto:
    def __init__(self, model, boja, proizvodac, godina):
        self.model = model
        self.boja = boja
        self.proizvodac = proizvodac
        self.godina = godina

    def ispis_podataka(self):
        print(f'Auto je {self.boja} {self.model}, iz godine {self.godina}')

    def obojaj(self, nova_boja):
        self.boja = nova_boja

auto1 = Auto('BMW 1M Coupe', 'crni', 'BMW', 2020)
auto2 = Auto('Clio','plavi','Renault', 2018)
auto3 = Auto('Astra', 'crveni', 'Opel', 2019)

auto1.ispis_podataka()
print(auto1.model, auto1.proizvodac, auto1.boja, auto1.godina)

auto3.obojaj("zelena")
print(f'Nova boja auta {auto3.model} je {auto3.boja}')


