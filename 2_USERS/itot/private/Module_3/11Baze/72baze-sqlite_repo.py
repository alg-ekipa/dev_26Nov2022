import sqlite3
from SQLite_repo import *

database_name = 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/11Baze/71Proizvodi.sql'



query_create = ''' Kreira novi red u tablici ZHaposlenici na osnovu podataka pohranjenih u djelatnik parametru'

                '''

try:
    sql_conn = sqlite3.connect(database_name)
    cursor = sql_conn.cursor()

    #                (naredba, ID)
    cursor.execute(query_delete, (2,))  
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