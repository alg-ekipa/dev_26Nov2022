import sqlite3

#dodavanje podataka u bazu

database_name = 'Tvrtka.db'

query_insert_into_table = '''INSERT INTO Djelatnici (ime, kontakt)
                                VALUES (? , ?)
                                '''
djelatnici=[('Pero Peric', 'pperic@mail.com'), ('Iva Ivic', 'iva@mail.com'), ('Kiki Kikic', 'kikic@mail.com')]

try:
    sql_connect = sqlite3.connect(database_name)
    cursor = sql_connect.cursor()

    for djelatnik in djelatnici:
        cursor.execute(query_insert_into_table, djelatnik)

    sql_connect.commit()

    cursor.close()

except sqlite3.Error as e:
    print('Pogreška: ', e)

#zatvaranje konekcije prema bazi
finally:
    if sql_connect:
        sql_connect.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')
