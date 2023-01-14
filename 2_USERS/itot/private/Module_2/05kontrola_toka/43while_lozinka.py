'''unos lozinke'''

''' Prekida se nakon jedne 'vrtnje' petlje

password = 'tajno'
unos=input('Unesi lozinku: ')

if unos == password:
    print('Točno!')
else:
    print('Krivi!')
'''

password = 'tajno'
unos = ''

while unos != password:
    unos=input('Unesi lozinku: ')
    if unos == password:
        print('Točno!')
    else:
        print('Krivi! Pokušajte ponovo')



while True:
    unos = input('Unesi lozinku: ')
    if unos == 'tajna':
        print('Dobro!')
        break
else:
    print('kriva lozinka, pokušajte ponovo!')
