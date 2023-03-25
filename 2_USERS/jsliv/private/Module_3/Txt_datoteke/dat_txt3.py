#Unos višestrukih osoba u adresar

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

file1=putanja+"adresar1.txt"

#aktivnost nad datotekom je append
#file_writer = open(file1, "a") 


counter = 1

while True:
    ime = input("Unesite ime: ")
    prezime = input("Prezime: ")
    mobitel = input("Mobitel: ")

    file_writer = open(file1, "a")
    redak = f"{counter}; {ime}; {prezime}; {mobitel}\n"
    file_writer.write(redak)
    counter +=1

    if input("Unos novog? ") != "da":
        break

file_writer.close()

