import sqlite3
from SQLite_repo1 import *
from stolovi import stolovi_rjecnik

database_name = 'Proizvodi.db'
stol_insert = ('Lucija','50x30x40','bijela')

query_create = ''' CREATE TABLE IF NOT EXISTS Stolovi
                    (
                    id INTEGER PRIMARY KEY,
                    naziv VARCHAR (30) NOT NULL,
                    dimenzija VARCHAR(20),
                    boja VARCHAR(20)
                    );
                '''
db_connection = create_connection(database_name)        #poziv funkcije iz SQLite_repo.py modula

with db_connection:
    create_table(db_connection, query_create)           #poziv funkcije - kreiranje tablice

    create_stol(db_connection, stol_insert)

print(stolovi_rjecnik)

query_inesert_into_table = ''' INSERT INTO Stolovi (naziv, dimenzija, boja)
                                    VALUES (?,?,?)
                        '''

for kljuc,vrijednost in stolovi_rjecnik.items(): # zavrtimo for petlju i tako izvucemo podatke
    #print(stolovi_rjecnik[kljuc][0])   #Ime
    #print(stolovi_rjecnik[kljuc][3]) 
    #print(stolovi_rjecnik[kljuc][4]) 

    sql_conn = sqlite3.connect(database_name)
    cursor = sql_conn.cursor()

    cursor.execute(query_inesert_into_table, ((stolovi_rjecnik[kljuc][0]), (stolovi_rjecnik[kljuc][3]) ,(stolovi_rjecnik[kljuc][4]))) 
    sql_conn.commit()

    cursor.close()