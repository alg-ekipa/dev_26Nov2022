class Ucenik:
    def __init__(self, ime, prezime, ocjena):
        self.ime = ime
        self.prezime = prezime
        self. ocjena = ocjena
    
    def ispis(self):
        print(f"Ucenik: {self.ime} {self.prezime} ima ocjenu {self.ocjena}.")
    
    #Metoda za ispis ucenika koji imaju ocjenu 1

    def ispis_1(self):
        if self.ocjena == 1:
            print(f"Ucenik {self.ime} {self.prezime} ima ocjenu 1.")

lista_objekata_ucenika = []
lista_ocjena = []
#Unos 3 ucenika i pretvaranje našeg unosa u objekt klase Ucenik

for i in range(3):
    ime_unos = input("Unesi ime učenika: ")
    prezime_unos = input("Unesi prezime ucenika: ")
    ocjena_unos = int(input("Unesi ocjenu: "))
    print()

    ucenik_objekt = Ucenik(ime_unos, prezime_unos, ocjena_unos)

    lista_objekata_ucenika.append(ucenik_objekt)

#print(lista_objekata_ucenika) #prikazi objekata nisu vidljivi tj. detalji

#prolaz kroz listu objekata
for ucenik in lista_objekata_ucenika:
    #ucenik.ispis()       #cijelokupan ispis unosa odnosno objekata u listi
    ucenik.ispis_1()
    lista_ocjena.append(ucenik.ocjena)
print(lista_ocjena)



      