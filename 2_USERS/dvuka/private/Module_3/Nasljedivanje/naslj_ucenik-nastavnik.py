#Napraviti klasu Osoba(parent) koju će naslijediti klase Učenik i Nastavnik
#Neka se unose nekoliko učenika i nastavnika preko tipkovnice, kreieraju kao objekt, a zatim spreme u neku listu
#lista _ucenici_ i lista_nastavnici

class Osoba:
    def __init__(self, ime, prezime):
        self.ime=ime
        self.prezime=prezime

class Ucenik(Osoba):
    def __init__(self, ime, prezime):
        super().__init__(ime, prezime)


class Nastavnik(Osoba):
    def __init__(self, ime, prezime):
        super().__init__(ime, prezime)

lista_ucenici=[]
lista_n