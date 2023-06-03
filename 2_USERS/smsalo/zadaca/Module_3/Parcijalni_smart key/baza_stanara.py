
import sqlite3


#baza stanara
create_table_query = """CREATE TABLE Stanari (
            ime text,
            prezime text,
            pin text
            )"""
database_name = "Stanari_kljuc.db"

try:
    sql_connect = sqlite3.connect(database_name)
    cursor = sql_connect.cursor()
    cursor.execute(create_table_query)
    cursor.execute("INSERT INTO Stanari VALUES ('Admin', 'Admin', '1234')")
    cursor.execute("INSERT INTO Stanari VALUES ('Ante', 'Kovačić', '1111')")
    cursor.execute("INSERT INTO Stanari VALUES ('Tin', 'Ujević', '2222')")

    sql_connect.commit()
    record_all = cursor.fetchall()

    cursor.close()

except sqlite3.Error as e:
    print('Pogreška: ', e)

finally:
    if sql_connect:
        sql_connect.close()


