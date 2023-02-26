import os

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


   
def input_automobila():
    model=input('unesi model:')
    proizvodac=input('unesi proizvodaca:')
    return Automobili(model,proizvodac)

os.system('cls')

lista_automobila=[]

lista_objekata=[]
for i in range(3):
    proizvodac= input ('Unesi proizvodaca automobila:')
    model = input ('Unesi model automobila:')
    auto_objekt= Automobili(model,proizvodac)
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

print('ukupan broj automobila je', broj_bijelih_automobila)


for auto in lista_automobila:
    if auto.boja=="bijela":
        print(auto.model)
