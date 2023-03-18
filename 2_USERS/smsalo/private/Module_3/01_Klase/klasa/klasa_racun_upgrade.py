def kreiraj_racun(brojac_racuna, datum, pdv):
    
    stavke={}

    while True:
        proizvod=input('Unesi proizvod:')
        cijena=float(input('Unesi cijenu: '))
        stavke[proizvod]=cijena
        if not input('Unos nove stavke? Za NE pritisnite Enter!'):
            break
    return stavke

brojac_r=1
PDV=0.25
datum='04.03.2023.'

racuni={}

while True:
    kreirani_racun=kreiraj_racun(brojac_r, datum, PDV)
    racun_br=f'R-{brojac_r}-2023'
    brojac_r +=1
    racuni[racun_br]=kreirani_racun

    if not input('Želite li novi račun? Enter ako NE!'):
        break
for rbr, racun in racuni.items():
    print(rbr, racun)

