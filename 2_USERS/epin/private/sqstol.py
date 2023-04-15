import sqlite3
from sqlite_repo1 import *
from class7 import *

database_name = 'Proizvodi.db'
stolovi_tuple = list(stolovi_rjecnik.items())
print(stolovi_tuple)

query_create = '''CREATE TABLE IF NOT EXISTS Stolovi1
                  (
                  id INTEGER PRIMARY KEY,
                  naziv VARCHAR(20),
                  cijena REAL,
                  dostupnost BOOLEAN,
                  dimenzije VARCHAR(20),
                  boja VARCHAR(20),
                  materijal VARCHAR(20)
                  );'''
query_insert = '''INSERT INTO Stolovi1 (id, naziv, cijena, dostupnost, dimenzije, boja, materijal)
                  VALUES (?, ?, ?, ?, ?, ?, ?);'''

try: 
    sql_conn = sqlite3.connect(database_name)
    cursor = sql_conn.cursor()

    cursor.execute(query_create)

    for stol in stolovi_tuple:
        cursor.execute(query_insert, [stol[0]] + stol[1])

    sql_conn.commit()

    cursor.close()

except sqlite3.Error as e:
    print('Pogreška ', e)
finally:
    if sql_conn:
        sql_conn.close()
