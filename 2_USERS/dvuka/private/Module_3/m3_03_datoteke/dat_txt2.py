#Pisanje

#Kreiranje varijable u koju se pohranjuje konekcija prema datoteci
# metoda open() definira ime datoteke i aktivnost koju radimo (r,w,a) . citanje, pisanje, dodavanje na kraju
# ako datoteka ne postoji, kreirati ce se
 


save_path = 'C:/Users/grafika10/Desktop/dev_26Nov2022-1/2_USERS/dvuka/private/Module_3/m3_03_datoteke/adresar.txt'
file_weiter = open(save_path, "a")

ime = input ("Unesi ime: ")
prezime = input ("Unesi prezime: ")
mobitel = input ("Unesi prezime: ")

# upisivanje sadrzaja z datoteku
file_weiter.write('Ime\tPrezime\tMobitel\n')
file_weiter.write(f'{ime}\t{prezime}\t{mobitel}\n')

#zatvaranje konkekcije i otpuštanje resursa
file_weiter.close()