#Višestruki unos osoba u adresar 

counter = 1

while True:
    ime = input('Unesi ime: ')
    prezime = input ('Unesi prezime: ')
    mobitel = input('Mobitel: ')

    file_writer = open('D:/python 26.11. grupa/dev_26Nov2022-1/2_USERS/zbene/private/Module_2/25.03.2023/adresar1.txt', 'a')
    redak = f'{counter};{ime};{prezime};{mobitel}\n'
    file_writer.write(redak)
    counter +=1
    
    if input ('Unos novog? ' != 'da'):
        break

file_writer.close()