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
    def __init__ (self, starost, visina, težina, razred):
        super().__init__ (starost, visina, težina)
        self.razred = razred
        
    def ispis (self):
        print()
        print(self.starost)
        print(self.visina)
        print(self.težina)
        print(self.razred)

class Nastavnik (Osoba):
    def __init__(self, starost, visina, težina, lokacija_rada):
        super().__init__ (starost, visina, težina)
        self.lokacija_rada = lokacija_rada

    def ispis (self):
        print()
        print(self.starost)
        print(self.visina)
        print(self.težina)
        print(self.lokacija_rada)

lista_učenici = []
while True:
    starost = input ('Unesi starost Osobe: ')
    visina = input ('Unesi visinu Osobe')
    težina = input ('Unesi težinu Osobe')
    razred = input ('Unesi razred Osobe')

    lista_učenici.append (Učenik(starost, visina, težina, razred))
    
    if input ('Za prekid dodavanja odaberite bilo što izuzev' 'ne') !='ne':
        break
    
for učenik in lista_učenici:
    učenici.ispis()

lista_nastavnici = []

#### dovršiti zadatak 8/8 na 03 predavanje, zadnja str