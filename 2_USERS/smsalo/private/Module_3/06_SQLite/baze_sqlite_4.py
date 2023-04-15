import sqlite3
# ČITANJE I DOHVAT PODATAKA IZ TABLICE

# svi podaci

query_select_all = '''SELECT * FROM Djelatnici'''

#podaci s određenim id
query_select = '''SELECT * FROM Djelatnici
                    WHERE id=?'''

database_name = 'Tvrtka.db'

try:
    sql_connect = sqlite3.connect(database_name)
    cursor = sql_connect.cursor()

    cursor.execute(query_select_all)
    record_all = cursor.fetchall()

    cursor.execute(query_select, (2,))
    record2=cursor.fetchall()

    #print(record_all)  ili kroz petlju da je preglednije
    for record in record_all:
        print(record)

    print(record2)
    
    cursor.close()

except sqlite3.Error as e:
    print('Pogreška: ', e)

#zatvaranje konekcije prema bazi
finally:
    if sql_connect:
        sql_connect.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')
