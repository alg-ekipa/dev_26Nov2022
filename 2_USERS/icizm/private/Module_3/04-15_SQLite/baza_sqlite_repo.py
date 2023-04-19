import sqlite3
from SQLite_repo1 import *

database_name = 'Proizvodi.db'

stol_insert = ('Lucija', '50x70x100', 'bijela')

query_create = ''' CREATE TABLE IF NOT EXISTS Stolovi
                    (
                    id INTEGER PRIMARY KEY,
                    naziv VARCHAR(30) NOT NULL,
                    dimenzija VARCHAR(20),
                    boja VARCHAR(20)
                    ); '''

db_connection = create_connection(database_name) # poziv funkcije iz SQLite_repo.py module - objedinjenesu funkcije koje smo do sad koristili

with db_connection: 
    create_table(db_connection, query_create)  # poziv funkcije kreiranja tablice

    create_stol(db_connection, stol_insert)