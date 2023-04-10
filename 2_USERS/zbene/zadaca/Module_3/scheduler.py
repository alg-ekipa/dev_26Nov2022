import datetime as dt

class Korisnik:
    def __init__(self, ime, email, mob):
        self.ime = ime
        self.email = email
        self.mob = mob
        self.sastanak = []

    def dodaj_sastanak (self, sastanak):
        self.sastanak.append(sastanak)

class Termin:
    def __init__(self, početak, kraj, napomena):
        self.početak = početak
        self.kraj = kraj
        self.napomena = napomena