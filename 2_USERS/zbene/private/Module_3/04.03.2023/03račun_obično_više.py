def kreiraj_račun (brojač_računa, datum, pdv):
    
    stavke = {}

    while True:
        proizvod = input ('\nUnesi proizvod: ')
        cijena = float (input ('Unesi cijenu proizvoda: '))
        stavke [proizvod] = cijena
        if not input ('\nUnos nove stavke? Za prekid pritisnite Enter. '):
            break

    return stavke

brojač_r = 1
PDV = 0.25
datum = '04.03.2023.'

računi = {}

while True:
    kreirani_račun = kreiraj_račun (brojač_r, datum, PDV)
    račun_broj = f'R-{brojač_r}-2023'
    brojač_r +=1
    računi [račun_broj] = kreirani_račun
    if not input ('\nUnos nove stavke? Za prekid pritisnite Enter. '):
        break

for rbr, račun in računi.items():
    print (rbr, račun)