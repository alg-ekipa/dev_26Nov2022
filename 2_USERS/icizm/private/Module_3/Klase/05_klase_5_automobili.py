# Iskoristite klasu Auto i instanciranje 3 objekta 
# spremite ta 3 objekta u listu lista_objekata_auto
# dodajte u klasi metodu za ispis samo crvenih auta i pozovite ju

class Auto(): 
    def __init__(self, marka, boja, vlasnik, registracija):
        self.marka = marka
        self.boja = boja
        self.vlasnik = vlasnik
        self.registracija = registracija

    def promjena_boje(self, nova_boja): 
        self.boja = nova_boja

    def ispis(self): 
        #print(self.marka, self.boja, self.vlasnik, self.registracija)
        print(f'Vlasnik {self.marka} automobila je {self.vlasnik}. Boja automobila je {self.boja}. Registracija automobila je: {self.registracija}.')

    def ispis_crvenih(self): 
        if self.boja == 'crvena': 
            print(f'Boja {self.marka} automobila čiji je vlasnik {self.vlasnik}, je crvena.')

automobil1 = Auto('Škoda', 'crvena', 'Mirjana Mirić', 'ZD3456PL')
automobil2 = Auto('Audi', 'roza', 'Marjan Marijančević', 'MA3456OK')
automobil3 = Auto('Citroen', 'žuta', 'Jelena Jelić', 'PŽ9485GH')

lista_objekata_automobili = [automobil1, automobil2, automobil3]

for auto in lista_objekata_automobili: 
    auto.ispis_crvenih()

# TO DO: prepravite da se objekti auti pune preko inputa u petlji, njima napunite listu (lista_objekata_auti=, napravite listu modela)
