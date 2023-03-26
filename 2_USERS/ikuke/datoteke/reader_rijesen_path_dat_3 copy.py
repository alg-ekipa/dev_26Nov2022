
import os
os.system('cls')



def vrati_putanju(datoteka):
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
    print (putanja+datoteka)
    #input()

    return putanja+datoteka



#pisanje


#kreiranje varijable u koju se pohranjuje konekcija prema datoteci
# metoda (open) definira ime datoteke i aktivnost koju     ,dodavanje na kraj
# #ako datoteka ne postoji, kreirat će se
# 
# 
# 

file1=vrati_putanju("datoteka3.txt")

#aktivnost nad datotekom je write
#file_writer = open(file1, "w") 


#višestruki unos osoba u adresar
counter=1
try:
    with open(file1) as file_reader:
        print(type(file_reader))
        file_data = file_reader.read()
        for red in file_reader:
            dijelovi_retka = red.split(';')
            print(dijelovi_retka)
            redni_broj= red[0]
            ime=red[1]
            prezime=red[2]
            mob=red[3].rstrip()
            print(redni_broj, ime, prezime, mob)
except Exception as e:
    print (f'Pogreska: {e}')
