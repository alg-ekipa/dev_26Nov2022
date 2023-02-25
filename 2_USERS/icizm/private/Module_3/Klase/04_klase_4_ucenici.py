class Ucenik: 
    def __init__(self, ime, prezime, ocjena):
        self.ime = ime
        self.prezime = prezime
        self.ocjena = ocjena
        
    def ispis(self): 
        print(f'Učenik: {self.ime} {self.prezime}, ocjena: {self.ocjena}')

    # metoda za ispis učenika koji imaju ocjenu 1

    def ispis_1(self): 
        if self.ocjena == 1: 
            print(f'Učenik {self.ime} {self.prezime} ima ocjenu 1')
            self.ispis() #možemo zvati metodu unutar metode - dodano kasnije

# unos 3 učenika i pretvaranje našeg unosa u objekt klase Ucenik
lista_objekata_ucenika = []
lista_ocjena =[]



for i in range(3): 
    ime_unos = input('Unesi ime učenika: ')
    prezime_unos = input('Unesi prezime učenika: ')
    ocjena_unos = int(input('Unesi ocjenu učenika: '))
    print()

    # kreiranje objekta
    ucenik_objekt = Ucenik(ime_unos, prezime_unos, ocjena_unos) 
    #treba ih staviti u listu

    # punimo listu objekata koju smo gore označili kao praznu
    lista_objekata_ucenika.append(ucenik_objekt)

#print(lista_objekata_ucenika)                       # prikaz objekata, nisu vidljivi detalji

for ucenik in lista_objekata_ucenika:                # svaki učenik je objekt koji povlači svoje parametre
    #ucenik.ispis()                                  # lijepi ispis naših unosa odnosno objekata u listi
    ucenik.ispis_1()
    lista_ocjena.append(ucenik.ocjena)

print(lista_ocjena)



