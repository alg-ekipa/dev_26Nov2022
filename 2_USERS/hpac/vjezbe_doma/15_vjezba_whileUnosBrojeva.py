#UNOS BROJA U NEKOM RASPONU, npr. između 10 i 20

while True:
    unos = input('Unesi broj u rasponu brojeva 10-20: ')

    while unos.isdigit() == False:
        print('Krivi unos! Pokušajte ponovno, broj u rasponu 10-20.')
        unos = input('Unesi broj u rasponu brojeva 10-20: ')
    if int(unos) < 21 and int(unos) >9:
        print('Uspješan unos')
        break
    else: 
        print('Broj nije u zadanom rasponu.')