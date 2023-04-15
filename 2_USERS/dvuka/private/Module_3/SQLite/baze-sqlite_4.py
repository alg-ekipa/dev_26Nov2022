import sqlite3

#ČITANJE I DOHVAT PODATAKA IZ TABLICE

#svi podaci

query_select_all='''SELECT * FROM Djelatnici'''
query_select='''SELECT * FROM Djelatnici
                    WHERE ID=?'''

database_name='C:/Users/grafika10/Desktop/dev_26Nov2022-1/2_USERS/dvuka/private/Module_3/SQLite/Tvrtka.db'

try:
    sql_conn=sqlite3.connect(database_name)
    cursor=sql_conn.cursor()

    cursor.execute(query_select_all)
    records_all=cursor.fetchall()

    cursor.execute(query_select, (2,))
    record_2=cursor.fetchall()

    #print(records_all)
    for record in records_all:
        print(record)

    print(record_2)

    cursor.close()

except sqlite3.Error as e:
    print('Pogreška: ', e)

#zatvarnjee konekcije prema bazi
finally:
    if sql_conn:
        sql_conn.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')