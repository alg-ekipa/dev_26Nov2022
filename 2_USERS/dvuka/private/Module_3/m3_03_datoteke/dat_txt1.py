#Pisanje

#Kreiranje varijable u koju se pohranjuje konekcija prema datoteci
# metoda open() definira ime datoteke i aktivnost koju radimo (r,w,a) . citanje, pisanje, dodavanje na kraju
# ako datoteka ne postoji, kreirati ce se
 

'''
outFileName="F:\\folder\\folder\\ime_test.txt"
outFile=open(outFileName, "w")
outFile.write("""Hello my name is ABCD""")
outFile.close()'''

save_path = 'C:/Users/grafika10/Desktop/dev_26Nov2022-1/2_USERS/dvuka/private/Module_3/m3_03_datoteke/ime.txt'
file_weiter = open(save_path, "w")

ime = input ("Unesi ime i prezime: ")

# upisivanje sadrzaja z datoteku
file_weiter.write(ime)

#zatvaranje konkekcije i otpuštanje resursa
file_weiter.close()

#ČITANJE

file_reader=open("ime.txt", "r")

file_data=file