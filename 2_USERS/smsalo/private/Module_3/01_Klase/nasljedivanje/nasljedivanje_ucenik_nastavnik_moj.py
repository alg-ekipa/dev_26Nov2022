# napraviti klasu Osoba (parent) koju će naslijediti klase Učenik i Nastavnik
# neka se unose nekoliko učenika i nastavnika preko tipkovnice, kreiraju kao objekti i zatim spremaju u neku listu
# lista učenici i lista nastavnici

class Osoba:
    def __init__(self, ime, prezime, god_rod):
        self.ime=ime
        self.prezime=prezime
        self.god_rod=god_rod

    def ispis(self):
        print(self.ime, self.prezime, self.god_rod)

class Ucenik(Osoba):
    def __init__(self, ime, prezime, god_rod, razred):
        super().__init__(self, ime, prezime, god_rod)
        self.razred=razred

class Nastavnik(Osoba):
    def __init__(self, ime, prezime, god_rod, radno_mjesto):
        super().__init__(ime, prezime, god_rod)
        self.radno_mjesto=radno_mjesto

lista_ucenika=[]
lista_nastavnika=[]

while True:
    ime = input('Unesite ime učenika ')
    prezime = input('Unesite prezime učenika ')
    god_rod = input('Unesite godinu rođenja učenika ')
    razred = input('Unesite razred koji učenik pohađa ')
  
    lista_ucenika.append(Ucenik(ime, prezime, god_rod, razred))
    if input('Zelite li dodati učenika? (da/ne) ') != 'da':
        break

for ucenik in lista_ucenika:
    ucenik.ispis()
    
print()