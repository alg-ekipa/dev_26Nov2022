#Napraviti klasu Osoba (parent) koju će naslijediti klase Učenik i Nastavnik
#Neka se unose nekoliko učenika i nastavnika preko tipkovnice, kreiraju kao objekti, a zatim spreme u neku listu
#lista_učenici i lista_nastavnici

class Osoba:
    def __init__ (self, starost, visina, težina):
        self.starost = starost
        self.visina = visina
        self.težina = težina
    def ispis (self):
        print()
        print(self.starost)
        print(self.visina)
        print(self.težina)
    
class Učenik (Osoba):
    def __init__ (self):
        super().__init__ (starost, visina, težina)
        učenici = input ('Unesi učenika: ')


class Nastavnik (Osoba):
    def __init__(self):
        super().__init__ (starost, visina, težina)

lista_učenici = []

while True:

lista_nastavnici = []