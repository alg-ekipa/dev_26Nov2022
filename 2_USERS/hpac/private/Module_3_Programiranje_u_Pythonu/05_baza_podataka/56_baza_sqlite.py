import sqlite3

# BRISANJE PODATAKA IZ TABLICE

query_delete = ''' DELETE FROM Djelatnici1
                    WHERE id=?
            '''

database_name = 'C:/Users/office10.UCIONE/Desktop/hp/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/05_baza_podataka/Tvrtka.db'

try:
    sql_conn = sqlite3.connect(database_name)
    cursor = sql_conn.cursor()

    cursor.execute(query_delete, (2,))
    sql_conn.commit()
    cursor.close()

except sqlite3.Error as e:
    print('Pogreška: ',e)

finally:
    if sql_conn:
        sql_conn.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')