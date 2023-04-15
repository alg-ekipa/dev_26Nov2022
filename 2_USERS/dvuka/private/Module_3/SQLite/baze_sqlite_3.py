import sqlite3

#DODAVANJE PODATAKA U BAZU

database_name='Tvrtka.db'

query_insert__into_table='''INSERT INTO Djelatnici (ime, kontakt)
                                VALUES(?,?)
                        '''

djelatnik=('Pero Perić','pperic@gmail.com')

try:
    sql_conn=sqlite3.connect(database_name)
    cursor=sql_conn.cursor()

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