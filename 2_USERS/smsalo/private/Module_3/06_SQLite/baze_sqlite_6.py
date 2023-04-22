import sqlite3

#BRISANJE

query_delete = '''DELETE FROM Djelatnici 
                    WHERE id=?'''

database_name='Tvrtka.db'

try:
    sql_connect = sqlite3.connect(database_name)
    cursor = sql_connect.cursor()

    cursor.execute(query_delete, (5,))
    sql_connect.commit()

    cursor.close()

except sqlite3.Error as e:
    print('Pogreška: ', e)

#zatvaranje konekcije prema bazi
finally:
    if sql_connect:
        sql_connect.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')
