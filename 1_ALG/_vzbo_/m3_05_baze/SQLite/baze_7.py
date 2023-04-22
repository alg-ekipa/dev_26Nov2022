import sqlite3
from SQLite_repo import *

query_create = '''CREATE TABLE IF NOT EXISTS Emp (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE);
                '''
djelatnici = [('Niko Nikic','nnikic@email.com'),('Kreso Kresic','kkresic@email.com')]

database = 'Tvrtka.db'

db_connection = create_connection(database)

with db_connection:
        create_table(db_connection, query_create)  # poziv iz repo - kreiranje tablice

        for djelatnik in djelatnici:
            create_employee(db_connection, djelatnik)  # poziv iz repo - dodavanje djelatnika


