class Ucenik:
    def __init__(self, ime, prezime, ocjena):
        self.ime=ime
        self.prezime=prezime
        self.ocjena=ocjena

    def ispis(self):
        print(f'Ucenik: {self.ime} {self.prezime}, ocjena: {self.ocjena}')

# metoda za ispis ucenika koji imaju ocjenu 1

    def ispis_1(self):
        if self.ocjena==1:
            print(f'Ucenik {self.ime} {self.prezime} ima ocjenu 1')
            self.ispis()

lista_objekata_ucenika=[]
#unos 3 ucenika i pretvaranje našeg unosa u klasu ucenik
for i in range(3):
    ime_unos=input('Unesi ime: ')
    prezime_unos=input('Unesi prezime: ')
    ocjena_unos=input('Unesi ocjenu: ')

    ucenik_objekt = Ucenik(ime_unos, prezime_unos, ocjena_unos)
    lista_objekata_ucenika.append(ucenik_objekt)

#print(lista_objekata_ucenika)       #prikaz objekata nije vidljiv

for ucenik in lista_objekata_ucenika:  # lijepi ispis nasih unosa
    ucenik.ispis()
    ucenik.ispis_1()            #popravi, ne radi

    

