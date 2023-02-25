# Zadatak: 
# Izradite klasu Auto, u kojoj definirajte 4 svojstva i 2 metode: za ispis i bojenje auta
# Zatim instancirajte 3 objekta klase Auto, pozivajte metode za ispis i obojajte 2 auta po izboru

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

automobil1 = Auto('Škoda', 'zelena', 'Mirjana Mirić', 'ZD3456PL')
automobil2 = Auto('Audi', 'roza', 'Marjan Marijančević', 'MA3456OK')
automobil3 = Auto('Citroen', 'žuta', 'Jelena Jelić', 'PŽ9485GH')

# print(f'Vlasnik {automobil1.marka} automobila je {automobil1.vlasnik}. Boja automobila je {automobil1.boja}. ')

automobil1.ispis()
automobil1.promjena_boje('narančasta')
automobil1.ispis()

# print(f'Vlasnik {automobil1.marka} automobila je {automobil1.vlasnik}. Boja automobila je {automobil1.boja}. ')
      



        
