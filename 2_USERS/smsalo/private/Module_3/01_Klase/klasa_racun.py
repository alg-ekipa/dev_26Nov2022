# VARIJABLE
broj='R1-2023-01'
datum='04.03.2023.'
stavke={
    'Laptop':12000,
    'Monitor': 2000,
    'Miš':100,
    'Tipkovnica':150
}

ukupno=0
PDV=0.25


for cijena in stavke.values():
    ukupno=ukupno+cijena
ukupno_pdv=ukupno*1.25
print(ukupno_pdv)

#ispis računa
print(broj)
print(datum)
print('-'*30)
print('Proizvod\t\tcijena')
for proizvod, cijena in stavke.items():
    print(f'{proizvod}\t\t\t{cijena}')
print('-'*30)
print(f'Ukupno:\t\t\t{ukupno_pdv}')
print(f'PVD:\t\t\t{ukupno*PDV}')
print('-'*30)