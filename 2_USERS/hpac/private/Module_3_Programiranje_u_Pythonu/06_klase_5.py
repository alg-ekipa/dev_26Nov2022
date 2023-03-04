# Iskoristite klasu Auto i instanciranje objekta
# Spremite ta 3 objketa u listu : lista_objekata_auto
# Dodajte u klasi metodu za ispis samo crvenih auta i pozovite ju

class Auto:
    def __init__(self, marka, model, godište, kilometri, boja, cijena):
        self.marka = marka
        self.model = model
        self.godište = godište
        self.kilometri = kilometri
        self.boja = boja
        self.cijena = cijena

    def ispisi(self):
        if self.boja == 'crvena':
            print(f'Auto marke {self.marka}, model {self.model} je {self.boja} boja')

    
auto1 = Auto('VW','Passat',2018,95000,'crvena',15000)
auto2 = Auto('Hyundai','Tucson',2014,186350,'srebrna',11630)
auto3 = Auto('Ford','Focus',2020,39500,'crvena',18600)

lista_objekata_auto = []        #može se ručno unijeti, budući da su već definirani

lista_objekata_auto.append(auto1)
lista_objekata_auto.append(auto2)
lista_objekata_auto.append(auto3)

for auto in lista_objekata_auto:
     auto.ispisi()

# ZADAĆA: prepravite da se objekti auti pune preko inputa u petjli, njima napunite listu(lista_objekata_auto), napraviti listu modela 