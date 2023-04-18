# Iskoristite klasu Auto i instanciranje 3 objekta
# spremite ta 3 objekta u listu: lista_objekata_auto
# dodajte u klasi metodu za ispis samo crvenih auta i pozovite ju 

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

    def ispisi_crveni(self):
        if self.boja == 'crveni':
            self.ispis_podataka()


auto1 = Auto('BMW 1M Coupe', 'crni', 'BMW', 2020)
auto2 = Auto('Clio','plavi','Renault', 2018)
auto3 = Auto('Astra', 'crveni', 'Opel', 2019)

lista_objekata_auti = [auto1, auto2, auto3]

print(lista_objekata_auti)

for auto in lista_objekata_auti:
    auto.ispis_podataka()
    #auto.ispisi_crveni()

# TO DO: prepravite da se objekti auti pune preko inputa u petlji, njima napunite listu (lista_objekata_auti), napravite listu modela 
