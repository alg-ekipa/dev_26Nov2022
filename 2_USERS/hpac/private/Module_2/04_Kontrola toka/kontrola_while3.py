#Unos passworda


'''
password = 'tajno'
unos = ''
while unos != password:
    unos = input('Unesi password: ')
    if unos == password:
        print('Točno!')
    else:
        print('Krivi password! Pokušajte ponovno!')
'''
password = 'tajno' 

while True:
    unos = input('Unesi password: ')
    if unos == password:
        print('Password je točan!') 
        break
    else:
        print('Krivi password! Pokušajte ponovno!')