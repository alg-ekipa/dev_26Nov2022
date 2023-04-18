# ZADAĆA: prepravite da se objekti auti pune preko inputa u petjli, njima napunite listu(lista_objekata_auto), napraviti listu modela 

class Auto():
    def __init__(self, marka, model, godište, boja):
        self.marka = marka
        self.model = model
        self.godište = godište
        self.boja = boja

    def ispis(self):
        print(f'Auto marke {self.marka} model {self.model}, {self.boja} boja je iz {self.godište}. godine')

    

lista_objekata_auto = []
lista_modela = []
broj_auta = int(input('Koliko auta hoćeš unijeti: '))

for i in range(broj_auta):
    marka = input(f'Unesi marku {i+1}. vozila: ')
    model = input(f'Unesi model {i+1}. vozila: ')
    godište = input(f'Unesi godište {i+1}. vozila: ')
    boja = input(f'Unesi boju {i+1}. vozila: ')
    print()

    auto = Auto(marka, model, godište, boja)

    lista_objekata_auto.append(auto)
    lista_modela.append(model)

print(lista_modela)


for auto in lista_objekata_auto:
    auto.ispis()


