import sqlite3
from SQLite_repo_1 import *
from DBstolovi import stolovi_rjecnik as sr

database_name = 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/11Baze/73Proizvodi.db'


query_create = ''' CREATE TABLE IF NOT EXISTS Stolovi
                    (
                    id INTEGER PRIMARY KEY,
                    sifra CARCHAR(20),
                    naziv VARCHAR (30),
                    cijena INTEGER,
                    dimenzija CARCHAR(20),
                    boja VARCHAR(20),
                    materijal VARCHAR(20)
                    );
                '''
db_connection = create_connection(database_name)        #poziv funkcije iz SQLite_repo.py modula

with db_connection:
    create_table(db_connection, query_create)           #poziv funkcije - kreiranje tablice

query_inesert_into_table = ''' INSERT INTO Stolovi (sifra, naziv, cijena, dimenzija, boja, materijal)
                                    VALUES (?,?,?,?,?,?)
                        '''

for k,v in sr.items(): # zavrtimo for petlju i tako izvucemo podatke

    sql_conn = sqlite3.connect(database_name)
    cursor = sql_conn.cursor()

    cursor.execute(query_inesert_into_table, (k,(sr[k][0]), (sr[k][1]) ,(sr[k][3]),(sr[k][4]),(sr[k][5]))) 
    sql_conn.commit()

    cursor.close()
