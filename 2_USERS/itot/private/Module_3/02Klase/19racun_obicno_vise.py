
def kreiraj_racun(brojac_racuna,datum, pdv):

    stavke = {}

    while True:
        proizvod = input('Unesi proizvod: ')
        cijena = float(input('Unesi cijenu proizvodda: '))
        stavke[proizvod]= cijena
        if not input(('Unesi nove stavke? Za NE pritisnite Enter')):
            break
    return stavke


brojac_r = 1
PDV=0.25
datum = '04.03.2023.'

racuni = {}

while True:
    kreirani_racun = kreiraj_racun(brojac_r, datum, PDV)
    racun_broj = f'R-{brojac_r}-2023'
    brojac_r += 1
    racuni[racun_broj] = kreirani_racun

    if not input('Zelite li novi racun: (Enter ako NE)'):
        break

for rbr,racun in racuni.items():
    print(rbr, racuni)

