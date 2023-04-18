#ZADATAK
#izradite klasu Auto, u kojoj def 4 svojstva i 2 metode za ispis i bojanje automobila
#Zatim inicirajte 3 objekta klase auto, pozivajte metode za ispis i obojajte 2 auta

class Auto():
    def __init__(self, marka, tip, boja, vrsta_goriva):
        self.marka= marka
        self.tip = tip
        self.boja = boja
        self.vrsta_goriva=vrsta_goriva
    
    def bojanje(self, nova_boja):
        self.boja = nova_boja
    
    def ispisi(self):
        print(f'Automobil marke {self.marka} je tipa {self.tip} {self.boja} boja, vrsta motora {self.vrsta_goriva}')

auto1= Auto('Toyota', 'Yaris', 'plava', 'hibrid')
auto2=Auto('VW', 'Polo', 'bijela', 'disel')
auto3=Auto('Renault', 'Clio', 'zelena', 'benzin')

auto1.bojanje('crvena')
auto2.bojanje('crna')

auto1.ispisi()
auto2.ispisi()
auto3.ispisi()
