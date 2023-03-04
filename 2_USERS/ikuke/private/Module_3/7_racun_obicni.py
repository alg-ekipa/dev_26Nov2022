import os

class bcolors:
    ZELENO = '\033[92m'
    ZUTO = '\033[93m'
    CRVENO = '\033[91m'
    KRAJ = '\033[0m'





broj ="R1-2023-01"
datum = '4.03.2023.'
stavke = {
    'Laptop': 12000,
    'Monitor': 2000,
    'Miš    ': 100,
    'Tipkovnica': 150
}
ukupno = 0
PDV = 0.25



os.system('cls')

for proizvod, cijena in stavke.items():
    print(f" {proizvod} \t \t \t \t \t {cijena}")


for cijena in stavke.values():
    ukupno = ukupno + cijena
ukupno_PDV= ukupno*PDV



print('---------------------------------------------------------')
print (f'ukupna cijena  \t \t \t \t-------> {ukupno} ')
print (f'           PDV \t \t \t \t-------> {ukupno_PDV}')
print (f'ukupno za platiti \t \t \t-------> {ukupno+ukupno_PDV}')
print()
