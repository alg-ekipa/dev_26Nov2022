#višestruki unos osoba u adresar
counter=1

while True:
    ime = input ("Unesi ime: ")
    prezime = input ("Unesi prezime: ")
    mobitel = input ("Unesi prezime: ")

    file_writer=open("C:/Users/grafika10/Desktop/dev_26Nov2022-1/2_USERS/dvuka/private/Module_3/m3_03_datoteke/adresar1.txt","a")
    redak=f'{counter};{ime};{prezime};{mobitel}\n'
    file_writer.write(redak)
    counter+=1

    if input('Unos novog? ')!='da':
        break

file_writer.close()