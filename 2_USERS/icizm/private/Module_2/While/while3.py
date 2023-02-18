#Unos passworda

password = 'tajno'
unos = '' #možemo ga staviti kao prazan string prije nego idemo sa while kako bi imali tu varijablu

while unos != password: #postavljano uvijet različiti nego u IFu
    unos = input('Unesi password: ')
    if unos == password:
        print('Točno')
    else:
        print('Krivi password! Pokušajte ponovno!')

