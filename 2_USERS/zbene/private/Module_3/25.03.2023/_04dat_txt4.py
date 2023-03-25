#Višestruki unos osoba u adresar 

counter = 1

while True:
    ime = input('Unesi ime: ')
    prezime = input ('Unesi prezime: ')
    mobitel = input('Mobitel: ')

    try:
        file_writer = open('D:/python 26.11. grupa/dev_26Nov2022-1/2_USERS/zbene/private/Module_3/25.03.2023/adresar2.txt', 'a')
        redak = f'{counter};{ime};{prezime};{mobitel}\n'
        file_writer.write(redak)
        counter +=1

    except Exception as e:
        print (f'dogodila se pogreška {e}')

    finally:
        file_writer.close()

    if input ('Unos novog? ') != 'da':
        break