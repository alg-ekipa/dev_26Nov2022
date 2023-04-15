import sqlite3

# ČITANJE I DOHVAT PODATAKA IZ TABLICE

# varijabla s imenom baze
database_name = 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/11Baze/68Djelatnici.sql'

# svi podatci
query_select_all = '''SELECT * FROM Djelatnici'''

# svi podatci
query_select = '''SELECT * FROM Djelatnici
                        WERE ID=?'''

try:
    sql_conn = sqlite3.connect(database_name)
    cursor = sql_conn.cursor()

    #                (naredba)
    cursor.execute(query_select_all) 
    records_all = cursor.fetchall() # dohvat svih zapisa

    #print(records_all)
    for record in records_all:
        print(record)

    cursor.close()

#ukoliko dođe do pogreške pri spajanju na bazu
except sqlite3.Error as e:
    print('Pogreška: ', e)

#zatvarnjee konekcije prema bazi
finally:
    if sql_conn:
        sql_conn.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')


        ### fALI DIO