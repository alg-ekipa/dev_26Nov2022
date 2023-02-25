#unesi niz brojeva kred kartice, koje će onda prikazati kao *************1234

broj_kartice = input('Unesi broj kartice: ')
duljina = len(broj_kartice)

i=0

while i < duljina-4:
    if i != '-':
        print('*',end='')
        i+=1
    else:
        ignore
print(broj_kartice[-4:])

