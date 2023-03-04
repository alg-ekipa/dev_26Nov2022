import os

class bcolors:
    ZELENO = '\033[92m'
    ZUTO = '\033[93m'
    CRVENO = '\033[91m'
    KRAJ = '\033[0m'




def kreiraj_racun(brojac_racuna, datum, pdv):

    stavke = {}

    while True:
        proizvod= input ('Unesi proizvod: ')
        cijena= input ('Unesi cijenu proizvoda: ')
        stavke[proizvod] = cijena
        if not input('Unos nove stavke? Za ne pritisnite Enter'):
            break
    return stavke


brojac_r = 1
PDV=0.25
datum = '4.03.2023.'

"""
stavke = {
    'Laptop': 12000,
    'Monitor': 2000,
    'Miš    ': 100,
    'Tipkovnica': 150
}
"""

ukupno = 0
PDV = 0.25



racuni = {}


os.system('cls')



while True:
    kreirani_racun=kreiraj_racun(brojac_r, datum, PDV)
    racun_broj = f'R-{brojac_r}-2023'
    brojac_r+=1
    racuni[racun_broj] = kreirani_racun

    if not input('Zelite li novi racun? (Enter ako ne)'):
        break


"""

for proizvod, cijena in racuni.items():
    print(f" {proizvod} \t \t \t \t \t {cijena}")
"""

"""
for cijena in stavke.values():
    ukupno = ukupno + cijena
ukupno_PDV= ukupno*PDV


"""


ukupno = 0


for rbr , racun in racuni.items():
    print (rbr, racun)
    print (ukupno)

"""


print('---------------------------------------------------------')
print (f'ukupna cijena  \t \t \t \t-------> {ukupno} ')
print (f'           PDV \t \t \t \t-------> {ukupno_PDV}')
print (f'ukupno za platiti \t \t \t-------> {ukupno+ukupno_PDV}')
print()


"""