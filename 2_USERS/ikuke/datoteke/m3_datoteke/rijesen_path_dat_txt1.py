
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
putanja=putanja+"/"
print (absolute_path)
print (putanja)



#pisanje


#kreiranje varijable u koju se pohranjuje konekcija prema datoteci
# metoda (open) definira ime datoteke i aktivnost koju     ,dodavanje na kraj
# #ako datoteka ne postoji, kreirat će se
# 
# 
# 

file1=putanja+"datoteka.txt"

#aktivnost nad datotekom je write
#file_writer = open(file1, "w") 


#aktivnost nad datotekom je append
file_writer = open(file1, "a") 


ime = input ("Unesi ime i prezime:") 


# upisivanje sadržaja u datoteku
file_writer.write(ime)


#zatvaranje konekcija i otpuštanje resursa

file_writer.close()