#Visestruki unos osoba u adresar
counter = 1
save_path = 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/08Datoteke/46adresar.txt'

while True:
    ime = input ("Unesi ime: ")
    prezime = input ("Unesi prezime: ")
    mobitel = input ("Unesi mobitel: ")

    file_weiter = open(save_path, "a")
    redak = f'{counter};{ime};{prezime};{mobitel}\n'
    file_weiter.write(redak)
    counter += 1

    if input('Unos novga? ') != 'da':
        break

file_weiter.close()