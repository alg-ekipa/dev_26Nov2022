import sqlite3


#AŽURIRANJE PODATAKA

query_update = '''  UPDATE Djelatnici
                    SET ime=?, kontakt=? WHERE id=?'''


# varijabla s imenom baze
database_name = 'Tvrtka.db'



try: #kreiramo konekciju prema bazi, ako baza ne postoji, kreirat će se
    sqlite_connection = sqlite3.connect(database_name)

    #kreiramo objekt cursor koji omogućava sve aktivnosti nad bazom
    cursor = sqlite_connection.cursor()
    print('baza je uspješno kreirana')



    # izvršavanje koda u SQL sintaksi
    cursor.execute(query_update, ('Luka Lukić', 'lukec@mail.com', 2))
    sqlite_connection.commit


    #otpuštanje resursa koje je zauzeo objekt cursor
    cursor.close()
    print ('resursi objekta cursor su uspješno otpušteni')





#ukoliko dođe do pogreške pri spajanju na bazu
except sqlite3.Error as e:
    print('pogreškas: ', e)





#zatvaranje konekcije prema bazi
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print('veza prema sql bazi je uspješno zatvorena')