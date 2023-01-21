#Unos passworda
'''
password = 'tajno'
unos = ''
while unos != password:
    unos = input ('Unesi password: ')
    if unos == password:
        print('Točno')
    else:
        print('Krivi password! Pokušajte ponovo')
'''
password = 'tajno'
while True:
    unos = input('Unesite password: ')
    if unos == password:
        print('Uspješan unos!')
        break
    else:
        print('Password nije ispravan, pokušajte ponovo!')