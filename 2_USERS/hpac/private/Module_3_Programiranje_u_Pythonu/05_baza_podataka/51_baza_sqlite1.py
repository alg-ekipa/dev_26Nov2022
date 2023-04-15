import sqlite3

# upit koji dohvaća verziju SQLite3 modula

query_version = 'SELECT sqlite_version();'

try: 
    # kreiramo konekciju prema bazi, ako baza ne postoji kreirat će se
    sqlite_connection = sqlite3.connect('C:/Users/office10.UCIONE/Desktop/hp/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/05_baza_podataka/SQLite_probna.db')

    # kreiramo objekt cursor koji omogućava sve aktivnosti nad bazom
    cursor = sqlite_connection.cursor()

    # izvršavanje koda u SQL sintaksi kojeg smo spremili u varijablu query version
    cursor.execute(query_version)

    # dohvat svih podataka koji su rezultat upita
    version = cursor.fetchall()

    print('Verzija SQLite-a je', version)

    # otupuštanje resursa koje je zaueo objekt cursor
    cursor.close()
    print('Resursi objekta curos su uspješno otpušteni!')

# Ukoliko dođe do pogreške pri spajanju na bazu
except sqlite3.Error as e:
    print('Pogreška: ',e)

# zatvaranje konekcije prema bazi
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')