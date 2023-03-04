import os
# izrada objekata iz liste

vozni_park = {
    1: ['kamion', 'Iveco', 'ZG 1234 IK', 2005, 45000],
    2: ['kombi', 'Iveco', 'ZG 1234 AK', 2015, 45000],
    3: ['dostavno vozilo', 'Fiat', 'ZG 1234 IK', 2015, 45000],
    4: ['automobil', 'Fiat', 'ZG 1234 IK', 2015, 45000],
    5: ['automobil', 'Fiat', 'ZG 1234 IK', 2015, 45000],
    3: ['dostavno vozilo', 'Opel', 'ZG 1234 IK', 2022, 45000]
}

class bcolors:
    ZELENO = '\033[92m'
    ZUTO = '\033[93m'
    CRVENO = '\033[91m'
    KRAJ = '\033[0m'

class Automobili():
    #konstruktor je metoda koja se zove __init__(initializacija)

    def __init__(self,model,proizvodac, boja="bijela", gorivo='nema', godina_proizvodnje="nepoznato",potrosnja="nepoznata"):
        self.model = model
        self.proizvodac=proizvodac
        self.gorivo=gorivo
        self.godina_proizvodnje=godina_proizvodnje
        self.potrosnja=potrosnja
        self.boja=boja
    

    def ispis(self):
        print('proba')
        print(f"model automobila: {self.model}, proizvođača: {self.proizvodac}, godine proizvodnje {self.godina_proizvodnje},ima boju: {self.boja}")

    def promijeni_boju(self):
        input()

        os.system('cls')
        print(self.proizvodac,self.model)
        boja=input('Unesi željenu boju automobila: ')
        print("stara boja automobila je", self.boja, "nova boja automobila je: ", boja)

        self.boja=boja


    def ispis_dostavnih_vozila(self):
        print('------------------------------------------ispis_dostavnih_vozila--------------------------------------------')
        if self.model =="dostavno vozilo":
            print(f"model automobila: {self.model}, proizvođača: {self.proizvodac}, godine proizvodnje {self.godina_proizvodnje},ima boju: {self.boja}")


   
    def input_automobila():
        model=input('unesi model:')
        proizvodac=input('unesi proizvodaca:')
        return Automobili(model,proizvodac)

os.system('cls')

lista_automobila=[]

lista_objekata=[]
for i in range(5):
    #proizvodac= input ('Unesi proizvodaca automobila:')
    #model = input ('Unesi model automobila:')
    vozilo=vozni_park[i+1]
    auto_objekt= Automobili(vozilo[0],vozilo[1], "bijela", "diesel", vozilo[4])
    lista_objekata.append(auto_objekt)



lista_automobila=lista_objekata


for auto in lista_automobila:
    auto.ispis()


#auto1.promijeni_boju()


os.system('cls')
broj_bijelih_automobila=0

for auto in lista_automobila:
    if auto.boja=="bijela":
        broj_bijelih_automobila+=1
    print(broj_bijelih_automobila)

print('ukupan broj bijelih automobila je', broj_bijelih_automobila)


for auto in lista_automobila:

    auto.ispis_dostavnih_vozila()
