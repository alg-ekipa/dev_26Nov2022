
# unosis broj sve dok se ne upise broj izmedu 10 i 20, bez provjere da li unosi broj ili string
'''

while True:
    broj = int(input('Unesite broj od 10 do 20: '))
    if 10 < broj < 20:
        print('Uspjesan unos!')
        break
    else:
        print('Broj nije u zadanom rasponu, pokušajte ponovo!')'''



while True:
    unos = input('Unesi broj od 10 do 20: ')
    while unos.isdigit() == False:
        print('Krivi unos, morate unijeti broj, ponovo unos!')
        unos = input('Unesi broj od 10 do 20: ')
    if 10 < int(unos) < 20:
        print('Uspjesan unos!')
        break
    else:
        print('Broj nije u zadanom rasponu, pokušajte ponovo!')

print('END!')