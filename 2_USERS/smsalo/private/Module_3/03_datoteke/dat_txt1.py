# PISANJE


# kretiranje varijable u koju se pohranjuje konecija prema datoteci
# metoda open() definira ime datoteke i aktivnost koju radimo (r, w, a ) read, write, append
# ako datoteka ne postoji, kreirat će se 

file_writer = open('D:/dev_26Nov2022-1/2_USERS/smsalo/private/Module_3/03_datoteke/ime.txt', 'w')

ime=input('Unesi ime i prezime: ')

file_writer.write(ime)          #UPISIVANJE SADRŽAJA U DATOTEKU

file_writer.close()               #zatvaranje datoteke


# ČITANJE

file_reader = open('D:/dev_26Nov2022-1/2_USERS/smsalo/private/Module_3/03_datoteke/ime.txt', 'r')
file_data = file_reader.read()
file_reader.close()
print(file_data)
