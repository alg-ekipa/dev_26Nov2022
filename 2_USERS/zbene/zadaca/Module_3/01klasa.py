#Iskoristite klasu Auto i instanciranje 3 objekta
#spremite ta 3 objekta u listu: lista_objekata_auto
#dodajte u klasi metodu za ispis samo crvenih auta i pozovite ju

#prepraviti da se objekti auti pune preko inputa u ptelji, njima napunite listu (lista_objekata_auti), napravite listu modela

class Auto:
    def __init__(self, marka, model, kw, ccm, boja='bez boje'):
        self.marka = marka
        self.model = model
        self.kw = kw
        self.ccm = ccm
        self.boja = boja

    def promijeni_boju (self):
        željena_boja = input ('Upiši željenu boju automobila: ')
        print(f'Auto marke {self.marka} je promijenio boju u {željena_boja}.')

    def ispiši(self):
        print (f' Auto marke {self.marka} i modela {self.model} ima {self.kw} kw i {self.ccm} ccm te je {self.boja}')

auto1 = Auto ('Fiat', 'Fićo', 69, 999,)
auto2 = Auto ('Peugeot', 'Pežić', 55, 1.199)
auto3 = Auto ('Opel', 'Opelić', 66, 1.499)

auto1.ispiši()
auto2.ispiši()
auto3.ispiši()

auto2.promijeni_boju(željena_boja)
auto3.promijeni_boju(self)