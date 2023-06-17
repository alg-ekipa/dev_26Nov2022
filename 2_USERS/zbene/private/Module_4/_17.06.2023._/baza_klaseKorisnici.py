import sqlite3

class BazaKorisnici:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    #metode za aktivan rad s bazom (kreiranje, pisanje, brisanje,...)

    def kreiraj_tablicu(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Korisnici
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                ime TEXT,
                                prezime TEXT,
                                OIB TEXT,
                                );''')            
        
    def dodaj_korisnika (self, ime, prezime, OIB):
        query_dodaj='''INSERT INTO Korisnici (ime, prezime, OIB, slika)
                        VALUES (?,?,?,?)'''
        values=(ime, prezime, OIB)
        self.cursor.execute(query_dodaj, values)
        self.connection.commit()

    def obriši_korisnika (self, OIB):
        pass

    def ažuriraj_korisnika (self, OIB):
        pass

    def zatvori_konekciju(self):
        self.connection.close()


baza_objekt= BazaKorisnici('Korisnici_baza.db')     #ovim dijelom pozvat će se samo dio __init__ tj. otvorit će se konekcija
baza_objekt.kreiraj_tablicu()
baza_objekt.zatvori_konekciju()