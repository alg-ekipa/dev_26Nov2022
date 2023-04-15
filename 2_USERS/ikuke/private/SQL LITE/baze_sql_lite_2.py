import sqlite3


#kreiranje tablice unutar BAZE



# UPIT KOJIM KREIRAMO TABLICU - string u kojeg pišemo SQL kod
query_create='''CREATE TABLE IF NOT EXISTS Djelatnici
                (
                id INTEGER PRIMARY KEY,
                ime VARCHAR(30) NOT NULL,
                kontakt VARCHAR(20)
                ); '''

# varijabla s imenom baze
database_name = 'Tvrtka.db'



#upit koji dohvaća verziju sqllite modula

query_version= 'SELECT sqlite_version();'

try: #kreiramo konekciju prema bazi, ako baza ne postoji, kreirat će se
    sqlite_connection = sqlite3.connect(database_name)

    #kreiramo objekt cursor koji omogućava sve aktivnosti nad bazom

    cursor = sqlite_connection.cursor()
    print('baza je uspješno kreirana')

    # izvršavanje koda u SQL sintaksi koju smo spremili u varijablu query_version
    cursor.execute(query_create)
    sqlite_connection.commit() #dodatni korak
    print('kreirana je tablica djelatnici')


    #otpuštanje rseursa koje je zauzeo objekt cursor
    cursor.close()
    print ('resursi objekta cursor su uspješno otpušteni')


#ukoliko dođe do pogreške pri spajanju na bazu
except sqlite3.Error as e:
    print('pogreškas: ', e)


#zatvaranje konekcije prema bazi
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print('veza prema sql bazi je uspješno zatvorena')