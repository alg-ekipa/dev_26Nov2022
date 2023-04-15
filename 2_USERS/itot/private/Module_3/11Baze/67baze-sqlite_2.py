import sqlite3

# KREIRANJE TABLICE UNUTAR BAZE

# UPIT KOJIM KREIRAMO TABLICU

query_create = ''' CREATE TAVLE ID NOT EXISTS Djelatnici
                    (
                    id INTEGER PRIMARY KEY,
                    ime TEXT NOT NULL,
                    kontakt TEXT NOT NULL
                    )'''

# varijabla s imenom baze
database_name = 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/11Baze/68Djelatnici.sql'

try:
    sql_connection = sqlite3.connect(database_name)
    cursor = sql_connection.cursor()
    print('Baza je uspjesno kreirana')

    coursor = sql_connection = sqlite3


    '''fali dio'''




    #ukoliko dođe do pogreške pri spajanju na bazu
except sqlite3.Error as e:
    print('Pogreška: ', e)

#zatvarnjee konekcije prema bazi
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')