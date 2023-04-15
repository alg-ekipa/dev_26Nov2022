import sqlite3

# DODAVANJE PODATAKA U BAZU

database_name = 'C:/Users/office10.UCIONE/Desktop/hp/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/05_baza_podataka/Tvrtka.db'

query_insert_into_table = '''INSERT INTO  Djelatnici1 (ime, kontakt)
                                VALUES (?, ?)
                        '''

djelatnici = [('Pero Perić', 'pperic@mail.com'),('Marko Marković', 'marko@mail.com'),('Ana Anić','ana@mail.com')]

try:
    sql_conn = sqlite3.connect(database_name)
    cursor = sql_conn.cursor()
    
    for djelatnik in djelatnici:
        cursor.execute(query_insert_into_table, djelatnik)

    sql_conn.commit()

    cursor.close()

except sqlite3.Error as e:
    print('Pogreška: ',e)

finally:
    if sql_conn:
        sql_conn.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')