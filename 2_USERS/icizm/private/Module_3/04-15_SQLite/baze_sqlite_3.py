import sqlite3

# DODAVANJE PODATAKA U BAZU

database_name = 'Tvrtka.db'

query_insert_into_table = ''' INSERT INTO Djelatnici (ime, kontakt)
                            VALUES (? , ?)'''

djelatnici = [('Pero Perić','pperic@mail.com'),('Marko Markito','mmarkito@mail.com'),('Antonije Antislav','aantislav@mail.com')] # radi appendanje u tablicu

try: 
    sql_conn = sqlite3.connect(database_name)
    cursor = sql_conn.cursor()

    for djelatnik in djelatnici:
        cursor.execute(query_insert_into_table, djelatnik)

    sql_conn.commit()

    cursor.close()

except sqlite3.Error as e: 
    print('Pogreška', e)

# zatvaranje konekcije prema bazi
finally: 
    if sql_conn: 
        sql_conn.close
        print('Veza prema SQL bazi je uspješno zatvorena!')
   
