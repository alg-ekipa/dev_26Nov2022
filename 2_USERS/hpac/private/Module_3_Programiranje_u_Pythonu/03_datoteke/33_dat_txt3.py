# VIšestruki unos osoba u adresar

counter = 1

while True:
    ime = input('Unesi ime: ')
    prezime = input ('Unesi prezime: ')
    mobitel = input('Mobitel: ')

    file_writer = open('D:/HP/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/03_datoteke/adresar1.txt','a')
    redak = f'{counter}. ;{ime };{prezime };{mobitel}\n' 
    file_writer.write(redak)
    counter +=1
    if input('Unos novof? ') != 'da':
        break

file_writer.close()
