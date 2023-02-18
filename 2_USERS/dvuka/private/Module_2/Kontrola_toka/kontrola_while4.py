#unos broja u nekom rasponu, npr. između 10 i 20
''' bez provjere unosi li korisnik string ili broj
while True:
    broj=int(input('Unesite broj u rasponu od 10 do 20!  '))
    if broj>=10 and broj<=20:
        print('Uspješan unos!')
        break
    else:
        print('Broj nije u zadanom raspnu, kušajte ponovno!')
 '''

while True:
    unos=input('Unesite broj u rasponu od 10 do 20!  ')

    while unos.isdigit()==False:
        print('Krivi Unos! Morate unijeti Broj! Ponovite unos! ')
        unos=input('Unesite broj u rasponu od 10 do 20! ')
    #print(type(unos))
    if int(unos)>=10 and int(unos) <=20:
        print('Uspješan Uns!')
        break
    else:
        print('Broj nije u zadanom rasponu , pokušajte ponovno!')

#s='123asd'

#print(s.isdigit())