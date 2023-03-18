#Zadatak
#izradite klasu Auto u kojoj definirajte 4 svojstva i 2 metode: za ispis i bojanje auta
#Zatim instancirajte 3 objekta klase Auto, pozivajte metode za ispis i obojajte 2 auta po izboru

class Auto:

    def __init__(self, marka, model, boja, cijena):
        self.marka=marka
        self.model=model
        self.boja=boja
        self.cijena=cijena

    def ispis(self):
        print(f'Automobil {self.marka},model{self.model} {self.boja}boje, sa cijenom od {self.cijena} eura')

    def obojaj(self, nova_boja):
        self.boja=nova_boja

Auto1=Auto('Fiat', 'Punto', 'Crna', 2000)
Auto2=Auto('Opel', 'Vectra', 'Crvena', 3000)
Auto3=Auto('Chevrolet', 'Aveo', 'Žuta', 4000)
Auto4=Auto('Ford','Focus','Plava', 5000)


#TO DO prepraviti da se objekti auti pune preko inputa u petlji, njima napnite listu(lista_objekata auti), napravite listu modela


