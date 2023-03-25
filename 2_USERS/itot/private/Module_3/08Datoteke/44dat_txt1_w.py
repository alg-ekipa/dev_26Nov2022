#Pisanje

#Kreiranje varijable u koju se pohranjuje konekcija prema datoteci
# metoda open() definira ime datoteke i aktivnost koju radimo (r,w,a) . citanje, pisanje, dodavanje na kraju
# ako datoteka ne postoji, kreirati ce se
 


save_path = 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/08Datoteke/44ime_test.txt'
file_weiter = open(save_path, "w")

ime = input ("Unesi ime i prezime: ")

# upisivanje sadrzaja z datoteku
file_weiter.write(ime)

#zatvaranje konkekcije i otpuštanje resursa
file_weiter.close()