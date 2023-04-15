import sqlite3
from SQLite_repo1 import *

database_name= 'Proizvodi_stolovi.db'

stolovi_rjecnik = {
    '0186': ['stol Jack', 700.00, True, 'smeđa', 'drvo', 4],
    '0203': ['stol Kathy', 880.00, True, 'smeđa', 'staklo', 3],
    '1234': ['stol Tomy', 1250.00, True, 'bijela', 'staklo', 4],
    '4002': ['stol Ohm', 940.00, True, 'crna', 'metal', 1],
    '0923': ['stol Heda', 940.00, False, 'crna', 'drvo', 1],
    '1773': ['stol Lucas', 940.00, True, 'crna', 'drvo', 4]
}
stol_insert=[]
for i, j in stolovi_rjecnik.items():
    stol_insert.append((i, j[0], j[1], j[2],j[3],j[4],j[5]))

query_create= '''CREATE TABLE IF NOT EXISTS Stolovi
                    (
                    id INTEGER PRIMARY KEY,
                    naziv VARCHAR(30) NOT NULL,
                    cijena FLOAT,
                    raspolozivost BOOL,
                    boja VARCHAR(30),
                    materijal VARCHAR(30),
                    komada INTEGER
                    );'''                           #PAZI ;

db_connection = create_connection(database_name)  #poziv funkcije iz SQLite_repo.py modula

with db_connection:
    create_table(db_connection, query_create)

    for stolovi in  stol_insert:
        create_stolovi(db_connection, stolovi)

