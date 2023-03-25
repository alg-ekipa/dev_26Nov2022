#Pisanje
#Kreiranje varijable u koju se pohranjuje konekcija prema datoteci
#Metoda open() definira ime datoteke i aktivnost koju radimo (r, w, a) čitanje pisanje, dodavanje na kraj
#Ako datoteka ne postoji, kreirati će se
save_path = 'D:/VisualStudioCode/Juli/dev_26Nov2022/2_USERS/jsliv/private/Module_3/Txt_datoteke/ime.txt'
file_writer = open(save_path, "w")

#file_writer = open("Ime.txt", "w")

ime = input("Unesi ime i prezime: ")

#Upisivanje sadržaja u datoteku

file_writer.write(ime)

#zatvaranje konekcije i otpuštanje resursa
file_writer.close()

#Čitanje

file_reader = open("ime.txt", "r")

file_date = file_reader.read()

