import sqlite3

# DODAVANJE PODATAKA U BAZU

# varijabla s imenom baze
database_name = 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/11Baze/68Djelatnici.sql'


query_inesert_into_table = ''' INSERT INTO Djelatnici (ime, kontakt)
                                    VALUES (?,?)
                        '''

djelatnik = ('Pero Paric', 'pero.peric@gmail.com')

try:
    sql_conn = sqlite3.connect(database_name)
    cursor = sql_conn.cursor()

    #                (naredba, podatci)
    cursor.execute(query_inesert_into_table, djelatnik)

    sql_conn.commit()

    cursor.close()

#ukoliko dođe do pogreške pri spajanju na bazu
except sqlite3.Error as e:
    print('Pogreška: ', e)

#zatvarnjee konekcije prema bazi
finally:
    if sql_conn:
        sql_conn.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')