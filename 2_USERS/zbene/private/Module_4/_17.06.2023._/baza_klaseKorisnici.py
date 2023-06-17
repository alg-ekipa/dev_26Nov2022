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
                                slika BLOB);''')            #SLIKA OBLIKA BLOB U BAZI    

    def procitaj_sliku(self, slika_jpg):
        slika_blob=open(slika_jpg, "rb").read()     
        return slika_blob             
    
    def dodaj_korisnika(self, ime, prezime, OIB, slika):
        query_dodaj='''INSERT INTO Korisnici (ime, prezime, OIB, slika)
                        VALUES (?,?,?,?)'''
        slika=self.procitaj_sliku(slika)
        values=(ime, prezime, OIB, slika)
        self.cursor.execute(query_dodaj, values)
        self.connection.commit()

    def zatvori_konekciju(self):
        self.connection.close()


baza_objekt= BazaKorisnici('Korisnici_baza.db')     #ovim dijelom pozvat će se samo dio __init__ tj. otvorit će se konekcija
baza_objekt.kreiraj_tablicu()
baza_objekt.dodaj_korisnika('Jure', 'Juric', '123456789','C:/Users/Korisnik/Documents/San/dev_26Nov2022/2_USERS/smsalo/private\Module_3/11_klasa_nakon GUI/slika.jpg')
baza_objekt.zatvori_konekciju()


