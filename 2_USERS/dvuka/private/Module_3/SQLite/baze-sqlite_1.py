import sqlite3

#upit koji dohvaća verziju SQLite3 modula
query_version='SELECT sqlite_version();'

try:
    #kreiramo konekciju prema bazi, ako baza ne postoji kreirat će se baza
    sqlite_connection=sqlite3.connect('SQLite:probna.db')
    #kreiramo objekt cursor koji omogućava sve aktivnosti nad bazom
    cursor=sqlite_connection.cursor()
    #izvršavanje koda u sql sintaksi kojeg smo spremili u varijablu query version

    cursor.execute(query_version)
    #dohvat svih podataka koji su rezultat upita

    version=cursor.fetchall()

    print('Verzija SQLite-a je', version)
    #otpuštanje resursa koje je nzauzeo objekt cursor

    cursor.close()
    print('Resursi objekta kursor su uspješno otpušteni!')

#ukoliko dođe do pogreške pri spajanju na bazu
except sqlite3.Error as e:
    print('Pogreška: ', e)

#zatvarnjee konekcije prema bazi
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')