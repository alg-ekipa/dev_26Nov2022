import sqlite3

from SQLite_repo1 import *

database_name = "Proizvodi.db"

stol_insert = ("Lucija", "50 x 30 x 40", "bijela")

query_create = """ CREATE TABLE IF NOT EXISTS Stolovi
                    (
                    id INTEGER PRIMARY KEY,
                    naziv VARCHAR(30) NOT NULL,
                    dimenzije VARCHAR(20),
                    boja VARCHAR(20)
                    ); """

db_connection = create_connection(database_name)   #poziv funkicje iz SQLite_repo.py modula

with db_connection:
    create_table(db_connection, query_create)     #poziv funkcije - kreiranje tablice

    create_stol(db_connection, stol_insert)