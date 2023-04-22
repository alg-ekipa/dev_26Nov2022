import sqlite3

# KREIRANJE TABLICE UNUTAR BAZE

query_create = '''CREATE TABLE IF NOT EXISTS Employees1 (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE);
                '''

database_name = 'Tvrtka.db'

try: 
    sqliteConnection = sqlite3.connect(database_name)
    cursor = sqliteConnection.cursor()
    print('Baza je uspješno kreirana!')

    cursor.execute(query_create)
    sqliteConnection.commit()
    print('Kreirana je tablica Employees1!')

    cursor.close()
    print('Resursi objekta cursor su uspješno otpušteni!')

except sqlite3.Error as e:
    print(f'Dogodila se pogreška pri spajanju na SQLite: {e}')

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQL konekcija je uspješno zatvorena!')