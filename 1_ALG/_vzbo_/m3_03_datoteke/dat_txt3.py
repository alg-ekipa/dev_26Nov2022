# Višestruki unos osoba u adresar
counter = 1

while True:
    ime = input("Unesi ime: ")
    prezime = input("Prezime: ")
    mobitel = input("Mobitel: ")

    file_writer = open("D:/Vesna/dev_26Nov2022/dev_26Nov2022/1_ALG/_vzbo_/m3_03_datoteke/adresar1.txt", "a")
    redak = f'{counter};{ime};{prezime};{mobitel}\n'
    file_writer.write(redak)
    counter += 1

    if input('Unos novog? ') != 'da':
        break

file_writer.close()
