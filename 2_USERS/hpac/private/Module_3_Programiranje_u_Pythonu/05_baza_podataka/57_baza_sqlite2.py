import sqlite3
from SQLite_repo_2 import *

stolovi_rjecnik = {
    '0186' : ['stol Jack', 700.00, True, '120x90x80', 'smeđa', 'drvo'],
    '0203' : ['stol Kathy', 880.00, True, '130x90x80', 'smeđa', 'drvo'],
    '1234' : ['stol Tomy', 1250.00, True, '150x100x90', 'bijela', 'drvo'],
    '4002' : ['stol Ohm', 940.00, True, '120x90x80', 'crna', 'metal'],
    '0923' : ['stol Heda', 940.00, False, '120x90x80', 'crna', 'metal'],
    '1773' : ['stol Lucas', 940.00, True, '120x90x80', 'crna', 'drvo']
   }

#stolovi_lista = [(k,v) for k,v in stolovi_rjecnik.items()]


stolovi_lista = []
for k,v in stolovi_rjecnik.items():
    stolovi_lista.append((k, v[0],v[1],v[2],v[3],v[4],v[5]))
print(stolovi_lista)

database_name = 'C:/Users/office10.UCIONE/Desktop/hp/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/05_baza_podataka/Proizvodi2.db'
#stol_insert = ('Lucija','50x30x40','bijela')

query_create = ''' CREATE TABLE IF NOT EXISTS Stolovi
                    (
                    id INTEGER PRIMARY KEY,
                    sifra VARCHAR(20),
                    naziv VARCHAR (30) NOT NULL,
                    cijena FLOAT(7 ,2),
                    dostupnost BOOLEAN,
                    dimenzija VARCHAR(20),
                    boja VARCHAR(20),
                    materijal VARCHAR(20)
                    );
                '''
db_connection = create_connection(database_name)        #poziv funkcije iz SQLite_repo.py modula

with db_connection:
    create_table(db_connection, query_create)           #poziv funkcije - kreiranje tablice

    for stol in stolovi_lista:
    #create_stol(db_connection, stol_insert)
        create_stol(db_connection, stol)




