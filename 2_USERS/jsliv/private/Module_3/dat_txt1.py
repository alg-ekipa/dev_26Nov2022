#Pisanje
#Kreiranje varijable u koju se pohranjuje konekcija prema datoteci
#Metoda open() definira ime datoteke i aktivnost koju radimo (r, w, a) čitanje pisanje, dodavanje na kraj
#Ako datoteka ne postoji, kreirati će se

file_writer = open("Ime.txt", "w")

ime = input("Unesi ime i prezime: ")

#Upisivanje sadržaja u datoteku

file_writer.write(ime)

#zatvaranje konekcije i otpuštanje resursa
file_writer.close()