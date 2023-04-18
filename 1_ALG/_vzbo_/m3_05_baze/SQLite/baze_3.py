import sqlite3

# DODAVANJE PODATAKA U BAZU

database_name = 'Tvrtka.db'

query_insert_into_table = ''' INSERT INTO Employees1 (name, email)
                                VALUES (?, ?)
'''

djelatnici = [('Niko Nikic','nnikic@email.com'),('Kreso Kresic','kkresic@email.com')]


try: 
    sqliteConnection = sqlite3.connect(database_name)
    cursor = sqliteConnection.cursor()
    print('Baza je uspješno kreirana!')

    for djelatnik in djelatnici:
        cursor.execute(query_insert_into_table, djelatnik)

    sqliteConnection.commit()
    #print('Kreirana je tablica Employees!')

    cursor.close()
    print('Resursi objekta cursor su uspješno otpušteni!')

except sqlite3.Error as e:
    print(f'Dogodila se pogreška pri spajanju na SQLite: {e}')

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQL konekcija je uspješno zatvorena!')