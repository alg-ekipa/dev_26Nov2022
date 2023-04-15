import sqlite3

#BRISANJE PODATAKA IZ TABLICE

query_delete='''DELETE FROM Djelatnici
                    WHERE id=?'''

database_name='Tvrtka.db'

try:
    sql_conn=sqlite3.connect(database_name)
    cursor=sql_conn.cursor()

    cursor.execute(query_delete, (2))
    sql_conn.commit()

    cursor.close()

except sqlite3.Error as e:
    print('Pogreška: ', e)

#zatvarnjee konekcije prema bazi
finally:
    if sql_conn:
        sql_conn.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')