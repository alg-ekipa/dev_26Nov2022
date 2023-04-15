import sqlite3

# ČITANJE I DOHVAT podataka iz tablice

# svi podaci
query_select_all = '''SELECT * FROM Djelatnici1'''

#podaci s određenim ID-em
query_select =  '''SELECT * FROM Djelatnici1
                    WHERE id=?'''

database_name = 'C:/Users/office10.UCIONE/Desktop/hp/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/05_baza_podataka/Tvrtka.db'

try:
    sql_conn = sqlite3.connect(database_name)
    cursor  =sql_conn.cursor()

    cursor.execute(query_select_all)
    records_all = cursor.fetchall()
    
    cursor.execute(query_select, (2,))
    records_2 = cursor.fetchall()

    #print(records_all)
    for record in records_all:
        print(record)
    print(  )
    print(records_2)

except sqlite3.Error as e:
    print('Pogreška: ',e)

finally:
    if sql_conn:
        sql_conn.close()
        print('Veza prema SQL bazi je uspješno zatvorena!')