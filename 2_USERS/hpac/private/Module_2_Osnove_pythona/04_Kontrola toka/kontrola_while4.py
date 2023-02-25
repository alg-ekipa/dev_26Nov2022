#UNOS BROJA U NEKOM RASPONU, npr. između 10 i 20

''' (bez provjere unosli li korisnik znak/string ili broj)
while True:
    broj = int(input('Unesite broj urasponu do 10 do 20!    '))
    if 10 <= broj <= 20:
        print('Uspješan unos!')
        break
    else:
        print('Broj niju u zadanom rasponu, pokušajte ponovno!')
'''

while True:
    unos = input('Unesite broju rasponu od 10 do 20:   ')

    while unos.isdigit() == False:
        print('Krivi unos! Morate unijeti BROJ! Ponovite unos1')
        unos = input('Unesite broj u rasponu 10 do 20:   ')
    if int(unos) >= 10 and int(unos) <= 20:
        print('Uspješan unos!')
        break
    else:
        print('Broj nije u zadnom rasponu, pokušajte ponovno!')

#s='f'
#print(s.isdigit())