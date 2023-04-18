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


file1=vrati_putanju("datoteka4.txt")



counter = 1

while True:
    ime = input("Unesite ime: ")
    prezime = input("Prezime: ")
    mobitel = input("Mobitel: ")

    try:
        file_writer = open(file1, "a")
        redak = f'{counter};{ime};{prezime};{mobitel}\n'
        file_writer.write(redak)
        counter +=1

    except Exception as e:
        print(f'Dogodila se pogreška {e}')

    finally:
        file_writer.close()

    if input('Unos novog? ') != 'da':
        break