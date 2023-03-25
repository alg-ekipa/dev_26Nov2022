# Korištenje try - except - finally strukture

counter = 1

while True:
    ime = input('Unesi ime: ')
    prezime = input ('Unesi prezime: ')
    mobitel = input('Mobitel: ')

    try:
        file_writer = open('D:/HP/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/03_datoteke/adresar1.txt','a')
        redak = f'{counter}. ;{ime };{prezime };{mobitel}\n'
        file_writer.write(redak)
        counter +=1

    except Exception as e:
        print(f'Dogodila se pogreška {e}')

    finally:
        file_writer.close()

    if input('Unos novog? ') != 'da':
        break