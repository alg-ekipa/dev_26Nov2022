import sqlite3

# KREIRANJE TABLICE UNUTAR BAZE

# Upit kojim kreiramo tablicu - string u kojeg pišemo SQL kod

query_create = ''' CREATE TABLE IF NOT EXISTS Djelatnici 
                    (
                    id INTEGER PRIMARY KEY,
                    Ime VARCHAR(30) NOT NULL,
                    kontakt VARCHAR(30)
                    ); '''


# Varijabla s imenom baze 
database_name = 'Tvrtka.db'

try: 
    sql_connection = sqlite3.connect(database_name)
    cursor = sql_connection.cursor()
    print('Baza je uspješno kreirana.')

    cursor.execute(query_create)
    # kad kreiramo TABLICU potrebna je još jedan dodatni korak potvrde pri konekciji
    sql_connection.commit()
    print('Kreirana je tablica Djelatnici.')

    cursor.close()
    print('Resursi objekta cursor su otpušteni.')

except sqlite3.Error as e: 
    print('Pogreška', e)

# zatvaranje konekcije prema bazi
finally: 
    if sql_connection: 
        sql_connection.close
        print('Veza prema SQL bazi je uspješno zatvorena!')

# Tablica se ne vidi dok ne stavimo u nju podatke