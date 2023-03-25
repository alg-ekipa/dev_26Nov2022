# PISANJE

# Kreiranje varijable u koje se pohranjuje konekcija prema datoteci
# metoda open definira ime datoteke i aktivnost koju radimo (read, write, append) (r, w, a)
# ako datoteka ne postoji, kreirat će se

file_writer = open('D:/python 26.11. grupa/dev_26Nov2022-1/2_USERS/zbene/private/Module_2/25.03.2023/ime.txt', 'w')

ime = input('Unesi ime i prezime: ')

# Upisivanje sadržaja u datotteku
file_writer.write(ime)

# zatvaranje konekcije i otpuštanje resursa
file_writer.close()

# Čitanje
file_reader = open('D:/python 26.11. grupa/dev_26Nov2022-1/2_USERS/zbene/private/Module_2/25.03.2023/ime.txt','r')

file_data = file_reader.read()
print(file_data)