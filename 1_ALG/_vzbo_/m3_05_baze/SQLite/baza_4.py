import sqlite3

# ČITANJE I DOHVAT PODATAKA IZ TABLICE

query_select_table = ''' SELECT * FROM Employees1 WHERE id=?'''

database_name = 'Tvrtka.db'

try: 
    sqliteConnection = sqlite3.connect(database_name)
    cursor = sqliteConnection.cursor()
    print('Baza je uspješno kreirana!')

    cursor.execute(query_select_table, (2,))
    records = cursor.fetchall()
    print(records)
    

    cursor.close()
    print('Resursi objekta cursor su uspješno otpušteni!')

except sqlite3.Error as e:
    print(f'Dogodila se pogreška pri spajanju na SQLite: {e}')

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQL konekcija je uspješno zatvorena!')