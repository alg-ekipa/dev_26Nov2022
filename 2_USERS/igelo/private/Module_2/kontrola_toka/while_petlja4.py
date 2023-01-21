#UNOS BROJA U NEKOM RASPONU
"""  ---bez provjere unosi li korisnik znak ili broj
while True:
    broj = int(input('Unesite broj u rasponu od 10 do 20! '))
    if broj >= 10 and broj <= 20:
        print('Uspješan broj!')
        break
    else:
        print('Broj nije u zadanom rasponu! Pokušajte ponovno!')

"""

while True:
    unos = (input('Unesite broj u rasponu od 10 do 20! '))

    while unos.isdigit() == False:
        print('Krivi unos! Morate unijeti broj! Ponovite unos!')
        unos = input('Unesite broj u rasponu od 10 do 20! ')

    if int(unos) >= 10 and int(unos) <= 20:
        print('Uspješan unos!')
        break
    else:
        print('Broj nije u zadanom rasponu! Pokušajte ponovno! ')




#s = '123asd'
#print(s.isdigit()) 

