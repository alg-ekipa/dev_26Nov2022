#Unos broja u nekom rasponu, Npr. između 10 i 20
''' (bez provjere unosi li korisnik znak/string ili broj)
while True:
    broj = int(input('Unesite broj u rasponu od 10 do 20: '))
    if 10 <= broj <= 20:
        print('Uspješan unos!')
        break
    else:
        print('Broj nije u zadanom rasponu, pokušajte ponovo!')
'''

while True:
    unos = input('Unesite broj u rasponu od 10 do 20: ')
    while unos.isdigit()==False:
        print('Krivi unos! Morate unijeti broj! Ponovite unos!')
        unos = input('Unesite broj u rasponu od 10 do 20: ')
    #print(type(unos))
    if 10 <= int(unos) <= 20:
        print('Uspješan unos!')
        break
    else:
        print('Broj nije u zadanom rasponu, pokušajte ponovo!')

#s = '123'
#print(s.isdigit())