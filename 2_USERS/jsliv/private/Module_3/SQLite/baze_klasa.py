import sqlite3


class BazaKorisnici:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def kreiraj_tablicu(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS korisnici
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            ime TEXT,
                            prezime TEXT,
                            OIB TEXT,
                            slika BLOB);""" )
    
    def procitaj_sliku(self, slika_jpg):
        slika_blob = open(slika_jpg, "rb").read()
        return slika_blob
    
    def dodaj_korisnika(self, ime, prezime, oib, slika):
        query_doday = """INSERT INTO korisnici (ime, prezime, OIB, slika)
                        VALUES (?, ?, ?, ?)"""
        slika = self.procitaj_sliku(slika)
        values = (ime, prezime, oib, slika)
        self.cursor.execute(query_doday, values)
        self.connection.commit()

    def zatovori_konekciju(self):
        self.connection.close()

baza_objekt = BazaKorisnici("Korisnici_baza.db")
baza_objekt.kreiraj_tablicu()
baza_objekt.dodaj_korisnika("Jure", "Jurić", "123456789", "C:/Users/JulijanaS/Desktop/VisualStudioCode/dev_26Nov2022-1/2_USERS/jsliv/private/Module_3/Photo/Algebra_campus.jpg")
baza_objekt.zatovori_konekciju()