import sqlite3
from SQLite_repo_1 import *

database_name = 'C:/Users/office10.UCIONE/Desktop/hp/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/05_baza_podataka/Proizvodi.db'
stol_insert = ('Lucija','50x30x40','bijela')

query_create = ''' CREATE TABLE IF NOT EXISTS Stolovi
                    (
                    id INTEGER PRIMARY KEY,
                    naziv VARCHAR (30) NOT NULL,
                    dimenzija CARCHAR(20),
                    boja VARCHAR(20)
                    );
                '''
db_connection = create_connection(database_name)        #poziv funkcije iz SQLite_repo.py modula

with db_connection:
    create_table(db_connection, query_create)           #poziv funkcije - kreiranje tablice

    create_stol(db_connection, stol_insert)
