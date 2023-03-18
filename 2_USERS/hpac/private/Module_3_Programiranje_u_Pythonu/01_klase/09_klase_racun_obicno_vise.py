def kreiraj_racun(brojac_racuna, datum, pdv):
    stavke = {}
    while True:
        proizvod = input ('Unesi proizvod: ')
        cijena = float(input('Unesi cijenu proizvoda: '))
        stavke[proizvod] = cijena
        if not input('Unos nove stavke? Za NE pritisnite ENTER'):
            print()
            break
        print()
    
    return stavke

brojac_r = 1
PDV = 0.25
datum = '4.3.2023.'

racuni = {}

while True:
    kreirani_racun = kreiraj_racun(brojac_r, datum, PDV)
    racun_broj = f'R-{brojac_r}-2023'
    brojac_r += 1
    racuni[racun_broj] = kreirani_racun

    if not input('Želite li novi račun? (ENTER ako ne želite)'):
        print()
        break
    print()

for rbr,racun in racuni.items():
    print(rbr, racun)