# VARIJABLE
broj = 'R1-2023-01'
datum = '4.03.2023.'
stavke = {
    'Laptop' : 12000,
    'Monitor' : 2000,
    'Miš' : 100,
    }

ukupno = 0
PDV = 0.25

# Izračun iznosa računa
for cijena in stavke.values():
    ukupno = ukupno + cijena

ukupno_PDV = ukupno * (1+PDV)

# Izračun PDV-a
pdv_od_racuna = ukupno*PDV

# Ispis
print()
print(broj)
print(datum)
print('-'*25)
print('Proizvod\tCijena')
for proizvod,cijena in stavke.items():
    print(f'{proizvod}\t\t{cijena}')
print('*'*25)
print(f'UKUPNO:\t\t{ukupno_PDV}')
print(f'PDV:\t\t{pdv_od_racuna}')