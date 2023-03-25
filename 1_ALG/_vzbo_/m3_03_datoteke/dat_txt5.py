# Korištenje strukture with open

counter = 1

while True:
    ime = input("Unesi ime: ")
    prezime = input("Prezime: ")
    mobitel = input("Mobitel: ")

    try: 
        with open('D:/Vesna/dev_26Nov2022/dev_26Nov2022/1_ALG/_vzbo_/m3_03_datoteke/adresar2.txt', 'a') as file_writer:
            redak = f'{counter};{ime};{prezime};{mobitel}\n'
            file_writer.write(redak)
            counter += 1

    except Exception as e:
        print(f'Dogodila se pogreška {e}')


    if input('Unos novog? ') != 'da':
        break