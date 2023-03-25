
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
    with open (file1) as file_writer:
    #file_writer = open(file1, "a") 



        while True:
            ime=input('Unesi ime: ')
            prezime=input('Unesi prezime: ')
            mobitel=input('Unesi mobitel: ')

            
            redak = f'{counter};{ime};{prezime};{mobitel};\n'
            file_writer.write(redak)


            counter +=1
            if input ('Unos novog? ') != 'da':
                break

except:
    print('desila se pogreška')

#finally:
#    file_writer.close()




