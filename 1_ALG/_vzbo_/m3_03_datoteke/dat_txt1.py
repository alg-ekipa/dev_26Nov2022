# PISANJE


# Kreiranje varijable u koju se pohranjuje konekcija prema datoteci
# metoda open() definira ime datoteke i aktivnost koju radimo (r, w, a) - čitanje, pisanje, dodavanje na kraj
# ako datoteka ne postoji, kreirat će se

file_writer = open("1_ALG/_vzbo_/m3_03_datoteke/ime.txt", "w")

ime = input("Unesi ime i prezime: ")

# upisivanje sadržaja u datoteku
file_writer.write(ime)

# zatvaranje konekcije i otpuštanje resursa
file_writer.close()