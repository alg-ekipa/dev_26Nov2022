"""
import os

absolute_path = os.path.dirname(__file__)
relative_path = "dev_26Nov2022\2_USERS\ikuke\datoteke\m3_datoteke"
full_path = os.path.join(absolute_path, relative_path)

"""
#pisanje


#kreiranje varijable u koju se pohranjuje konekcija prema datoteci
# metoda (open) definira ime datoteke i aktivnost koju     ,dodavanje na kraj
# #ako datoteka ne postoji, kreirat će se
# 
# 
# 

file1="adresar.txt"

#aktivnost nad datotekom je write
#file_writer = open(file1, "w") 
ime = input ("Unesi ime i prezime:") 
ime=ime+"\n"

#aktivnost nad datotekom je append
file_writer = open(file1, "a") 


# upisivanje sadržaja u datoteku
file_writer.write(ime)


#zatvaranje konekcija i otpuštanje resursa

file_writer.close()