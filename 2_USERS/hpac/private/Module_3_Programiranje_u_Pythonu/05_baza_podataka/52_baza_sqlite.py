import sqlite3

# KREIRANJE TABLICE UNUTAR BAZE

# Upit kojim kreiramo tablicu - string u kojeg pišemo SQL kod

query_create = '''CREATE TABLE IF NOT EXISTS Djelatnici1
                    (
                    id INTEGER PRIMARY KEY,
                    ime VARCHAR(30) NOT NULL,
                    kontakt VARCHAR(20)
                    );'''

# varijable s imenom baze
database_name = 'C:/Users/office10.UCIONE/Desktop/hp/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/05_baza_podataka/Tvrtka.db'

try:
    sql_connection = sqlite3.connect(database_name)
    cursor = sql_connection.cursor()
    print('Baza je uspješno kreirana')

    cursor.execute(query_create)
    sql_connection.commit()             # dodatni korak 'potvrde' pri konekciji
    print('Kreirana je tablica Djelatnici!')

    cursor.close
    print('Resursi objekta cursor su otpušteni')

except sqlite3.Error as e:
    print('Pogreška: ',e)

finally:
    if sql_connection:
        sql_connection.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')