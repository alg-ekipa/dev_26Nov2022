import sqlite3

#Kreiranje tablice unutar baze

#Upit kojim kreiramo tablicu. String u koji pišemo SQL kod.

query_create = """ CREATE TABLE IF NOT EXISTS Djelatnici
                    (
                    id INTEGER PRIMARY KEY,
                    ime VARCHAR(30) NOT NULL,
                    kontakt VARCHAR(20)                
                    );"""
#Varijabla s imenom baze
database_name = "Tvrtka.db"

try:
    sql_connection = sqlite3.connect(database_name)
    cursor = sql_connection.cursor()
    print("Baza je uspješno kreirana.")

    cursor.execute(query_create)
    sql_connection.commit()  #dodatni korak "potvrde" pri konekciji
    print("Kreirana je tablica djelatnici")

    cursor.close()
    print("Resursi objekta cursor su otpušteni.")

except sqlite3.Error as e:
    print("Pogreška", e)

finally:
    if sql_connection:
        sql_connection.close()
        print("Veza prema SQL bazi je uspješno zatvorena.")


