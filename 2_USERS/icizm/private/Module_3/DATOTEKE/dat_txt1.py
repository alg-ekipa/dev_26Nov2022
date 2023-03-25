# PISANJE

# Kreiranje varijable u koju se pohranjuje konekcija prema datoteci 
# Meoda open definira ime datoteke i aktivnost koju raimo (r, w, a) - čitanje, pisanje i dodavanje na kraju
# Ako datoteka ne postoji, kreirat će se 

file_writer = open("ime.txt", "w")  

ime = input('Unesi ime i prezime: ')

# Upisivanje sadržaja u datoteku
file_writer.write(ime)

# Zatvaranje konekcije i otpuštanje resursa
file_writer.close()

# Najjednostavniji kod sa 3 osnovna koraka
# kako nismo lokalno onda može se u terminalu koristiti change directory ili cd i iskopirati path u kojem radimo kako bi se tamo napravio txt file kojeg trebamo a da nije skroz vani


# ČITANJE

file_reader = open("ime.txt", "r")

file_data = file_reader.read()

print(file_data)
