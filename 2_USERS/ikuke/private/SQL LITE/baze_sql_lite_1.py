import sqlite3

#upit koji dohvaća verziju sqllite modula

query_version= 'SELECT sqlite_version();'

try: #kreiramo konekciju prema bazi, ako baza ne postoji, kreirat će se
    sqlite_connection = sqlite3.connect('SQLite_probna.db')

    #kreiramo objekt cursor koji omogućava sve aktivnosti nad bazom

    cursor = sqlite_connection.cursor()


    # izvršavanje koda u SQL sintaksi koju smo spremili u varijablu query_version
    cursor.execute(query_version)

    #dohvat svih podataka koji su rezultat upita/querija
    version=cursor.fetchall()

    print ('verzija SQLitea je', version)

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