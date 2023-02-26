class Učenik:
    def __init__(self, ime, prezime, ocjena):
        self.ime = ime
        self.prezime = prezime
        self.ocjena = ocjena
    
    def ispis(self):
        print(f' Učenik: {self.ime} {self.prezime}, ocjena: {self.ocjena}')

    # metoda za ispis učenika koji imaju ocjenu 1
    def ispis_1(self):
        if self.ocjena == 1:
         #   print(f'Učenik {self.ime} {self.prezime} ima ocjenu 1!!')
            self.ispis()


lista_objekata_ucenika = []
lista_ocjena =  []

#Unos 3 učeniak i pretvaranje našeg unosa u objekt klase Učenik
for i in range(3):
    ime_unos = input('Unesi ime učenika: ')
    prezime_unos = input('Unesi prezime učenika: ')
    ocjena_unos = int(input('Unesi ocjenu: '))
    print()

    #kreiranje objekata
    ucenik_objekt = Učenik(ime_unos, prezime_unos, ocjena_unos)

    #punimo listu objekata, koju smo gore označili kao praznu
    lista_objekata_ucenika.append(ucenik_objekt)

#print(lista_objekata_ucenika) #prikaz objekata, nisu vidljivi detalji


#prolazak kroz listu objekata, nad svakim objektom radimo posebno
for ucenik in lista_objekata_ucenika:
    #ucenik.ispis()      #lijepi ispis naših unosa objekata u listi
    ucenik.ispis_1()       # ispi učeika koji imaju keca
    lista_ocjena.append(ucenik.ocjena)

print(lista_ocjena)