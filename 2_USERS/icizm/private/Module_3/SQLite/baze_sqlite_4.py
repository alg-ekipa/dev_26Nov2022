import sqlite3

# ČITANJE I DOHVAT PODATAKA IZ TABLICE

# Svi podaci

query_select_all_data = ''' SELECT * FROM Djelatnici'''

# Podaci s određenim ID-em 

query_select = ''' SELECT * FROM Djelatnici
                    WHERE id=?'''

database_name = 'Tvrtka.db'

try: 
    sql_conn = sqlite3.connect(database_name)
    cursor = sql_conn.cursor()

    cursor.execute(query_select_all_data)
    records_all = cursor.fetchall()

    cursor.execute(query_select, (2,))
    record_2 = cursor.fetchall()

    # print(records_all) - ispiše cijelu listu pa smo to stavili tako da ispiše u obliku ntorki jedne ispod drugih: 

    for record in records_all: 
        print(record)

    print(record_2)

    cursor.close()

except sqlite3.Error as e: 
    print('Pogreška', e)

# zatvaranje konekcije prema bazi
finally: 
    if sql_conn: 
        sql_conn.close
        print('Veza prema SQL bazi je uspješno zatvorena!')