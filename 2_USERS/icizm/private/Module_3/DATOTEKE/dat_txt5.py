# WITH OPEN 


counter = 1

while True: 
    ime = input('Unesi ime: ')
    prezime = input('Unesi prezime: ')
    mobitel = input('Unesi mobitel: ')

    try: 
        with open('adresar2.txt', 'a') as file_writer: 
            redak = f'{counter}; {ime}; {prezime}; {mobitel}\n'
            file_writer.write(redak)
            counter += 1

    except Exception as e: 
        print('Dogodila se pogreška {e}')


    if input('Unos novog? ') != 'da':
        break