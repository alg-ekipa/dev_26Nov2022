#Unos passworda

password='tajno'
unos=''
while  unos !=password:
    unos=input('Unesi password: ')
    if unos==password:
        print('Točno!')
    else:
        print('Krivi password! Pokušajte ponovno!')

while True:
    password=int(input('Unesite broj u rasponu od 10 do 20!  '))
    if broj>=10 and broj<=20:
        print('Uspješan unos!')
        break
    else:
        print('Broj nije u zadanom raspnu, kušajte ponovno!')