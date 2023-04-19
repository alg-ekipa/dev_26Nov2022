import sqlite3

# AŽURIRANJE PODATAKA (REDAKA)

query_update_table = ''' UPDATE Employees1 SET name=?, email=? WHERE id=?
                        '''

database_name = 'Tvrtka.db'

try: 
    sqliteConnection = sqlite3.connect(database_name)
    cursor = sqliteConnection.cursor()
    print('Baza je uspješno kreirana!')

    cursor.execute(query_update_table, ('Ana Ivic','aanic@email.com', 2))
    sqliteConnection.commit()
    
    cursor.close()
    print('Resursi objekta cursor su uspješno otpušteni!')

except sqlite3.Error as e:
    print(f'Dogodila se pogreška pri spajanju na SQLite: {e}')

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQL konekcija je uspješno zatvorena!')