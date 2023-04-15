import sqlite3


#ČITANJE I DOHVAT PODATAKA IZ TABLICE

#svi podaci

query_select_all='''SELECT * FROM Djelatnici'''
query_select = '''SELECT * FROM Djelatnici
                    WHERE id=?'''



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
    cursor.execute(query_select_all)
    records_all=cursor.fetchall()
    
    cursor.execute(query_select, (2,))
    records_2=cursor.fetchall()


    print(records_all)
    print (records_2)

    #otpuštanje resursa koje je zauzeo objekt cursor
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