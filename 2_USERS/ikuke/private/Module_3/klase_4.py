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

auto1=input_automobila()
auto2=input_automobila()
auto3=input_automobila()

print (auto1.proizvodac)
print (auto2.proizvodac)
print (auto3.proizvodac)



auto1.ispis()
auto2.ispis()
auto3.ispis()


auto1.promijeni_boju()

auto1.ispis()

os.system('cls')


lista_objekata=[]
for i in range(3):
    proizvodac= input ('Unesi proizvodaca automobila:')
    model = input ('Unesi model automobila:')
    auto_objekt= Automobili(model,proizvodac)
    lista_objekata.append(auto_objekt)

for ucenik in lista_objekata:
    ucenik.ispis()

