# Napraviti klase Osoba(parent), koju ćenasljediti klase Učenik i Nastavnik
# Neka se unose nekoliko učenika i nastavnika preko tipkovnice, kreiraju kao objekti, a zatim spreme u neku lisu
# lista_ucenici i lista_nastavnici

class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime

    
class Nastavnik(Osoba):
    def __init__(self, ime, prezime, predmet):
        super().__init__(ime, prezime)
        self.predmet = predmet

class Učenik(Osoba):
    def __init__(self, ime, prezime, razred):
        super().__init__(ime, prezime)
        self.razred = razred

lista_nastavnici = []
lista_učenici =  []

while True:
    ime = input('Unesite ime nastavnika: ')
    prezime = input('Unesite prezime nastavnika: ')
    predmet = input('Unesite koji predmet nastavnik predaje: ')

    lista_nastavnici.appena(Nastavnik(ime, prezime, predmet))
    
    