# Korištenej strukture with open

counter = 1

while True:
    ime = input('Unesi ime: ')
    prezime = input ('Unesi prezime: ')
    mobitel = input('Mobitel: ')

    try:
        with open('D:/HP/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/03_datoteke/adresar2.txt','a') as file_writer:
            redak = f'{counter},{ime},{prezime},{mobitel}\n'
            file_writer.write(redak)
            counter +=1

    except Exception as e:
        print(f'Dogodila se pogreška {e}')

    

    if input('Unos novog? ') != 'da':
        break