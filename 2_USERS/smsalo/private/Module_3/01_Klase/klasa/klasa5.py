#iskoristite klasu Auto i instancirajte 3 objekta
#spremite ta 3 objekta u listu: lista_objekata_auto
# dodajte u klasi metodu za ispis samo crvenih automobila i pozovite ju


class Auto:
    def __init__(self, marka, tip, boja, vrsta_goriva):
        self.marka=marka
        self.tip =tip
        self.boja =boja
        self.vrsta_goriva=vrsta_goriva

    def ispis(self):
        print(f'Automobil:{self.marka} {self.tip}, boja: {self.boja}')

    def ispisi_crveni(self):
        if self.boja == 'crveni':
            self.ispis()   

lista_automobila=[]
for i in range(3):
    auto_marka=input('Unesite marku automobila:')
    auto_tip=input('Unesite tip marke automobila: ')
    auto_boja=input('Unesite boju automobila: ')
    auto_vrsta_goriva=input('Unesite vrstu goriva: ')

    automobil=Auto(auto_marka, auto_tip, auto_boja, auto_vrsta_goriva)
    lista_automobila.append(automobil)

for vozilo in lista_automobila:  # lijepi ispis nasih unosa
    vozilo.ispis()
    vozilo.ispisi_crveni()
   

#TO DO: prepravite da se objekti pune preko inputa petljim njime napunite listu, napravite listu modela

