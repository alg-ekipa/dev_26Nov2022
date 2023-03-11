#modificiramo pgoram za generiranje i unos računa, tako da unutar klase Račun napravimo klasu Stavke

class Račun:
    def __init__ (self, broj, datum, proizvod, cijena):
        self.broj = broj
        self.datum = datum
        self.stavka = self.Stavka(proizvod, cijena)

    def ispiši (self):
        print (f'Račun broj {self.broj}, Datum: {self.datum}')
        self.stavka.prikaži()

    def unesi_stavke (self):
        lista_objekata_stavki = []
        ukupna_cijena = 0
        while True:
            proizvod = input ('Unesi proizvod: ')
            cijena = float (input('Unesi cijenu proizvoda: '))
            stavka_objekt = self.Stavka(proizvod, cijena)
            lista_objekata_stavki.append(stavka_objekt)
            
            odluka = input ('Nastavlja se ukoliko se ne upiše ne: ')
            if odluka == 'ne':
                break

        return lista_objekata_stavki

    class Stavka:
        def __init__ (self, proizvod, cijena):
            self.proizvod = proizvod
            self.cijena = cijena

        def prikaži (self):
            print(self.proizvod, self.cijena)

r = Račun (1, '01.01.2001', '', 1)
r.unesi_stavke()