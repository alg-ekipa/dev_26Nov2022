# PISANJE

# Kreiranje varijable u koje se pohranjuje konekcija prema datoteci
# metoda open definira ime datoteke i aktivnost koju radimo (read, write, append) (r, w, a)
# ako datoteka ne postoji, kreirat će se

file_writer = open('ime.txt', 'w')

ime = input('Unesi ime i prezime: ')

# Upisivanje sadržaja u datotteku
file_writer.write(ime)

# zatvaranje konekcije i otpuštanje resursa
file_writer.close()