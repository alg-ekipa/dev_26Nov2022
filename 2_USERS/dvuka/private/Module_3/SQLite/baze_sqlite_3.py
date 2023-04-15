import sqlite3

#DODAVANJE PODATAKA U BAZU

database_name='C:/Users/grafika10/Desktop/dev_26Nov2022-1/2_USERS/dvuka/private/Module_3/SQLite/Tvrtka.db'

query_insert__into_table='''INSERT INTO Djelatnici (ime, kontakt)
                                VALUES(?,?)
                        '''

djelatnici=[('Pero Perić','pperic@gmail.com'),('Marko Marković','marko@gmail.com'), ('Ana Anić', 'aanic@gmail.com')]

try:
    sql_conn=sqlite3.connect(database_name)
    cursor=sql_conn.cursor()

    for djelatnik in djelatnici:
        cursor.execute(query_insert__into_table, djelatnik)

    sql_conn.commit()

    cursor.close()

except sqlite3.Error as e:
    print('Pogreška: ', e)

#zatvarnjee konekcije prema bazi
finally:
    if sql_conn:
        sql_conn.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')