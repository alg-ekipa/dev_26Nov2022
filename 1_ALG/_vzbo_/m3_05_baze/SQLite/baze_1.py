import sqlite3

# DOHVAĆANJE VERZIJE SQLITE

query_version = 'SELECT sqlite_version();'

try:
    # kreiranje konekcije prema bazi, navodimo ime baze, ako ne postoji, kreirat će se
    sqliteConnection = sqlite3.connect('SQLite_Py.db')

    # kreiranje objekta cursor koji je zaužen za sve aktivnosti prema bazi
    cursor = sqliteConnection.cursor()
    print('Baza je uspješno kreirana i spojeni smo na SQLite')

    # izvršavanje SQL koda koji je pripremljen u varijabli query_version 
    cursor.execute(query_version)

    # dohvat svih podataka koji su rezultat upita
    version = cursor.fetchall()
    print('SQLite verzija je ', version)

    # otpuštanje resursa koje je zauzeo objekt cursor
    cursor.close()
    print('Resursi cusor objekta uspješno su otpušteni!')

except sqlite3.Error as e:
    print(f'Dogodila se pogreška prilikom spajanja na SQLite: {e}')

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite konekcija je uspješno zatvorena!')