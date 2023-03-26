# korištenje try-except-finally strukture

counter = 1

while True: 
    ime = input('Unesi ime: ')
    prezime = input('Unesi prezime: ')
    mobitel = input('Unesi mobitel: ')

    try: 
        file_writer = open('adresar3.txt', "a")
        redak = f'{counter};{ime};{prezime};{mobitel}\n'
        file_writer.write(redak)
        counter += 1

    except Exception as e: 
        print('Dogodila se pogreška {e}')

    finally: 
        file_writer.close()

    if input('Unos novog? ') != 'da':
        break

   