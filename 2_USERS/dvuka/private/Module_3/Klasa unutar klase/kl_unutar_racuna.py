#Modificiramo program za generiranje i unos računa, tako da unutar klase Račun napravimo klasu Stavke

class Racun:
    def __init__(self, broj, datum, proizvod, cijena):
        self.broj=broj
        self.datum=datum
        self.stavka=self.Stavka(proizvod, cijena)

    def ispisi(self):
        print(f'Račun broj {self.broj}, Datum: {self.datum}')
        self.stavka.prikazi()

    def unesi_stavke(self):
        lista_objekata_stavki=[]
        while True:
            proizvod=input('Unesi proizvod: ')
            cijena=float(input('Unesi cijenu proizvoda: '))
            stavka_objekt=self.Stavka(proizvod, cijena)

            lista_objekata_stavki.append(stavka_objekt)

            odluka=input('Nastavljamo li s stavkama? da/ne: ')
            if odluka=='ne':
                break   

        return lista_objekata_stavki

    class Stavka:
        def __init__(self, proizvod, cijena):
            self.proizvod=proizvod
            self.cijena=cijena

        def prikazi(self):
            print(self.proizvod, self.cijena)

r=Racun(1,'1.1.2001.', '',1)
r.unesi_stavke()