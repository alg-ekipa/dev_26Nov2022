#Pisanje
#Kreiranje varijable u koju se pohranjuje konekcija prema datoteci
#Metoda open() definira ime datoteke i aktivnost koju radimo (r, w, a) čitanje pisanje, dodavanje na kraj
#Ako datoteka ne postoji, kreirati će se
#save_path = 'D:/VisualStudioCode/Juli/dev_26Nov2022/2_USERS/jsliv/private/Module_3/Txt_datoteke/ime.txt'
#file_writer = open(save_path, "w")

#file_writer = open("Ime.txt", "w")
import os
os.system('cls')

absolute_path = os.path.dirname(__file__)
print(absolute_path)
putanja=""

i=len(absolute_path)
for k in range (i):
    slovo=absolute_path[k]
    if slovo == "\\" :
        putanja=putanja+"/"
    else:
        putanja=putanja+slovo

print (absolute_path)
print (putanja)

file1=putanja+"datoteka.txt"

#aktivnost nad datotekom je append
file_writer = open(file1, "a") 


ime = input ("Unesi ime i prezime:") 


# upisivanje sadržaja u datoteku
file_writer.write(ime)


#zatvaranje konekcija i otpuštanje resursa

file_writer.close()

