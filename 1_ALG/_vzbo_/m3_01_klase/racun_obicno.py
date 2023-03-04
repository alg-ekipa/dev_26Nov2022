# VARIJABLE
broj = 'R1-2023-01'
datum = '4.03.2023.'
stavke = {
    'Laptop': 12000,
    'Monitor': 2000,
    'Miš': 100,
    
}
ukupno = 0
PDV = 0.25

# IZRAČUN IZNOSA RAČUNA
for cijena in stavke.values():
    ukupno = ukupno + cijena
ukupno_PDV = ukupno*(1+PDV)

# ISPIS RAČUNA
print(broj)
print(datum)
print('*'*35)
print('Proizvod\t\tCijena')
for proizvod,cijena in stavke.items():
    print(f'{proizvod}\t\t\t{cijena}')
print('-'*35)
print(f'UKUPNO:\t\t\t{ukupno_PDV}')
print(f'PDV:\t\t\t{ukupno*PDV}')
