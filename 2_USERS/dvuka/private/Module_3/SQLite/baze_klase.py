import sqlite3

class BazaKorisnici:
    def __init__(self, db_file):
        self.connection=sqlite3.connect(db_file)
        self.cursor=self.connection.cursor()


    #metode za aktivan rad s bazom(kreiranje, pisanje, brisanje, dodavanje)

    def kreiraj_tablicu(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS korisnici
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            ime TEXT, 
                            prezime TEXT,
                            OIB TEXT,
                            slika BLOB);''')
        
    def procitaj_sliku(self, slika_jpg):
        slika_blob=open(slika_jpg, "rb").read()
        return slika_blob
        
    def dodaj_korisnika(self, ime , prezime, oib, slika):
        query_dodaj='''INSERT INTO korisnici (ime, prezime, OIB, slika)
                        VALUES  (?,?,?,?)'''
        slika=self.procitaj_sliku(slika)
        values=(ime, prezime, oib, slika)
        self.cursor.execute(query_dodaj, values)
        self.connection.commit()

    def zatvori_konekciju(self):
        self.connection.close()

baza_objekt=BazaKorisnici('Korisnici_baza.db')
baza_objekt.kreiraj_tablicu()
baza_objekt.dodaj_korisnika('Jure', 'Juric', '12345678901','C:/Users/danij/Downloads/dev_26Nov2022/1_ALG/_vzbo_/m3_05_fotodatoteke/Algebra_greyp.jpg')
baza_objekt.zatvori_konekciju()