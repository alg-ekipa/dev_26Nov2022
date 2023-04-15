import sqlite3

# kreiranje tablice unutar baze
# upit kojim kreiramo tablicu

query_create = '''CREATE TABLE IF NOT EXISTS Djelatnici
                    (
                    id INTEGER PRIMARY KEY,
                    ime VARCHAR(50) NOT NULL,
                    kontakt VARCHAR(150) NOT NULL
                    );'''

database_name = 'Tvrtka.db'
try:
    sql_connection = sqlite3.connect(database_name)
    cursor = sql_connection.cursor()
    print('Baza je uspješno kreirana!')

    cursor.execute(query_create)
    sql_connection.commit()         #dodatni korak potvrde pri konekciji
    print('kreirana je tablica Djelatnici!')

    cursor.close()
    print('Resursi objekta cursor su otpuštni!')

except sqlite3.Error as e:
    print('Pogreška: ', e)

#zatvaranje konekcije prema bazi
finally:
    if sql_connection:
        sql_connection.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')


