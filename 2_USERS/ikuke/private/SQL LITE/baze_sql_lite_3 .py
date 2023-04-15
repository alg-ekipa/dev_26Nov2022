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



#DODAVANJE PODATAKA U BAZU

query_insert_into_table = '''INSERT INTO Djelatnici (ime, kontakt)
                                VALUES (?,?)

                            '''


djelatnik = [('Pero Perić', 'pperic@mail.com'), ('marko markić', 'mmarkic@mail.com')]


#upit koji dohvaća verziju sqllite modula

query_version= 'SELECT sqlite_version();'

try: #kreiramo konekciju prema bazi, ako baza ne postoji, kreirat će se
    sqlite_connection = sqlite3.connect(database_name)

    #kreiramo objekt cursor koji omogućava sve aktivnosti nad bazom

    cursor = sqlite_connection.cursor()
    print('baza je uspješno kreirana')

    # izvršavanje koda u SQL sintaksi
    cursor.execute(query_insert_into_table, djelatnik)
    sqlite_connection.commit() #dodatni korak
    print('dodani su podaci u tablicu')


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