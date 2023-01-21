# klasičan primjer Unos PASSWORDA

password = 'tajno'
unos = input('Unesi password: ')
unos = ''
while unos != password:
    unos = input('Unesi password: ')
    if unos == password:
        print('Točno!')
    else:
        print('Krivi password! >pokušajte ponovno!')
