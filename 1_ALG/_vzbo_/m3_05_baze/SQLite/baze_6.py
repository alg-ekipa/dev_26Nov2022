import sqlite3

# BRISANJE PODATAKA IZ BAZE

database_name = 'Tvrtka.db'

query_delete_table = ''' DELETE FROM Employees1 WHERE id=?'''

try: 
    sqliteConnection = sqlite3.connect(database_name)
    cursor = sqliteConnection.cursor()
    print('Baza je uspješno kreirana!')

    cursor.execute(query_delete_table, (3,))
    

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