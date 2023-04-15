import sqlite3

#čitanje i dohvat podataka iz tablice

#svi podaci

query_select_all= """ SELECT * FROM Djelatnici"""

#podaci s odredjenim IDom
query_select = """ SELECT * FROM Djelatnici
                    WHERE id=?"""

databese_name = "Tvrtka.db"

try:
    sql_conn = sqlite3.connect(databese_name)
    cursor = sql_conn.cursor()

    cursor.execute(query_select_all)
    records_all = cursor.fetchall()

    cursor.execute(query_select, (2,))
    record_2 = cursor.fetchall()

    #print(records_all)
    for record in records_all:
        print(record)
    
    print(record_2)

    cursor.close()

except sqlite3.Error as e:
    print("Pogreška", e)

finally:
    if sql_conn:
        sql_conn.close()
        print("Veza prema SQL bazi je uspješno zatvorena.")