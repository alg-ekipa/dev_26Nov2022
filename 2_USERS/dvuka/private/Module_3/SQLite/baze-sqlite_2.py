import sqlite3

#KREIRANJE TABLICE UNUTAR BAZE

#upit kojim kreiramo tablicu-string u kji pišemo sql kod

query_create='''CREATE TABLE IF NOT EXISTS Djelatnici
                 (
                 id INTEGER PRIMARY KEY,
                 ime TEXT NOT NULL,
                 kontakt TEXT NOT NULL
                 ); '''
#varijbla s imenom baze
database_name='C:/Users/grafika10/Desktop/dev_26Nov2022-1/2_USERS/dvuka/private/Module_3/SQLite/Tvrtka.db'

try:
    sql_connection=sqlite3.connect(database_name)
    cursor=sql_connection.cursor()
    print('Baza je uspješno kreirana')

    cursor.execute(query_create)
    sql_connection.commit()     #dodatni korak 'potvrde' pri konekciji
    print('Kreirana je tablica Djelatnici!')

    cursor.close()
    print('Resursi objekta cursor su otpušteni')

except sqlite3.Error as e:
    print('Pogreška: ', e)

#zatvarnjee konekcije prema bazi
finally:
    if sql_connection:
        sql_connection.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')