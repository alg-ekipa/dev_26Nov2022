import sqlite3

#Upit koji dohvaća verziju sqlite3 modula

query_version = "SELECT sqlite_version();"

try:
#kreiranje konekcije prema bazi, ako baza ne postoji kreirati će se
    sqlite_connection = sqlite3.connect("SQLite_probna.db")
#kreiramo objekt cursor koji omogućava sve aktivnosti nad bazom
    cursor = sqlite_connection.cursor()
#izvršavanje koda u sql sintaxi kojeg smo spremili u varijablu query_version
    cursor.execute(query_version)
#dohvat svih zadataka koji su rezultat upita
    version = cursor.fetchall()

    print("Verzija SQLita je", version)
#otpuštaje resursa koje je zauzeo objekt cursor
    cursor.close()
    print("Resurs objekta cursor su uspješno otpušteni.")

except sqlite3.Error as e:
    print("Pogreška", e)

finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Veza prema SQL bazi je uspješno zatvorena.")


