# Napraviti klasu Osoba (parent) koju će naslijediti klase Ucenik i Nastavnik.
# Neka se unose nekoliko učenika i nastavnika preko tipkovnice, kreiraju kao objekti, a zatim spreme u neku listu 
# lista_ucenici i lista_nastavnici


class Osoba:
    def __init__(self,ime):
        self.ime = ime
class Ucenik(Osoba):
    def __init__(self,ucenik):
        super().__init__(ime)
        self.ucenik = ucenik
class Nastavnik:
    def _init__ (self,profesor):
        self.profesor = profesor
    
