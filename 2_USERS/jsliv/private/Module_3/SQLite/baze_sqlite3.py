import sqlite3
#Dodavanje podataka u bazu

database_name = "Tvrtka.db"

query_insert_into_table = """ INSERT INTO Djelatnici (ime, kontakt)
                                VALUES (? , ? )
                        """
#Ako želimo više djelatnika radimo listu
djelatnici = [("Pero Perić", "pperic@mail.com"), ("Matej Matejić", "matejic@mail.com"), ("Ana Anić", "ana.anic@mail.com")]

try:
    sql_conn = sqlite3.connect(database_name)
    cursor = sql_conn.cursor()

    for djelatnik in djelatnici:
        cursor.execute(query_insert_into_table, djelatnik)

    sql_conn.commit()

    cursor.close()

except sqlite3.Error as e:
    print("Pogreška", e)

finally:
    if sql_conn:
        sql_conn.close()
        print("Veza prema SQL bazi je uspješno zatvorena.")

