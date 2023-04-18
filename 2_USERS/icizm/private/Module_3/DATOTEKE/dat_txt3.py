# Višestruki unos ocoba u adresar 
counter = 1

while True: 
    ime = input('Unesi ime: ')
    prezime = input('Unesi prezime: ')
    mobitel = input('Unesi mobitel: ')

    file_writer = open('adresar1.txt', "a")
    redak = f'{counter};{ime};{prezime};{mobitel}\n'
    file_writer.write(redak)
    counter += 1

    if input('Unos novog? ') != 'da':
        break

    file_writer.close()