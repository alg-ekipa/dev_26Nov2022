import sqlite3

from SQLite_repo1 import *

database_name = "Proizvodi.db"

#stol_insert = ("Lucija", "50 x 30 x 40", "bijela")

stol_insert = []

for k, v in stolovi_rijecnik.items():
    stol_insert.append((k, v[0], v[1], v[2], v[3], v[4], v[5]))
print(stol_insert)

query_create = """ CREATE TABLE IF NOT EXISTS Stolovi
                    (
                    šifra TEXT,
                    naziv VARCHAR(30) NOT NULL,
                    cijena FLOAT (7, 2),
                    raspolozivost BOOL,
                    dimenzije VARCHAR(20),
                    boja VARCHAR(20),
                    materijal VARCHAR(20)
                    ); """

db_connection = create_connection(database_name)   #poziv funkicje iz SQLite_repo.py modula

with db_connection:
    create_table(db_connection, query_create)     #poziv funkcije - kreiranje tablice

    create_stol(db_connection, stol_insert)

    for stol in stol_insert:
        create_stol(db_connection, stol)