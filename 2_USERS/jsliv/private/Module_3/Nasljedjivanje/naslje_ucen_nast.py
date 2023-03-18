#Napraviti klasu Osoba (parent) koju će nasljediti klase Ucenik i Nastavnik
#Neka se unose nekoliko učcenika i nastavnika preko tipkovnikce, kreiraju kao objekti, zati ju spremiti u listu
#Lista ucenici, nastavnici

class Osoba:
    def __init__(self, ime_prezime, adresa, svojstvo):
        self.ime_prezime = ime_prezime
        self. adresa = adresa
        self. svojstvo = svojstvo

class Ucenik:
    def __init__(self, ime_prezime, adresa, svojstvo, ocjena):
        super().__init__(ime_prezime, adresa, svojstvo)
        self.ocjena = ocjena
    
class Ucitelj:
    def __init__(self, ime_prezime, adresa, svojstvo, satnica):
        super().__init__(ime_prezime, adresa, svojstvo)
        self.satnica = satnica

ucenik =[]
while = True:
    


    