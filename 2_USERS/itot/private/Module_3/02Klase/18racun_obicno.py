# varijable
broj = 'R1-2023-01'
datum = '04.03.2023.'
stavke = {
    'Laptop' : 12000,
    'Monitor' : 2000,
    'Miš' : 100,
    'Tipkovnica' : 1200

}
ukupno = 0
PDV = 0.25

# IZRACUN IZNOSA RACUNA
for cijena in stavke.values():
    ukupno = ukupno + cijena
ukupno_PDV = ukupno*(1+PDV)

#Ispis
print(broj)
print(datum)
print('-'*25)
print('Proizvod\t\tCijena')
for proizvod, cijena in stavke.items():
    print(f'{proizvod}\t\t\t{cijena}')
print('-'*25)
print(f'Ukupno:\t\t\t{ukupno}')
print(f'PDV:\t\t\t{PDV}')